n = 10
for num in range(n):
    if num in (0,1):
        print(num)
    else:
        print(num-1 + num-2)
