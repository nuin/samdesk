import sys

def s_or_u(reactor):
    diff = [reactor[i+1] - reactor[i] for i in range(len(reactor) - 1)]
    if all(1 <= d <= 3 for d in diff):
        return True
    elif all(-3 <= d <= -1 for d in diff):
        return True
    else:
        return False

safe = 0
with open("input.txt") as f:
    for line in f:
        if not line:
             continue
#        print(f"Checking {line.strip()}")
        levels = list(map(int, line.split()))
        if s_or_u(levels):
             safe += 1	        

print(f"Safe: {safe}") 
