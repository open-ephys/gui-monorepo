# Open Ephys GUI - Monorepo

Experimental repo that automatically builds the host application and plugins together. This should be useful for testing the core GUI and external plugins in one place.

Thanks to [@admunkucsd](https://github.com/admunkucsd) for the inspiration and instructions!

## Recommended workflow

1. Clone this repository locally.

2. Launch Visual Studio Code with the following extensions installed:
- C/C++
- CMake Tools
- C++ TestMate

3. Open the `gui-monorepo` directory

4. Select the "All Open Ephys Components" configuration preset for your platform.

5. Select "install" as the default build target.

6. Run "Build"

Now, you should be able to run and debug the GUI, and run and debug all tests from within Visual Studio Code.

## Working with submodules

To add an additional plugin as a submodule, navigate to the top-level directory (`gui-monorepo`) and run:

```bash
git submodule add <repository_URL>
```

Running `git status` after adding the submodule will show that the module is stored as a commit hash. This will influence all interactions with this submodule through the perspective of the monorepo: *you are not interacting with the submodule repo directly, but rather the submodule in a discrete state, i.e. at a particular commit in a detached HEAD state.*

### Pulling changes

Running `git pull` will update the submodule hashes the monorepo *should* use, but will not actually update the submodules directory. After running `git pull` to update the base repo, run the following to update the submodules:

(for the first time): `git submodule update --init --recursive`
(subsequent pulls): `git submodule update --recursive`

### Pushing to remote

**IMPORTANT**: Git does not automatically push submodule changes when pushing from the top-level repo. As such, other users that pull this remote branch may not be able to pull the correct submodule hashes from their respective remotes. To fix this, add the following git config flag:

```bash
git config push.recurseSubmodules on-demand
```

This will change `git push` to recursively push all submodules to remote.

### Deleting submodules

Submodules leave git artifacts beyond the reference hash. To fully remove a submodule, follow these instructions:

1. Delete the relevant section from the .gitmodules file
2. Stage the .gitmodules changes: `git add .gitmodules`
3. Delete the relevant section from `.git/config`
4. Run `git rm --cached path_to_submodule` (no trailing slash)
5. Run `rm -rf .git/modules/path_to_submodule` (no trailing slash)
6. Commit using `git commit -m "Removed submodule"`
7. Delete the now-untracked submodule files: `rm -rf <path_to_submodule>`




