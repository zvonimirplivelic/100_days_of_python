# Goal of this excercise is to switch data stored in variables
# a and b through third variable

a = input()
b = input()

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)