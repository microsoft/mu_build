# MuBuild

This is the entrypoint into the CI / Pull Request build and test infrastructure. 

## Getting MuBuild

Your Project Mu repo will most likely need the _mu_build_ repo for Project Mu build tools, Edk2 build tools, scripts, and other critical foundational assets.

Since MuBuild is targeted for use on **Shared** repo Projects, the requirement is to use the _*.mu.yaml_ config file to describe the _mu_build_ repo dependency.  This allows the repo to describe its needs for CI but not interfere with submodule usage when the repo is consumed by another project. 


For any new clone of your repo you will want to bootstrap the repo. 
```cmd
mu_bootstrap -c mu_yaml_config_file
```

More information on the bootstrap process see (TODO!!)

## Usage

General usage is run from workspace root as follows 
``` cmd
MU_BUILD\UefiBuild\MuBuild\MuBuild.py -c Ci.mu.yaml
```

MuBuild.py has a few other prameters. Keep reading for more details. 
* To show detailed help use `-h`
* To limit the MuBuild processing to certain packages use `-p <package 1> <package 2>`
* When a dependency doesn't match just ignore issue and build with whatever is there `--ignore-git`
* When a dependency doesn't match delete repo and clone again. This can be distructive.  This will also fetch and update submodules. `--force-git`
* To update from the server all dependencies use.  This will not do distructive operation.  `--update-git`

In a __local developer__ workflow where the dependencies may be intentionally modifed it is common to use `--ignore-git`. 

In a __ci server__ workflow where the dependencies should be clean up and updated it is common to use `--force-git` and `--update-git`


## Using Git for Dependencies

MuBuild leverages a yaml config file that contains the dependency information.  MuBuild will clone the repositories and set the commit as described in the config file.  Since there are times the dependencies already exist in your workspace and/or in developer workflows these dependencies will not match the required versions defined in the config file and MuBuild provides some flexibilty.  

![MuBuild Dependency Sync Process](Git_Repo_Clone_Checkout_Process_mu.PNG)


## Copyright

Copyright (c) 2018 Microsoft Corporation

All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.