#!/usr/bin/env python

# Author: Eric Greenfeder
# Date: 12/18/2017
# Version 1.0
# Purpose: Build the application if it requires compiling and place the deployment artifacts (ex. JAR) in the deploy directory in the proper place.

import git 
import os
import sys
import commands
import subprocess
import fnmatch
import shutil
import glob

def buildJavaApplication():
  if not os.path.exists(PROJECT_HOME+"/pom.xml"):
    print("Could not find a pom.xml file exists in the root folder of this Java project")
    sys.exit(1)

  os.chdir(PROJECT_HOME)
  args = ['mvn', 'package']
  process = subprocess.Popen(args, stderr=subprocess.PIPE)
  out, err = process.communicate()
  if err:
    print("Build failed: "+err)
    sys.exit(1)
  else:
    print(out)
  for filename in glob.glob(os.path.join(PROJECT_HOME+"/target", '*.jar')):
    shutil.copy(filename, PROJECT_HOME+"/deploy/jar/app.jar")

def buildNodeJSApplication():
  print("Building Nodejs Application")

def recursive_glob(rootdir='.', pattern='*'):
	matches = []
	for root, dirnames, filenames in os.walk(rootdir):
	  for filename in fnmatch.filter(filenames, pattern):
		  matches.append(os.path.join(root, filename))

	return matches

def isJavaProject():
  flist = recursive_glob(PROJECT_HOME,"*.java")   
  if flist:  
    return True
  else:
    return False

# Setup variables
if (len(sys.argv) < 2) or (sys.argv[1] != "-p"):
   print("Usage: buildApplication.py -p <project home path>")
   sys.exit(1)

PROJECT_HOME = sys.argv[2];
if not os.path.exists(PROJECT_HOME):
  print("The project home path does not exist: "+PROJECT_HOME)
  sys.exit(1)

if isJavaProject():
  buildJavaApplication()
else:
  buildNodeJSApplication()

