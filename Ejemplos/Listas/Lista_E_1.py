palabra = "electroencefalografista"
a = e = i = o = u = 0
for i in palabra:
    if "a" in palabra:
        a += 1
    elif "e" in palabra:
        e += 1
    elif "i" in palabra:
        i += 1
    elif "o" in palabra:
        o += 1
    elif "u" in palabra:
        u += 1

print(a)
print(e)
print(i)
print(o)
print(u)
