#coding: utf-8
#author: ourfor
#date: 20190123
#description: 练习python中的判断语句

print("利用if-else来打赢分段函数的值:")
print("输入1到10之间的任意整数")
num=0
num=input("输入1~10之间的整数:")
num=int(num)

print(type(num))

if num>=1 and num<=4 :
    print("输入的是一个大于等于1小于等于4的整数。")
elif num <=8 :
    print("输入的是一个大于4小于等于8的整数")
else :
    print("输入的是一个大于8小于等于10的整数")
