
# Given 2 strings, return their concatenation, 
# except omit the first char of each.
# The strings will be at least length 1.


# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'


# a = str(input("enter a word:"))
# b = str(input("enter another word:"))

# def non_start(a,b):
#     return a[1:] + b[1:]
# print(non_start(a,b))



# Given a string, return a version without the first and last char, 
# so "Hello" yields "ell". The string length will be at least 2.


# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'

a = input("enter a word:")

def without_end(a):
    return a[1:-1]


if len(without_end(a)) <= 2:
    print(a)


print(without_end(a))