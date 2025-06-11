"""
How to start a git repository?
git init

How to clone a repository from any online repository?
git clone <url>

How to update git folders?
git add .

How to check for changes?
git status

How to commit the changes after they were updated on git folder?
git commit -m "<commit message>" -m "<commit description>"

How to update the repository located outside of the local machine
git push -u origin <branch name>
git push

We use -u here so that the branch is remembered for futures pushs

How to update the local repository based on the latest changes made on cloud
repository?
git pull

How to list all git branchs?
git branch

How to delete a branch?
git branch -D <branch name>

How to create a new branch?
git checkout -b <new branch name>

How to create remote origin?
git remote add origin <repository url>

How can I unstage file from git?
If you have used for example:
git add app.py
You could unstage the changes by using the command:
git reset app.py

How to undo a commit?
1. This moves the current branch back by one commit, effectively undoing the last commit.
git reset --hard HEAD~1
git reset HEAD~1
"--hard" is used to completely remove changes made on future branchs

2. This resets your current branch's HEAD to the last commit fetched from the remote 
repository, discarding any local changes.
git reset --hard origin/HEAD

3. Typically used after a fetch to reset to what was fetched.
git reset --hard FETCH_HEAD

How to go back to a version of the code on a commit?
git reset --hard <commit id>
git reset --hard <commit id>
"""