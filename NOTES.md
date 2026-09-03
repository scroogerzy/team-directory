# Git Fundamentals Assignment Notes

## Question 1 — What is worth its own commit?

### Category A: High-value commit boundaries

1. Add project structure
A separate commit makes it easy to review the initial setup.

2. Add main application logic
This allows future developers to isolate changes to core behaviour.

3. Add data storage
Keeping data changes separate helps track changes independently.

4. Add search feature
A feature should have its own commit because it can be reviewed or reverted.

### Category B: Changes NOT worth a separate commit

1. Small spelling mistakes fixed immediately.
They add unnecessary commits and make history noisy.

2. Formatting-only changes.
They make reviews harder because they hide important changes.

### Category C: .gitignore scope

I ignored .env files and log files because they may contain secrets or unnecessary output. If committed, removing them later would require rewriting history.



## Question 2 — Choosing merge vs rebase

Merge preserves the real branch history and creates a merge commit.
Rebase creates a cleaner linear history but rewrites commit history.

For the conflict task, I will use merge because it demonstrates how Git handles two independent changes.



## Question 3 — Remote operations inventory

git push:
Uploads local commits to GitHub.

git pull:
Downloads changes from GitHub.

git clone:
Copies a repository from GitHub.

git fetch:
Downloads remote history without merging.

GitHub cannot verify if local code quality is correct because it only stores committed files.



## Question 4 — Commit messages

a. "fixed stuff" 
Bad. Replace with:
"Fix incorrect directory output"

b. "Update index.js"
Too implementation-focused.
Replace with:
"Display team members"

c. "WIP"
Bad.
Replace with:
"Add team search functionality"

d. "Add email format validation so invalid addresses cannot be submitted"
Good.

e. "asdasd"
Bad.
Replace with:
"Add team data validation"

f. "Changed line 47 of notes.md"
Bad.
Replace with:
"Document Git workflow decisions"
## Intentional Conflict Resolution

The conflict happened because both branches changed the same line in README.md. Git could not automatically decide which version should remain. I resolved it by combining the useful information from both branches into one final README version.

## Team Summary Feature

I added a team summary to make it easier to see the size of the team without counting the members manually. It shows the total number of members as well as how many people are in each role, which should make the directory more useful as the team grows.

## Assignment 1.2

### Question 1 — Why fork, not branch, this time?

In Assignment 1.1 I worked inside my own repository where I already had write access. In Assignment 1.2 I contributed to another person's repository, so I needed to fork their repository first. Forking creates my own copy where I can make changes and push branches without needing permission on the original repository. If I only cloned my partner's repository, I would not be able to push branches directly unless I had been given write access.

### Question 2 — PR description: bad vs. good

Bad PR Description:

Added role search.

Good PR Description:

What:
Added a role search feature that allows users to search for team members by role.

Why:
The application previously only supported searching by name. This change makes it easier to find all team members with a specific role.

How to verify:
1. Run python main.py.
2. Enter an existing role.
3. Confirm matching team members are displayed.
4. Enter a role that does not exist.
5. Confirm a not found message is displayed.

The second description is easier to review because it explains the purpose of the change and gives clear testing steps for the reviewer.

### Question 3 — Triaging review comments

A blocking comment identifies a problem that should be fixed before the code is merged. A nit or suggestion is an optional improvement that does not prevent merging. A question asks for clarification or additional information.

If a reviewer does not label a comment, I will treat it as blocking if it affects correctness, usability, or maintainability. Otherwise, I will treat it as a suggestion or question.

### Question 4 — When fetch beats pull

I would use git fetch before git pull when I want to inspect changes on origin/main before updating my local branch. This allows me to see new commits, review incoming work, and check for potential conflicts before merging those changes into my local repository.

### What you contributed, and why you chose it

I contributed a role search feature to my partner's team-directory project. I chose it because the application could already search by name, but there was no way to find team members by role. This makes the directory more useful when working with larger teams.

### A comment you received that changed your code

My reviewer pointed out that the role search was displaying the "not found" message twice when no matching role existed. I fixed the logic so the message only appears once, improving the user experience and output accuracy.

### A comment you gave that you stand by

I requested that the new team summary feature be documented in NOTES.md before merging. I believe this was important because future contributors should understand why the feature was added and how it improves the project.

### Fetch vs. pull, in practice

After running git fetch, I was able to inspect the remote changes before updating my local branch. I could see commits from another contributor on origin/main before they were merged into my local copy. This showed me that fetch is useful when I want to review incoming changes before running git pull.