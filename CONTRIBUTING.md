# Contributing to shop-easy-api

## Branch names

| Type | Pattern | Example |
|---|---|---|
| Feature | `feature/SHOP-<id>-<description>` | `feature/SHOP-1042-forgot-password` |
| Bug fix | `bugfix/SHOP-<id>-<description>` | `bugfix/SHOP-1080-email-error` |
| Hotfix | `hotfix/SHOP-<id>-<description>` | `hotfix/SHOP-1099-password-reset` |
| Release | `release/<major>.<minor>` | `release/2.4` |

## Workflow

```bash
git switch main
git pull
git switch -c feature/SHOP-1234-short-description
# ...work, in small commits...
git status
git diff
git add <files>
git commit -m "Describe what this commit does"
pytest
git push -u origin feature/SHOP-1234-short-description
```

Then open a Pull Request into `main`.

## Commit messages

- Imperative mood, short first line: `Add password reset flow`, not `added stuff`.
- One logical change per commit. Don't mix unrelated changes. Stage only what belongs.

## Pull Requests

- Fill in the template: what changed, how it was tested, the Jira ticket.
- Required: 1 approval and a green CI check. CODEOWNERS reviews are required for their areas.
- If `main` has moved and your PR conflicts, `git fetch origin` and update your branch
  (merge `origin/main` or rebase onto it, as the team prefers), re-run the tests, then push.

## Undoing things

- Uncommitted change to a file: `git restore <file>`
- Local commit that was never pushed: `git reset`
- Commit that is already shared: `git revert <hash>`. Never force-push to `main`.
