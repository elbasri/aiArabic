morabba3 = []

for i in range(25):
    morabba3.append(i*i)
print(morabba3)

morabba3Banyat = [i * i for i in range(25)]
print(morabba3Banyat)

morabba3Banyat2 = [i ** 2 for i in range(25)]
print(morabba3Banyat2)

morabba3Banyat3 = {i ** 2 for i in range(25) if i % 2 == 0}
print(morabba3Banyat3)

morabba3BanyatID = {i: i*i for i in range(15)}
print(morabba3BanyatID)

masfofaBanyat = [[i for i in range(10)] for j in range(3)]
print(masfofaBanyat)