import math

t = int(input())
for _ in range(t):
    n, a = map(int, input().split())

    fact = math.factorial(n)
    fact_str = str(fact)
    target = str(a)

    ans = fact_str.count(target)
    print(ans)

#math.factorial() is a built-in function in Python that calculates the factorial of a given number. It is part of the math module, which provides various mathematical functions and constants. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n, denoted as n!. For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.
#target_str.count(target) is a string method in Python that counts the number of occurrences of a specified substring (target) within the string (fact_str). It returns an integer representing the count of non-overlapping occurrences of the substring. In this case, it counts how many times the digit 'a' appears in the string representation of n!.