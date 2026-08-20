# 17 august 2026

#implicit type conversion

a = 10
b = 44
print(a+b)  # int + int = int

c = 12
d = 3.4
print(c+d) # int + float = float

e = 8
f = 9 + 7j
print(e+f) # int + complex = complex
print(type(e))
print(type(f))



#explicit type conversion

a = 44
print(type(a))
a = float(a)
print(type(a))


b = 56.7
print(type(b))
b = int(b)
print(type(b))


c = 77.8
print(type(c))
c = complex(c)
print(type(c))

# d = "python"
# print(type(d))
# d = int(d)
# print(type(d)) #error



