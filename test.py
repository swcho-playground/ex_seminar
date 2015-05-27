__author__ = 'swcho'

list1 = ['physics', 'chemis@try', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[0:5]

str_type = 'test'
print type(str_type)
type_of_test = type('test')

for item in list1:
    # print item, type(item)
    if isinstance(item, str) and '@' in item:
        print item