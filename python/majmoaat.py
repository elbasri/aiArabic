
mowaddafin_ids = {1,2,3,4,5,6,7}
vowel_letters = {'a', 'e', 'i', 'o', 'u'}

fruitList = set(['tofa7a', 'banana', 'lemon', 'laymon', 'tofa7a'])
print(fruitList)
print(len(fruitList))


fruitList2 = set()
print(type(fruitList2))
fruitList2.add("lemon")
print(mowaddafin_ids|fruitList|fruitList2)
print(fruitList&fruitList2)
fruitList.remove("laymon")
print(fruitList)