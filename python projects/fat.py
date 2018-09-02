def fat(n):
    print(n)
    return 1 if (n < 1) else n * fat(n-1)

x = fat(5)
print(x)
