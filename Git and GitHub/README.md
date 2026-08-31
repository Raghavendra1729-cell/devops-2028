# Git and GitHub

**Name:** Raghavendra

**Enrollment number:** 24BCS10250

I used a small practice repository to compare commit commands, create a branch, and cherry-pick one commit.

## 1. `git commit -a -m` vs `git commit -m`

| Command | What it does |
| --- | --- |
| `git commit -m "message"` | Commits changes that are already staged with `git add`. |
| `git commit -a -m "message"` | Automatically stages modified and deleted **tracked files**, then commits them. |

The `-a` option does not include a new untracked file. A new file must be added with `git add` first.

I modified the already tracked `README.md` and committed it without running `git add` again:

```console
git status --short
 M README.md
git commit -a -m "Add Git basics"
[main 836bca1] Add Git basics
 1 file changed, 2 insertions(+)
```

## 2. Create commits on `main`

I created three commits before making the feature branch:

```console
git log --oneline --decorate -3
7292894 (HEAD -> main) Document Git commands
836bca1 Add Git basics
3f65ea2 Create Git practice lab
```

## 3. Create a branch and add commits

```console
git switch -c feature-notes
Switched to a new branch 'feature-notes'
```

I made three commits on `feature-notes`:

```console
git log --oneline --decorate -3
5f0b9b2 (HEAD -> feature-notes) Add status reminder
0ea9897 Explain cherry-pick
7daff05 Add branching note
```

## 4. Cherry-pick one commit

I selected `0ea9897`, switched back to `main`, and applied only that commit:

```console
git switch main
Switched to branch 'main'
git cherry-pick 0ea9897
[main 09a3b5e] Explain cherry-pick
 Date: Mon Aug 31 18:37:49 2026 +0530
 1 file changed, 3 insertions(+)
 create mode 100644 cherry-pick.md
```

The new commit has a different hash because Git applied the selected change on top of a different branch history.

## 5. Final history

```console
git log --graph --oneline --decorate --all
* 5f0b9b2 (feature-notes) Add status reminder
* 0ea9897 Explain cherry-pick
* 7daff05 Add branching note
| * 09a3b5e (HEAD -> main) Explain cherry-pick
|/
* 7292894 Document Git commands
* 836bca1 Add Git basics
* 3f65ea2 Create Git practice lab
```

The final graph shows the commits on both branches and the selected commit copied to `main` with cherry-pick.

![Git history after cherry-pick](Screenshot%202026-08-31%20at%207.49.28%E2%80%AFPM.png)
