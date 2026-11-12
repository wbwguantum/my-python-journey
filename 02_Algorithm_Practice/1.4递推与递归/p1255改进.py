import sys
sys.set_int_max_str_digits(0)

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    a = 1
    b = 2
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    print(b)

#sys.set_int_max_str_digits(0) is a function that sets the maximum number of digits allowed in an integer string representation. Setting it to 0 means there is no limit on the number of digits, allowing for very large integers to be handled without raising an error.
#recursiveely pushed
