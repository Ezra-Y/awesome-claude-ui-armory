#!/usr/bin/env python3
"""Update the ⭐N star counts in README.md / README.zh-CN.md.

Only touches table cells that are *already* in the `⭐N` form (Community
entries). Cells holding `—` (Official / Mine) are never modified.

Uses only the Python standard library — no third-party deps to install.
GitHub REST API is queried with the GITHUB_TOKEN env var (set by the
workflow's default GITHUB_TOKEN). Each unique repo is queried at most once
per run (deduped via an in-memory cache); 403/429 responses skip that repo
and leave the existing value untouched.
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()

# Files to scan, relative to the repo root (the script's parent dir).
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(SCRIPT_DIR)
README_FILES = [os.path.join(REPO_DIR, "README.md"),
                os.path.join(REPO_DIR, "README.zh-CN.md")]

# A markdown table data row beginning with a link cell and ending with a
# star cell that is either ⭐N or — . Anchored to start/end of line so header
# and separator rows (and prose lines) are ignored.
ROW_RE = re.compile(
    r"^\|\s*\[([^\]]+)\]\((https?://[^)]+)\)\s*\|(?P<middle>.*)\|"
    r"\s*(?P<stars>⭐\d+|—)\s*\|\s*$"
)

STAR_NUM_RE = re.compile(r"⭐(\d+)")
# Match lines ending in a ⭐N star cell, so we only ever rewrite the trailing
# star number and never an emoji that might (theoretically) appear in a desc.
TRAILING_STAR_RE = re.compile(r"⭐\d+(?=\s*\|\s*$)")

# Gentle pause between API calls to stay well clear of secondary rate limits.
REQUEST_DELAY = 0.4


def extract_repo(url):
    """Return 'owner/repo' for a github.com URL, or None.

    Accepts trailing /tree/<branch>/... paths and a trailing .git.
    """
    m = re.match(r"https?://github\.com/([^/]+)/([^/?#]+)", url)
    if not m:
        return None
    owner, repo = m.group(1), m.group(2)
    if owner.endswith(".git"):  # implausible, but defensive
        return None
    if repo.endswith(".git"):
        repo = repo[:-4]
    if not owner or not repo:
        return None
    return "{}/{}".format(owner, repo)


def fetch_stars(repo):
    """Return stargazers_count for owner/repo, or None on any failure."""
    url = "https://api.github.com/repos/{}".format(repo)
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "awesome-claude-ui-armory-star-updater")
    if TOKEN:
        req.add_header("Authorization", "Bearer {}".format(TOKEN))
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("stargazers_count")
    except urllib.error.HTTPError as e:
        if e.code in (403, 429):
            sys.stderr.write("  rate-limited on {}, skipping\n".format(repo))
        else:
            sys.stderr.write("  HTTP {} for {}, skipping\n".format(e.code, repo))
        return None
    except Exception as e:  # network / parse errors
        sys.stderr.write("  error for {}: {}\n".format(repo, e))
        return None


def collect_repos(text):
    """Scan file text and return the set of owner/repo needing lookups."""
    repos = set()
    for line in text.splitlines(keepends=True):
        m = ROW_RE.match(line)
        if not m:
            continue
        stars = m.group("stars")
        if not STAR_NUM_RE.fullmatch(stars):
            continue  # `—` cell — leave alone
        repo = extract_repo(m.group(2))
        if repo:
            repos.add(repo)
    return repos


def apply_updates(text, stars_map):
    """Rewrite star cells in text, return (new_text, changedbool, updates)."""
    new_lines = []
    changed = False
    updates = []
    for line in text.splitlines(keepends=True):
        m = ROW_RE.match(line)
        if not m:
            new_lines.append(line)
            continue
        stars = m.group("stars")
        if not STAR_NUM_RE.fullmatch(stars):
            new_lines.append(line)
            continue  # `—` — never touch
        repo = extract_repo(m.group(2))
        if not repo or repo not in stars_map:
            new_lines.append(line)
            continue  # couldn't fetch — preserve existing value
        actual = stars_map[repo]
        old = int(STAR_NUM_RE.match(stars).group(1))
        if old == actual:
            new_lines.append(line)
            continue
        new_line = TRAILING_STAR_RE.sub("⭐{}".format(actual), line, count=1)
        if new_line != line:
            changed = True
            updates.append((repo, old, actual))
        new_lines.append(new_line)
    return "".join(new_lines), changed, updates


def main():
    # Phase 1: collect the unique set of repos to query across both files.
    texts = {}
    repo_set = set()
    for path in README_FILES:
        with open(path, "r", encoding="utf-8") as f:
            texts[path] = f.read()
        repo_set |= collect_repos(texts[path])

    if not repo_set:
        print("No ⭐N Community rows found; nothing to do.")
        return 0

    print("Looking up {} unique repos...".format(len(repo_set)))

    # Phase 2: query each repo once (in-memory cache = the stars_map).
    stars_map = {}
    for repo in sorted(repo_set):
        s = fetch_stars(repo)
        if s is not None:
            stars_map[repo] = s
            print("  {}: {}".format(repo, s))
        time.sleep(REQUEST_DELAY)

    print("Fetched {}/{} repos.".format(len(stars_map), len(repo_set)))

    # Phase 3: apply updates; only write a file if it actually changed.
    any_changed = False
    for path in README_FILES:
        new_text, changed, updates = apply_updates(texts[path], stars_map)
        if not changed:
            print("No changes for {}".format(os.path.basename(path)))
            continue
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(new_text)
        any_changed = True
        for repo, old, actual in updates:
            print("  {} {} -> {} in {}".format(repo, old, actual, os.path.basename(path)))

    if not any_changed:
        print("All star counts already current; no commit needed.")
    else:
        print("Updated star counts written to README files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
