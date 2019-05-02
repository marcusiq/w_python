print "Python review Part 4 - Calculations and Math Functions"

# import the math module as follows.
import math

# Get help on the math module by uncommenting this statement.
# help(math)

message1 = """\n1. Find the absolute value of  the floating point number -2.34 using a method from the math module.
You must not use the __builtin__ method abs(), but a similar math module method starting with f.
"""
print message1
x = -2.34
# Add your code for exercise 1 here. Be sure to print out the results.
x = math.fabs(x)
print x


message2 = """\n2. A right triangle has legs a = 5.0, b = 12.0
Find the hypotenuse c using the sqrt() method from the math module.
"""
print message2
a = 5.0
b = 12.0
# Add your code for exercise 2 here. Be sure to print out the results.
hyp = math.sqrt(a**2 + b**2)
print hyp

message3 = """\n\n3. Find the angle B opposite the longer side b using the relation:
sin(B) = b/c
"""
print message3
# Add your code for exercise 3 here. Use the asin() function, which by definition returns radians.
angleb = math.asin(b/hyp)
print angleb


message4 = """\n\n4. Express the angle B in degrees using math.degrees()
"""
print message4

# Add your code for exercise 4 here.
B = math.degrees(angleb)
print B

message5 = """\n\n5. Express 1000 (base 10) in base 2 using the built-in bin() command. (bin, short for binary).
"""
print message5
# Add your code for exercise 5 here.
x = bin(1000)
print x[2:]


message6 = """\n\n6a. Convert the binary number n2 = '10100100010000100000' back to base 10 using the built-in int() command
with an optional second argument to specify the base.
"""
print message6
n2 = "10100100010000100000"
# Add your code for exercise 6a here.
n3 = int(n2,2)
print n3

print "b. Check you work by converting back to base 2 using bin()."
# Add your code for exercise 6b here.
n4 = bin(n3)
print n4[2:]

# * * * EXERCISE 7 * * *

message7a = """\n\n7a. Using math.log() with two arguments, find the log of 10,000,000 in base 1000. (one thousand)
"""
print message7a
# Add your code for exercise 7a here. Be sure to print out the answer using a complete sentence.
t = math.log(10000000,1000)
print t

message7b = """\n\n7b. Using math.pow() find  1000 to the seven thirds power. Beware of the integer division!
"""
print message7b
# Add your code for exercise 7b here. Be sure to print out the answer using a complete sentence.
t = float(7/3.0)
y = math.pow(1000,t)
print y

x = 1000
for n in range:
    binary_string = bin(n)[2:]
    reverse_string = binary_string[::-1]
    if binary_string == reverse_string:
        b +=1
        print b


