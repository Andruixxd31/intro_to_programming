squares = [x**2 for x in range(10)]
print(squares)

listcomp = [(x, y) for x in [1,2,3] for y in [3,1,4] if x == y]
print(listcomp)

vec = [-4, -2, 0, 2, 4]
[abs(x) for x in vec]
print(vec)

vec = [[1,2,3], [4,5,6], [7,8,9]]
listcomp = [num for elem in vec for num in elem]
print(listcomp)
