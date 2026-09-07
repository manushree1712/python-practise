
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