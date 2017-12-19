#!/bin/bash
# Author: Eric Greenfeder
# Date: 12/18/2017
# Version 1.0
# Description: This shell script represents the main CI pipeline build process

# Load environment variables
. ./setenv.sh

# Get the latest docker templates files from Git
./getLatestDockerTemplates.py

# Setup microservice project directory
./setupProjectDirectory.py
