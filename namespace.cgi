#!/bin/bash

echo "Content-Type: text/html"
echo ""

SEP="/"

# 默认 ROOT
if [[ "$GITROOT" == "" ]]; then
	GITROOT=/home/git/gitroot
fi
cd $GITROOT

# 容纳所有
HEADS=()

# repo / namespace / head
for RNH in */refs/namespaces/*/refs/heads/*
do
	#echo ${#HEADS[@]}
	HEADS[${#HEADS[@]}]=$RNH
done

# repo / packed-refs
for RP in */packed-refs
do
	# namespace / head
	NHS=`cat $RP | awk '{print $2}' | grep namespaces`
	#echo $NHS
	for NH in $NHS
	do
		#echo ${RP%%$SEP*}/$NH
		#echo ${#HEADS[@]}
		HEADS[${#HEADS[@]}]=${RP%%$SEP*}/$NH
	done
done

# 上一次NS
LASTNS=

for RNH in `echo ${HEADS[@]} | sed -e 's/ /\n/g' | sort | uniq`
do
	# 物理库
	REPO="${RNH%%$SEP*}"

	# 逻辑库名
	NS=`echo $RNH | awk -F/ '{print $4}'`

	# URL访问库名(不含点)
	REPONAME="${RNH%%.*}"

	#echo $REPO --- $REPONAME --- $NS
	if [[ "$LASTNS" != "$NS" ]]; then
		if [[ "$LASTNS" != "" ]]; then
			echo "<br/>"
		fi
		echo "ns/$REPONAME/$NS"
		LASTNS=$NS
	fi

	# 分支名称
	HEADNAME="${RNH##*$SEP}"

	# 分支路径
	HEADPATH="${RNH#*$SEP}"

	#echo $HEADNAME --- $HEADPATH
	echo "<a href='./?p=$REPO;a=shortlog;h=$HEADPATH'>$HEADNAME</a>"
done

