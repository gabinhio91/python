# class Persoana:
#     # nume = ''
#     # varsta = 0
#     def __init__(self, nume, varsta):
#         self.nume = nume
#         self.varsta = varsta
        
#     def persoana_afisare(self):
#         print (f'obiectul se numeste {self.nume} si are {self.varsta}')
#     def __str__(self):
#         return (f'obiectul se numeste {self.nume} si are {self.varsta}')
        
        
# gigel = Persoana('gigel sonescu', 30)
# # gigel.nume = 'gigel sonescu'
# # gigel.varsta = 30

# gigel.persoana_afisare()
# print(gigel)



# 1.clasa data calendaristica
#-constructor
#-functie de afisare
#-functie care afiseaza ziua de dupa obiect

class Calendar:
    list1 = ['Ianuarie', 'Februarie', 'Martie', 'Aprilie', 'Mai', 'Iunie', 'Iulie',' August', 'Septembrie',' Octombrie',' Noiembrie',' Decembrie']
    #            0           1           2          3        4        5       6       7             8           9           10             11
    def __init__(self, zi, luna, an):
        self.list1 = ['Ianuarie', 'Februarie', 'Martie', 'Aprilie', 'Mai', 'Iunie', 'Iulie',' August', 'Septembrie',' Octombrie',' Noiembrie',' Decembrie']
        self.zi = zi
        self.luna = luna
        self.an = an
    def __str__(self):
        return(f'ziua {self.zi} in luna {self.luna}, anul {self.an}')
    def ziua_urm(self):
        if self.zi == 31 and self.luna == self.list1[11]:
            self.an +=1
            self.zi = 1
            self.luna = self.list1[0]
        else:
            for i in range (len(self.list1)):
                if i % 2 == 0 and i <=6  and self.zi == 31:
                    self.luna = self.list1[i+1]
                    self.zi = 1
                elif i%2 !=0 and i <= 6 and self.zi == 30:
                    self.luna = self.list1[i+1]
                    self.zi = 1
                elif i % 2 != 0 and i >6  and self.zi == 31:
                    self.luna = self.list1[i+1]
                    self.zi = 1
                    print(i)
                elif i%2 ==0 and i > 6 and self.zi == 30:
                    self.luna = self.list1[i+1]
                    self.zi = 1
        print(f'ziua {self.zi} in luna {self.luna}, anul {self.an}')
                
Craciun = Calendar(31, 'Octombrie' , 2023)
print(Craciun)
Craciun.ziua_urm()

