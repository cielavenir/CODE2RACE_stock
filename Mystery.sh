#!/bin/sh
#coding:utf-8
#author:cielavenir (https://github.com/cielavenir)

read t
for i in `seq $t`; do
  read n
  <<<$n factor | tr \  '\n' | uniq -c | sed 1d | awk 'BEGIN{n=1}{n*=$1+1}END{print n}'
done
