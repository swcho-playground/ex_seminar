
file_test = open('sample.txt', 'rt')

print type(file_test)
print file_test

# first_line = file_test.readline()
# second_line = file_test.readline()
#
# print first_line
# print second_line

lines = file_test.readlines()

#print type(lines)
#print lines

print type(lines)

range_1 = range(100, 105)
print type(range_1)
print range_1

for number in range_1:
    print number

for line in lines:
    print line