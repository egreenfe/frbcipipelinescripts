#!/usr/bin/env python

# Author: Eric Greenfeder
# Date: 12/18/2017
# Version 1.0
# Purpose: Setup the microservice project directory and Git pull the latest files

import git 
import os
import sys
import commands
import subprocess

def getLatestProjectFiles(projHomePath,projGitRepoURL):

    if not os.path.exists(projHomePath):
      os.makedirs(projHomePath);
    
    repo = git.Repo.init(projHomePath)
    if not repo.remotes:
      origin = repo.create_remote('origin',projGitRepoURL)
    origin = repo.remotes.origin
    origin.fetch()
    origin.pull(origin.refs[0].remote_head)
    return;

def initAnsibleContainer()
  os.chdir(
  subprocess.call 

# Setup variables
if len(sys.argv) < 4:
   print("Usage: setupProject.py -p <project home path> -r <project Git repo URL>")
   sys.exit(1)



# Get the latest project files from Git
getLatestProjectFiles(sys.argv[1],sys.argv[2])

# Apply the docker templates and create the docker configuration files for this project
subprocess.call(["./applyDockerTemplatesToProject.py","-d",sys.argv[1]])


