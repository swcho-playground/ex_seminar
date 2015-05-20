# -*- coding: utf-8 -*-
__author__ = 'sungwoo'

tuple1 = (1, 2)
print type(tuple1)

list = [1, 2]

print type(list)
dict = {
    'name': 'sungwoo',
    'age': '20'
}
print type(dict)

x, y = tuple1

print "Start out"
print tuple1
print x
print y
print dict

with open('sample.txt', 'rt') as f:
    data = f.read()
    print data

if False:
    print 'hello 1'
print 'hello 2'