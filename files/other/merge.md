# [Merging two git repositories](http://blog.caplin.com/2013/09/18/merging-two-git-repositories/)
*on Sep 18, 2013 in Stuff we like by Jeremy Herr*

Today I would like to tell you about why and how we recently merged two git repositories, and the complications we encountered.

I’ve found myself in the situation a couple times, most recently on a project here at Caplin, where a project team started out with front- and back-end code in different places and then later ended up consolidating it. The code was originally kept separate for convenience so that set-up work could be done in isolation. Having different repositories initially made it easier to track revision history (fewer commits to look at). It also made life easier for the front-end developers, who could stick with a particular stable commit whilst the back-end was ongoing massive changes, only getting back-end updates when things were working. Later, as the project got fully underway and we started writing integration tests, it became a headache to have our code divided into two repositories. So we decided to merge the two repositories into one.

Let’s call our two repos A and B for now. The easiest thing to do would be simply to copy all the files from B into A and commit that, but then we would lose all of B’s revision history. We could keep repository B around as a reference, but nobody would want to go look up a deprecated repository that is kept only for historical information. Worse, this invites the possibility that someone will mistakenly commit new code to the deprecated repo.

Our goal was to merge the repositories, preserving the revision history of both in one repository. Essentially our procedure was to declare one repository to be a remote of the other, then merge the remote master branch into the other’s.

## Basic example: merge repo B into repo A

Let’s keep calling the repos A and B for the moment, assume we are merging B into A, and consider the following simple example first. We’ll create a remote inside A pointing to B, then merge B’s master branch into A’s master branch.

Clone both repositories into the same directory and go into repo A:

```bash
$ git clone A
$ git clone B
$ cd A
```

Add a remote called B that points to the repo B (do `git remote -v` to view your remotes), and fetch copies of all B’s branches:

```bash
$ git remote add B ../B
$ git fetch B
```

To view all B’s branches that we’ve just fetched, do git branch -a. You should see B/master in the list. Now, still in repo A, create a branch called B-master in repo A that tracks B/master.

```$ git branch B-master B/master```

If you’re not already in the master branch, check it out, then merge B-master into A’s master.

```$ git merge B-master```

Assuming you have no merge conflicts, you’re done!

## Should I merge A into B or B into A?

How do you decide which repo to merge into the other? The short answer is: merge the smaller one into the bigger one. We merged our front-end repo into our back-end repo, because:

    There were fewer developers working on the front-end repo in the beginning. When it came time to merge, we didn’t want to do it more than once. Given the complications we encountered, it took a couple hours before we had the merged repository ready, so we asked all front-end developers to stop committing to the old repository before we started the merge, and then resume working in the new location after we were finished. We didn’t want to interrupt more developers than necessary.
    There were fewer unmerged feature branches on the front-end repo. It’s not impossible to merge in more branches later, but because of the hurdles outlined below, merging each branch is a bit of a hassle. So we wanted to leave the repository with the most unmerged branches alone.
    The back-end repository had a longer revision history, and more files with history. We wanted all the front-end code to go under a new client folder, into which we moved every single file in the front-end repo. This means that when tracking the entire history of a single file, the history only goes back to when it was moved, so we wanted to move as few files as possible (more details on this below).

## Complications: submodules, moving files and tags

A few things made our procedure more involved than the simple example above.

The presence of submodules in the front-end repository made things a bit tricky. Our front-end code uses the CaplinTrader SDK, and instead of just dumping the code into our repository, we track it separately in its own repo. Some teams always use the latest release of the SDK every time the project is built, but our team prefers to keep it in a separate repository, and include this in our project as a submodule. I plan on discussing some benefits of submodules in another post, but as far as merging repos, dealing with submodules was a pain.

We moved all our front-end files into a new folder called client, and we wanted to bring any tags across, so these added to the steps below.

## The glorious details

Our goal is to merge the front-end repo (henceforth known as front-end-repo) master branch into the back-end-repo master branch, moving all front-end files into a new folder client/ and bringing our sdk submodule along. We want to preserve front-end-repo revision history and any tags on master, and since we don’t have many unmerged feature branches, we won’t worry about those for the moment.

This merge won’t affect back-end developers at all; they should see a new client/ folder appear in the repo, and if they want to build the whole project, they’ll be able to do so all in the same repo, but nothing else will change for them.

First let’s freshly clone both repositories. NB: We will spend the entire time inside back-end-repo.

In back-end-repo, add a remote pointing to front-end-repo, and fetch copies of all front-end-repo‘s branches.

```bash
$ git clone user@git.server.caplin.com:/git/front-end-repo.git
$ git clone user@git.server.caplin.com:/git/back-end-repo.git
$ cd back-end-repo/
$ git remote add front-end-remote ../front-end-repo
$ git fetch front-end-remote
```

Create branch front-end-master to hold the entire master branch from front-end-repo and check it out.

$ git checkout -b front-end-master front-end-remote/master

In front-end-master, move everything into a new folder, client/. Now that we’re moving these files, if we want to look at the complete revision history of a file, that history will only go back in time to the point when we moved it. We can see the earlier history by looking at the old path where the file used to be.

```bash
$ mkdir client
$ git mv README.md client/
$ git mv apps client/
$ git mv js-patches client/
$ git mv conf client/
$ git commit -m "Moved front-end-repo files and folders into client/"
```

Remove the submodule in front-end-master. Submodules are a bit finicky and it seems the only way to move them over is to delete all traces of them then add them later in the back-end-repo.

```bash
$ git rm .gitmodules
$ git rm --cached sdk
$ git commit -m "Deleted sdk submodule"
$ rm -rf sdk # git doesn't delete folders
```

Merge front-end-master into back-end-repo master

```bash
$ git co master
$ git merge front-end-master
```

The only conflicts we had were in .gitignore, easily resolved.

```bash
$ git add .gitignore
$ git commit -m "Merged front-end-master (master branch from deprecated front-end-repo) into master"
```

Add the submodule back into client/.

```bash
$ git submodule add ../sdk client/sdk
$ git commit -m "Added sdk submodule"
```

Bring front-end-repo tags over. If none of your tag names collide, you can import the tags from front-end-repo to back-end-repo with:

```$ git fetch --tags front-end-remote```

In our case, we only had one tag in front-end-repo, v0.1, which collided with v0.1 in back-end-repo, so I created the new tag manually:

```bash
$ git co <SHA1_FOR_COMMIT>
$ git tag -a v0.1-client -m "v0.1 release from original front-end repo"
```

Finally, push any tags you’ve imported or created to origin.

```bash
$ git push origin master
$ git push --tags origin
```

Clean up: delete the front-end-remote, front-end-master branch, and front-end-repo so you won’t be tempted to use it (unless you still have branches that need to be merged).

```bash
$ git remote rm front-end-remote
$ git br -d front-end-master
$ cd ..
$ rm -rf front-end-repo
```

Anyone who pulls from back-end-repo won’t automatically get the submodule locally, so if they want it they’ll need to do:

```bash
$ git submodule init
$ git submodule update
```

Feel free to rename back-end-repo to something more appropriate like repo on your git server. This doesn’t involve git commands, just rename front-end-repo.git.
Jenkins

After the merge, our back-end jenkins build was failing because it saw the submodule and was trying to update it but couldn’t (it was related to needing different ssh keys for different github repos). Since the back-end build has no need of anything in client/, we disabled this feature in the jenkins settings until we sorted the issue out.

Eventually we moved our repos to our own internal git server, which solved the problem. In the meantime, to change the setting, we checked the box:

Source Code Management -> Repository Browser -> Disable submodules processing

If you’re using a build tool like jenkins, you should be aware that you might need to configure its git submodule settings.
Merging old unmerged feature branches from front-end-repo

If there is outstanding unmerged work in feature branches in front-end-repo, merging these into the back-end-repo is a hassle, because we’re moving all the front-end stuff into client/ and git isn’t smart enough to figure out that any edits you did to e.g. apps/trader/MyClass.js should apply to client/apps/MyClass.js. So we’d be resolving a lot of merge conflicts.
Tracking revision history of individual files that have been moved

We’ve moved all the files from front-end-repo into client/, so if you view the revision history of a single file using git log -- filename (maybe I’m weird but I do this all the time) you will only see changes dating back to the point in time when you moved it (e.g. when we merged repos).

You can try your luck with git log --follow -- filename, but my experiences with it have been hit and miss. Sometimes it shows me the entire history including the move, sometimes not. I haven’t investigated yet why it doesn’t always work. If you know, please comment!

In any case, when we merged repos, the front-end-repo had fewer files, so the effect of this problem was minimized. You can always ask git for the revision history of the old file location, before it was moved.

Show all changes to this file after it was moved into client/

```$ git log -p -- client/apps/trader/index.html```

Show all changes to this file before it was moved

```$ git log -p -- apps/trader/index.html```

Git blame appears to work well with moved files, showing commits before and after the move.
