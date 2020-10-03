#!/usr/bin/python
#coding:utf-8
#author:cielavenir (https://github.com/cielavenir)

try:
	import sympy
	factor=sympy.factorint
except ImportError:
	import nzmath
	factor=nzmath.factor.methods.factor

for _ in range(int(input())):
	r=1
	for (k,v) in factor(int(input())).items():
		r*=v+1
	print(r)
