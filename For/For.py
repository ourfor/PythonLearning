#!/usr/bin/python
#coding:utf-8
import sys
print("输入一个自然数，我将求它的前n项和")
n=input("N=")
i=1
s=0
while i<=n:
    s+=i
    i+=1
print("1+2+...+"+str(n)+"="+str(s))
