#!/bin/python
#coding:utf-8
#author: ourfor
#date: 20181212 11:31
#description: 练习函数和递归

def Recur(n):
    if n==0:
        return 1
    else:
        return n*Recur(n-1)

print("输入一个整数，求出这个数的阶乘")
n=input("n=")
print(str(Recur(n)))


