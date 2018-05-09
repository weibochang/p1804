#coding:utf-8
a =int(input('你要输入的数字'))

if a%4 ==0 and a%100 != 0:
    print('闰年')
elif a%400 == 0:
    print('润年')
else:
    print('平年')
