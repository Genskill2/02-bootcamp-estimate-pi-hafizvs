def wallis(n):
    k = 1
    pi = 1
    numb = input('enter value')
    n = int(numb)
    while True:
        p = 4 * (k ** 2) / (4 * (k ** 2) - 1)
        if k == n:
            break
        pi = pi * p
        k = k + 1
    return 2*pi







