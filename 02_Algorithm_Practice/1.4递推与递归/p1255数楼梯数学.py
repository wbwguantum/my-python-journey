import math
n = int(input())
ans = 0
for two_steps in range(n // 2 + 1):    
    one_steps = n - (2 * two_steps)    
    total_steps = two_steps + one_steps
    ways = math.comb(total_steps, two_steps)    
    ans += ways
print(ans)

#math.comb(n, k) is a function that returns the number of ways to choose k items from n items without regard to the order of selection. It is equivalent to the binomial coefficient C(n, k) = n! / (k! * (n - k)!).