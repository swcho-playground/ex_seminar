__author__ = 'sdlee'

# Variable-length arguments
# def sum( arg1, *tuple ):
#     sum = arg1
#     for i in tuple:
#         sum = sum + i
#     print "Sum of arguments: %s" %(sum)
#     return
#
# sum( 10 )
# sum( 70, 60, 50, 5, 4, 3, 2, 1 )

def extract(arg1):
    #print arg1.keys()
    array = arg1.keys()
    for x in arg1.values():
        if x != None:
            array.append(extract(x))

    return array


tree = {
    '01': {
        '01-01': None,
        '01-02': None,
        '01-03': None,
        '01-04': None,
        '01-05': {
            '01-05-01': None,
            '01-05-02': None,
            '01-05-03': None,
            '01-05-04': None
        }
    }
}
print extract(tree)