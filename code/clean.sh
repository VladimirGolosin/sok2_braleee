#!/bin/bash

# This script is used to clean unnecessary generated files/folders.

remove_eggs() {
  # The directory path is sent as the first argument
  cd $1
  rm -rf build
  rm -rf *.egg-info
  rm -rf dist
  cd ..
}

# remove build files from components
remove_eggs Core
remove_eggs TestParser
remove_eggs CSVParser
remove_eggs JSONParser
remove_eggs FilePathParser
remove_eggs VlafaParser
remove_eggs SimpleVisualizer
remove_eggs ComplexVisualizer

# remove db
#cd django_project
#rm *.sqlite3
#cd ..
