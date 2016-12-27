#!/bin/bash

newDate="$1"

echo "$newDate" > date.log
git add .
git commit -m "Commit for $newDate"
lastCommitHash=$(git log --format="%H" -n 1)
./change-git-commit-date.sh -f "$lastCommitHash" master "$newDate"