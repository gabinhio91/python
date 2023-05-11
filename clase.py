# dimensiune = int(input("Dimensiunea este: "))
# i=0; s=0;
# while i<dimesnsiune:
#     var = int(input('introdu un numar'))
#     s=s+var
#     i+=1
# s=s/dimesnsiune
# print(s)
# j=1
# s=0
# list1 =[]
# while j<=dimensiune:
#     list1.append(int(input('introdu un numar')))
#     j+=1
# for i in list1:
#     print(i)
#     s= s + i
# s=s/dimensiune
# print (s)





### CLASE

# class Masina:
#     an =0
#     marca = ""
#     def afisare(self):
#         print(f"masina mea este {self.marca} din anul {self.an}")



# masina_mea = Masina()
# masina_mea.an = 2000
# masina_mea.marca = "BMW"

# # print ('Am o masina ',masina_mea.marca, "din ",masina_mea.an)
# print(f"Am o masina {masina_mea.marca} din {masina_mea.an}")


# masina_mea.afisare()

# class Dreptunghi():
#     lungime =0
#     latime = 0
#     def 
#     def arie_return(self):
#         return(self.lungime * self.latime)
#     def arie_print(self):
#         print(self.lungime * self.latime)
# tablou = Dreptunghi()
# tablou.latime = 20
# tablou.lungime = 30
# tablou.arie_print()

# print(tablou.arie_return())

###constructorii
# def  __init__(self,lungime,latime):
#     self.lungime =lungime
#     self.latime = latime

# class Dreptunghi:
#     def  __init__(self,lungime,latime):
#         self.lungime =lungime
#         self.latime = latime
#     def arie_return(self):
#         return(self.lungime * self.latime)
#     def arie_print(self):
#         print(self.lungime * self.latime)

# tablou = Dreptunghi(lungime = 25, latime = 20)
# tablou.arie_print()


class Persoana:
    def __init__(self,nume,prenume,varsta):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta 
    def afisare(self):
        print(self.nume , self.prenume , self.varsta)
marius = Persoana(nume = 'Marius', prenume = 'Daniel', varsta = 77)
marius.afisare()

def verif(varsta,nume,prenume):
    if (varsta >= 18):
        print(nume, prenume, "este major")
    else:
        print(nume, prenume, "este minor")
verif(marius.varsta, marius.nume, marius.prenume)
