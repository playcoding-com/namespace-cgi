#!/bin/bash

echo "Content-Type: text/html"
echo ""

SEP="/"

# 默认 ROOT
if [[ "$GITROOT" == "" ]]; then
	GITROOT=/home/git/gitroot
fi
cd $GITROOT

# 枚举 namespace
for REPONS in */refs/namespaces/*
do
	# 库
	REPO="${REPONS%%$SEP*}"
	NS="${REPONS##*$SEP}"
	REPONAME="${REPONS%%.*}"

	#echo "$REPO"
	#echo "$NS"
	#echo $REPONAME
	echo "ns/$REPONAME/$NS"

	# heads
	for HEADS in $REPONS/refs/heads/*
	do
		#echo $HEADS
		HEADNAME="${HEADS##*$SEP}"
		HEADPATH="${HEADS#*$SEP}"
		#echo $HEADNAME
		#echo $HEADPATH
		echo "<a href='./?p=$REPO;a=shortlog;h=$HEADPATH'>$HEADNAME</a>"
	done

	echo "<br>"
done

