# Git Commands Cheat Sheet

## 🔹 Basic Setup
```bash
git config --global user.name "Your Name"      # Set your username
git config --global user.email "you@example.com"  # Set your email
git config --list                              # View configuration
git config --global --unset user.name          # Remove username setting
git config --global --unset user.email         # Remove email setting
git config --unset <key>                       # Remove specific config setting
rm ~/.gitconfig                                # Delete entire global Git config file
```

## 🔹 Starting a Repository
```bash
git init                   # Initialize a new Git repository
git clone <repo-url>       # Copy an existing repository
```

## 🔹 Basic Workflow
```bash
git status                 # Show the status of files
git add <file>             # Add a file to staging area
git add .                  # Add all changes in current directory
git commit -m "message"    # Commit staged changes
git log                    # Show commit history
git diff                   # Show unstaged changes
git diff --staged          # Show staged changes
```

## 🔹 Branches
```bash
git branch                  # List branches
git branch <branch-name>    # Create a new branch
git checkout <branch-name>  # Switch to another branch
git checkout -b <branch-name> # Create & switch to new branch
git merge <branch-name>     # Merge a branch into current one
git branch -d <branch-name> # Delete a branch
```

## 🔹 Remote Repositories
```bash
git remote -v               # Show remotes
git remote add origin <url> # Add a remote repository
git push origin <branch>    # Push commits to remote
git pull origin <branch>    # Fetch & merge from remote
git fetch                   # Download latest changes (without merging)
```

## 🔹 Undo / Fix / Delete
```bash
git reset <file>            # Unstage a file
git reset --hard            # Discard all local changes
git revert <commit-id>      # Undo a commit by creating a new one
git checkout -- <file>      # Discard changes in a file
git rm <file>               # Remove file from Git and working directory
git rm --cached <file>      # Remove file from Git but keep in working directory
git clean -fd               # Remove untracked files and directories
```

## 🔹 Stash (Temporary Save)
```bash
git stash                   # Save uncommitted changes temporarily
git stash pop               # Reapply stashed changes
git stash list              # View stashed changes
```

## 🔹 Inspection
```bash
git show <commit-id>        # Show details of a commit
git blame <file>            # Show who changed each line
git tag                     # List tags
git tag <tag-name>          # Create a new tag
```
