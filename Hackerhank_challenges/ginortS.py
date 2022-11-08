s = sorted(input())
lower, upper, even, odd = '', '', '', ''

for i in s:
    if i.islower():
        lower = lower + i

    elif i.isupper():
        upper = upper + i

    elif int(i) % 2 != 0:
        odd = odd + i

    elif int(i) % 2 == 0:
        even = even + i

print(lower + upper + odd + even)
