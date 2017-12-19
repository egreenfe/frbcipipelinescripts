#!/usr/bin/env python

# Author: Eric Greenfeder
# Date: 12/18/2017
# Version 1.0
# Purpose: This python script is used by the CI pipeline process to make sure the latest docker Jinja2 template files are pulled from Git

import git 
import os
import sys
import commands

def getLatestDockerTemplateFiles():
    # Check out the docker template repo files from Git
    if not "DKTEMP_HOME" in os.environ:
      print('The DKTEMP_HOME environment variable is not set!')
      sys.exit()

    temp_home = os.environ.get("DKTEMP_HOME");

    if not "DKTEMP_GIT_REPO" in os.environ:
      print('DKTEMP_GIT_REPO environment variable is not set!')
      sys.exit()

    git_repo = os.environ.get("DKTEMP_GIT_REPO");

    # Make sure the docker template home directory has the lastest teamplate files.
    # First make sure the directory exists and if not create it
    if not os.path.exists(temp_home):
      os.makedirs(temp_home)
      os.chdir(temp_home) 
      print(commands.getstatus('/usr/bin/git clone '+git_repo))
    
    repo = git.Repo.init(temp_home)
    if not repo.remotes:
      origin = repo.create_remote('origin',git_repo)
    origin = repo.remotes.origin
    origin.fetch()
    origin.pull(origin.refs[0].remote_head)

    return;

getLatestDockerTemplateFiles()


