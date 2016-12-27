#!/bin/bash

for i in `seq 275 365`; do
	d=$(date --date "-$i day")
	echo "$d" > date.log
	rand=$(shuf -i 0-30 -n 1)
	rand=$((rand-15))

	if [ $rand -lt 0 ]; then
		rand=0
	fi

	echo $rand

	for j in `seq 1 $rand`; do
		echo "$j" > count.log
		git add .
		git commit -m "$d $j"
		lastCommit=$(git log --format="%H" -n 1)
		./change-git-commit-date.sh -f $lastCommit master "$d"
	done

done
