# ## 1. Recap functia lambda

# x = lambda i:i+1
# print(x(10))

# x = lambda a,b,c : (a+b+c)/3 
# print(x(4,5,6))


# ## 2. MAP/map

# list1 = [1,2,3,4]
# ##program ca toate elem *10
# list2 = []
# for i in list1:
#     list2.append(i*10)
# print(list2)

# def ori_zece(x):
#     return x*10

# list2 = list(map(ori_zece, list1))
# print(list2)

# list2 = list(map(lambda x: x * 10, list1))
# print(list2)

# ## 3. filter

# def filtrare(x):
#     return x%2 == 0


# list1= [1,2,34,5,4122,5,124,5,213,5,7]
# list2 = []

# list2 = list(filter(filtrare, list1))
# print(list2)


# list2= []
# list2 = list(filter(filtrare, list1))
# print(list2)

# lista_mea = list(range(-10, 10))
# print(lista_mea)


# mai_mici_ca_10 = list(filter(lambda x: x<10, lista_mea))
# print(mai_mici_ca_10)

list1 = []
for i in range (1,51):
    list1.append(i)

# x= None
# ok = None


# def prim(x):
#     for i in x:
#         ok = 1
#         if i == 1:
#             ok = 0 
#             break
#         else:
#             for j in range (2,i):
#                 if i%j == 0:
#                     ok = 0
#         if ok == 1:
#             return True



# def prim(x):
#     if x == 1 or x == 0:
#             return False
#     for i in range (2,x):
#         if x%i == 0 :
#             return False  
#     return True


# listp = list(filter(prim, list1))
# print(listp)

### 4. Reduce

from functools import reduce 

# list1 = [24,25,1,0,9]
# def suma(x):
#     sum = 0
#     for i in x:
#         sum = sum + i
#     return sum

# print(suma(list1))

# print(reduce(lambda a,b : a+b, list1))

# print(reduce(lambda a,b : a + ' ' + b, 'python'))
