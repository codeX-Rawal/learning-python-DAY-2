a = 31
t = type(a) # class <int>

print(t)

b = "rawal"
t = type(b)  # class <str>

print(b)

a = "31.5"
b = float(a) # a but the type should be float
t = type(b)

print(t)

# str(31)   =>  #"31"  #integer to string conversion
# int("32")  => #string to integer conversion
# float(32)  => #integer to float conversion