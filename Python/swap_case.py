S = raw_input()
A = list(S)
a = []

for x in A:
    if ord(x)>=65 and ord(x)<=90:
        B = x.lower()
        a.append(B)
    elif ord(x)>=90 and ord(x)<=122:
        B = x.upper()
        a.append(B)
    else:
        a.append(x)

out = "".join(a)
print out
