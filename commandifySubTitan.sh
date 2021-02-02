#!/bin/bash

# make a sym link from subTitan.sh here to the users's bin so that `subTitan` can be used anywhere on oscar

mkdir -p ~/bin

currPath=$PWD

cd ~/bin
ln -s -f $currPath/subTitan.sh subTitan

cd $currPath

echo "Success! `subTitan` command now aviable anywhere on OSCAR"
