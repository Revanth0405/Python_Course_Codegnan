n = 5
for i in range(n):
    for j in range(n):
        if (i==0 and j!=0) or (i==n//2 and j!=0 and j!=n-1) or (i==n-1 and j!=n-1) or (j==0 and i<n//2 and i!=0) or (j==n-1 and i>n//2 and i!=n-1):
            print("*", end='')
        else:
            print(" ", end='')
    print()