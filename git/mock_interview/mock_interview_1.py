"""
Q1. What is a Git repository, and how does it help with collaboration in software development?

A Git repository is a version control system that tracks code changes. It enables multiple developers 
to collaborate by allowing branching, merging, code reviews, and shared history.
Git Repository solves the issue of code collaboration by having an environment where all developers
can change the code, have code reviews and work simultanoues on many different features at the same
time.

Q2. Imagine you've made several changes to a file, but you're not ready to commit them yet. What does 
git add do in this case, and how does it differ from git commit?

git add command stage the changes made to the code, but it indeed does not commit them yet. It works
as a preview step of what the commit would be. Let's say you are working on a bug fix that needs to
update two functions on a code, you could fix each of them and use git add and once both fixes are done
you can commit the bug fix changes.

Q3. You're working on a new feature and want to isolate your work from the main codebase. How does 
Git branching help in this scenario?

In this scenario, you could pull the main code from a Git Repository such as GitHub into your local
machine, after that you just need to use "git checkout -b feature". Once you've finished the update
on the code you push it to the remote repository and merge it. On this workflow you can easily
work on the branch without affecting the production branch code.

Q4. During a git pull, you encounter a merge conflict. What steps would you take to resolve it?

Conflicts happen when the code you have does not follow the same structure of the code within the
GitHub repository and this could happen for many reasons. In this scenario you should resolve the
conflicts on a code editor such as VSCode, in this step you can choose what you want to maintain in
the code that comes from the remote origin and what you actually want to maintain from your local
machine repository.

Q5. What is the difference between git fetch and git pull, and when would you use one over the other?

There is a big difference from the given commands:

1. git fetch retrieves changes made on the remote repository to the local repository, but does not
update the local repository neither commit any changes to it
2. git pull goes on step further and merge the changes made on the remote repository into the local
branch

Q6. Let's say you've accidentally pushed a commit to a public branch. How would you safely revert 
that change without altering commit history?

To safely revert a commit in a public branch without altering history, I would use 
git revert <commit-hash>. This creates a new commit that undoes the changes, keeping the commit 
history intact and safe for collaboration.

Q7. Explain the use cases for the three modes of git reset: --soft, --mixed, and --hard.

Q8. What is git stash, and can you give an example of when it would be useful during development?
git stash is a feature of git commonly used by developers to save changes to a branch without the need
to make any changes into the working repository. It allows developers to save their modifications without
commiting them to the repository.

stashing is usefull when you want to change branchs without having to commit updates you have done into
your local code.
"""