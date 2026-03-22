#!/bin/bash

branch=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
docrootlocal="Export/$branch/latex/"
startdir=$(pwd)

cd $docrootlocal && lualatex *.tex; cd $startdir