#!/usr/bin/python

# Function definition is here
def changeme( arg1 ):
   "This changes a passed list into this function"
   arg1 = arg1.upper()
   print "Values inside the function: ", arg1
   return arg1

arg1 = '1'
arg2 = '2'

# Now you can call changeme function
global_variable = "hi"
global_variable = changeme( global_variable )
print "Values outside the function: ", global_variable

# Function definition is here
def printme( str01 ):
   "This prints a passed string into this function"
   print str01;
   return;

# Now you can call printme function
printme(str01='Hi');

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
