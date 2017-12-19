#!/usr/bin/env python
# Author: Eric Greenfeder
# Date: 12/18/2017
# Version: 1.0
# Purpose: This python script is used by the CI pipeline process to create project specific container.yml file for Ansible Container using a microservices projvars.yml file. The Jinja2 python template framework is used for conditional variable substitution.
import os
import jinja2
import yaml
import sys
import shutil

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)

def checkCmdArgs():
  printUsage = False
  if len(sys.argv) < 3:
    printUsage = True

  if printUsage or sys.argv[1] != '-d':
    print('Usage: setupProject.py -d <path to project directory>')
    sys.exit()

def checkEnvVars():
  if not "DKTEMP_HOME" in os.environ:
    print('The DKTEMP_HOME environment variable is not set!')
    sys.exit()

def createContainerYamlFile():
  with open (PROJECT_DIR+"/deploy/projvars.yml", "r") as myfile:
    context =  yaml.safe_load(myfile)
  result = render(DKTEMP_HOME+'/container.yml.template',context)
  with open(PROJECT_DIR+'/deploy/container.yml', "w") as yaml_file:
    yaml_file.write(result.replace('\\n',os.linesep))

def copyRequirementsYamlFile():
  shutil.copyfile(DKTEMP_HOME+"/requirements.yml.template",PROJECT_DIR+"/deploy/requirements.yml");




# Setup variables
PROJECT_DIR = sys.argv[2]
DKTEMP_HOME = os.environ.get("DKTEMP_HOME");

if not PROJECT_DIR:
      print('Usage: setupProject.py -d <path to project directory>')

# Start execution
checkEnvVars()
checkCmdArgs()
createContainerYamlFile()
copyRequirementsYamlFile()

