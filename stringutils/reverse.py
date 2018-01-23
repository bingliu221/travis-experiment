def reverse(text):
    l1 = list(text)

    l2 = list(text)
    for i, c in enumerate(l1):
        print(c)
        l2[len(l2) - i - 1] = c
    return ''.join(l2)
