# check if N number is Perfect or not

def check(N):
    sums = 0
    for idx in range(1, N):
        if N % idx == 0:
            sums += 1
    if sums == N:
        return "Perfect"
    else:
        return "Not perfect"        
  