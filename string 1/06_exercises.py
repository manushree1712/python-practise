
# Given a string of even length, return the first half.
# So the string "WooHoo" yields "Woo".


# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'

def first_half(str):
    return str[:len(str)//2]   #len ---- length

print(first_half("food"))




# Given a string, return a version without the first
# and last char, so "Hello" yields "ell". The string length will 
# be at least 2.


# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'

def between(str):
    return str[1:-1]

print(between("exercise"))




# Given 2 strings, a and b, return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty (length 0).


# combo_string('Hello', 'hi') → 'hiHellohi'
# combo_string('hi', 'Hello') → 'hiHellohi'
# combo_string('aaa', 'b') → 'baaab'

a = str(input("enter a word:"))
b = str(input("enter another word:"))

if len(a) > len(b):
    print(b+a+b)
else:
    print(a+b+a)