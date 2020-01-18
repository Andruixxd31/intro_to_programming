par = 0
inpar = 0
cero = 0
for x in range(10):
    num = int(input(">>"))
    if num == 0:
        cero += 1
    elif num % 2 == 0:
        par += 1
    else:
        inpar +=1

print(par)
print(inpar)
print(cero)