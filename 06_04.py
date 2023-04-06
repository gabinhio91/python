# list1 = [i**2 for i in range(10)]
# print(list1)

# list3 = [i**2 for i in range(10) if i > 5]
# print(list3)


# set1 = {a**2 for a in range(10)}
# print(set1)

# dict1 = {i:i*i for i in range(10)}
# print(dict1)

# x=int(input())
# def funct(x):
#     x=x+3
#     return(x)

# print(funct(x))


# var1 = lambda x,y,z: x+y+z
# print(type(var1))

# print(var1(1,2,3))

# def concat(list1):
#     list2= []
#     for i in range (5):
#         for j in range (5):
#             list2.append(i*j)
#     return list1+list2

# list1=['a','b','c']
# print(concat(["aici","am","prima","lista"]))
# print("SAAAUUUUUU")
# print(concat(list1))


x = lambda lista: [i+j for i in range(5) for j in range(5)] +lista
print(type(x))
lista_finala=x(["incepem",'lista: '])
print(lista_finala)




