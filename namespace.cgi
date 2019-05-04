#!/bin/bash

echo "Content-Type: text/plain"
echo ""

GITROOT=/home/git/gitroot
cd $GITROOT

for ns in */refs/namespaces/*
do
	echo $ns
done

