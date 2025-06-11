"""
1. What is a Git repository?
A Git repository stores a project's files and revision history and facilitates version 
control by tracking changes made over time. It can be located locally within a folder on 
your device or an online platform like GitHub. This enables users to collaborate, revert 
to previous versions, and efficiently manage project development using commands like commit, 
push, and pull.

2. How does Git work?
Git operates by recording changes made to files and directories in a project, capturing 
snapshots of its evolving condition. Users can oversee alterations, create branches for 
simultaneous development, merge branches, and revert to previous states if required. It 
also promotes collaboration and ensures effective version control in software development 
endeavors.

3. What is git add?
The git add command is used in Git to stage changes for inclusion in the next commit. It 
prepares modifications, additions, or deletions made to files in the working directory, 
marking them to be included in the upcoming commit snapshot. Note this command does not 
actually commit the changes but prepares them for staging.

4. What is git push?
The git push command is used in Git to upload local repository content to a remote repository. 
It transfers committed changes from the local repository to a remote one, typically on a server 
like GitHub or GitLab. This command enables collaboration by allowing users to share their 
changes with others on the same project.

5. What is git status?
The git status command displays the current state of the repository in Git. It provides information 
about which files have been modified, which are staged for the next commit, and which are untracked. 
It helps users track the progress of their work and identify any changes that need to be committed 
or staged.

6. What is a commit in Git?
A commit represents a snapshot of the changes made to files in a repository at a specific point in 
time. When you commit changes in Git, you are effectively saving the current state of your files and 
can provide a descriptive message that explains the changes made (which is recommended).

Each commit creates a unique identifier, allowing you to track the history of changes in the repository. 
Commits play a crucial role in version control, as they provide a way to revert to previous states of 
the project, review the history of changes, and collaborate with others by sharing updates.

7. What is branching in Git?
Branching refers to the practice of diverging from the main line of development (typically called 
the "master" branch) to work on new features, fixes, or experiments without affecting the main 
codebase. It allows multiple parallel lines of development to coexist within the same repository.

Each branch represents a separate line of development with its own set of commits, enabling 
developers to work on different features or fixes simultaneously. Branching facilitates 
collaboration, experimentation, and organization within a project, as changes made in one 
branch can be merged back into the main codebase once they are completed and tested.

8. What is a conflict in Git?
Conflicts arise when conflicting changes are made to the same part of a file or files by different 
contributors, typically during a merge or rebase operation. Git cannot automatically resolve 
these conflicting changes, requiring manual intervention by the user to resolve the discrepancies.

Thus, to resolve conflicts, the conflicted files must be reviewed and edited based on the best 
suited reconciliation before the resolved version is committed.

9. What is merge in Git?
Merging is a fundamental operation in Git that facilitates collaboration and the integration of 
changes across different branches in a project. Namely, a merge is the process of combining the 
changes from different branches into a single branch, typically the main branch (e.g., master or main).

A merge integrates the changes made in one branch with another, resulting in a new commit that 
combines the histories of both branches.

10. What is a remote in Git?
A remote is a repository hosted on a server or another computer for collaboration and sharing code 
with others. It serves as a centralized location where developers can push their local changes and 
pull changes made by others.

Remotes are typically set up on hosting platforms like GitHub, GitLab, or Bitbucket, and they enable 
distributed development and facilitate teamwork by providing a common location for storing and 
synchronizing project code among multiple contributors.

11. What is the difference between git fetch and git pull?
The main difference between git fetch and git pull lies in what they do and how they update the 
local repository.

The git fetch command retrieves changes from a remote repository to the local repository. It updates 
the remote-tracking branches (e.g., origin/master) in the local repository to reflect the state of 
the remote repository, but it does not update the working directory or merge any changes into the 
current branch. This means that after fetching, you can review the changes made in the remote 
repository without affecting your local work.

The git pull command also retrieves changes from a remote repository, but it goes a step further by 
fetching changes and merging them into the current branch in one step. It essentially performs a 
git fetch followed by a git merge to incorporate the changes from the remote repository into the 
current branch.

12. How do you revert a commit that has already been pushed and made public?
The git revert <commit-hash> command can be used to revert a commit that has already been pushed and made public.

The step-by-step process is as follows:

1. Identify the commit you want to revert to by finding its commit hash. This can be done using the 
git log command to view the commit history and find the commit hash you want to revert.

2. Once you have the commit hash, use the git revert command followed by the commit hash to create a 
new commit that undoes the changes introduced by the specified commit. For example:
git revert <commit-hash>

3. Git will open a text editor to create a commit message for the revert. You can edit the message 
if needed, then save and close the editor.

4. After saving the commit message, Git will create a new commit that effectively undoes the changes 
introduced by the specified commit. This new commit will be added to the history, effectively reverting 
the changes made by the original commit.

5. Finally, push the new commit to the remote repository to make the revert public using the following 
command:
git push origin <branch-name> 

Using git revert creates a new commit that undoes the changes introduced by the original commit, 
effectively reverting the changes without altering the commit history. This approach is safer than 
git reset or git amend, which can alter the commit history and cause issues for collaborators who 
have already pulled the changes.

13. What does git reset do?
The git reset command resets the current HEAD to a specified state. This means it can be used to 
undo changes, unstage files, or move the HEAD pointer to a different commit. Note there are three 
main modes of git reset:

--soft: Resets the HEAD pointer to a specific commit, keeping changes staged. Files remain modified 
in the working directory, allowing you to re-commit them.
--mixed: Resets the HEAD pointer to a specific commit, unstaging changes. Files remain modified in 
the working directory, but changes are not staged for commit.
--hard: Resets the HEAD pointer to a specific commit, discarding all changes in the working directory 
and staging area. Use with caution, as it permanently deletes uncommitted changes.

14. What is git stash?
git stash is a Git command that temporarily stores changes in the working directory that are not 
ready to be committed. It allows developers to save their modifications without committing them to 
the repository.

Stashing is useful when switching branches, but you don't want to commit or lose your changes. Later, 
you can apply the stashed changes to your working directory or pop them off the stash stack to 
continue working on them.

15. What is git reflog?
git reflog is a Git command used to view the reference logs, which record changes to the HEAD pointer 
and the history of commits that have been checked out in the repository. It provides a chronological 
list of recent actions performed in the repository, including commits, checkouts, merges, and resets.

The reflog is helpful for recovering lost commits or branches and understanding the sequence of actions 
taken in the repository.
"""