#!/bin/zsh

echo "-----1: ----$1"
if [ $1 ]; then
    subdir=$1
else
    subdir=.
fi
# echo "-----subdir: ----$subdir"

while true; do
    clear
    make pytest_all
    #make pytest_system
    # make pytest
    # use this to stop at first failure:
    # pytest -x -vv $subdir
    fswatch ./**/*.py  -1
done
