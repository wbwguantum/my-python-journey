n = int(input())
for _ in range(n):    
    n1, a1 = map(int, input().split())    
    count = 1        
    for i in range(n1):        
        count *= (i + 1)

    count = str(count)    
    times = 0    
    a1 = str(a1)        
    for i in range(len(count)):        
        dp = count[i]        
        if dp == a1:            
            times += 1    
    print(times)