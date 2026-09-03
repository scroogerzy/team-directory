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

