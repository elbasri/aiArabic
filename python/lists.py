point = [1, -3, 2]
print(point)

point2 = [-3, 1, 2]
print(point2)

ncrList = [21.42, 'hello', 3, 4, 'salam alaykom', False, 3.14150]
print(ncrList)
print(ncrList[4])
print(ncrList[1:3])

points = [point, point2]
print(points[1])
print(points[1][0])

#tuples
days = ('Itnin', 'tolata', 'jomo3a')
print(days)
print(days[1])

print(len(days))

print(points.count(points[0]))

numbers = [12, 33, 8, 4]
numbers.append(7)
print(numbers)
new_numbers = [15, 45 , 78 , 1]
numbers.extend(new_numbers)
print(numbers)

numbers[0] = 99
numbers.remove(78)
print(numbers)
del numbers[-1]
print(numbers)
print(numbers.pop())


numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.clear()
print(numbers)