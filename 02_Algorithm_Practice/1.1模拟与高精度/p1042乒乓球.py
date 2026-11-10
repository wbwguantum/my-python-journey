import sys
input_data = "".join(sys.stdin.read().split())
if 'E' in input_data:
    input_data = input_data[:input_data.index('E')]
def play(target):
    w = 0
    l = 0
    for char in input_data:
        if char == 'W':            
            w += 1        
        elif char == 'L':            
            l += 1
        if (w >= target or l >= target) and abs(w - l) >= 2:            
            print(f"{w}:{l}")            
            w = 0       
            l = 0
    print(f"{w}:{l}")
play(11)
print()
play(21)