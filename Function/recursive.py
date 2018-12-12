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

def BubbleSort(array):
    for i in range(len(array),1,-1):
        for j in range(0,i):
            if array[j]>array[j+1]:
                tmp=array[j]
                array[j]=array[j+1]
                array[j+1]=tmp
    return array

print("输入一个整数，求出这个数的阶乘")
n=input("n=")
array=[2,3,1,33,11,332]

print(str(Recur(n)))

for i in range(0,len(array)):
    print(str(array[i]))
