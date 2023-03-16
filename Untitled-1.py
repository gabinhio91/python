def intro():
    nume=input("salut, cum te numesti?: ")
    print("ok, ", nume, "o sa ne jucam Spanzuratoarea! ")
    raspuns = input("Are you ready? yes/no: ")
    if raspuns == "yes":
        return True
    else:
         return False

def reguli():
    from time import sleep
    sleep(1)
    print("Regulile sunt urmatoarele:")
    print("1. Trebuie sa ghicesti cuvantul din 6 litere")
    print("2. Ai la dispozitie 6 vieti")
    print("3. Daca termini vietiile vei pierde")

def design_spanzuratoare(vieti):
    if vieti == 0:
        print(" +-----+")
        print(" |     |")
        print(" |     0 ")
        print(" |    /|\ ")
        print(" |    / \ ")
        print("_|_")
    if vieti == 1:
        print(" +-----+")
        print(" |     |")
        print(" |     0")
        print(" |    /|\ ")
        print(" |    /  ")
        print("_|_")
    if vieti == 2:
        print(" +-----+")
        print(" |     |")
        print(" |     0")
        print(" |    /|\ ")
        print(" |")
        print("_|_")
    if vieti == 3:
        print(" +-----+")
        print(" |     |")
        print(" |     0")
        print(" |    /| ")
        print(" | ")
        print("_|_")
    if vieti == 4:
        print(" +-----+")
        print(" |     |")
        print(" |     0")
        print(" |     |")
        print(" |    ")
        print("_|_")
    if vieti == 5:
        print(" +-----+")
        print(" |     |")
        print(" |     0")
        print(" |     ")
        print(" |     ")
        print("_|_")
    if vieti == 6:
        print(" +-----+")
        print(" |     |")
        print(" |     ")
        print(" |     ")
        print(" |    ")
        print("_|_")

def start_joc(litera,cuv, cuv_cautat):
    contor = 0
    global alegere 
    alegere = False 

    for element in cuv:
        if litera == element:
            cuv_cautat[contor] = litera
            alegere = True
        contor+=1
    print(*cuv_cautat)



cuvant = ['d','e', 'b', 'u', 'g']
cuvant_cautat = ['_','_','_','_','_']









if intro() == False:
    print("ok, ne vedem data viitoare")
else:
    reguli()
    vieti = 6
    while vieti != 0:
        litera = input("Alege o litera: ")
        start_joc(litera, cuvant, cuvant_cautat)
        if alegere == False:
            design_spanzuratoare(vieti)
            vieti -=1
        else:
            vieti = vieti +1 - 1
            if cuvant == cuvant_cautat:
                print("Felicitari, ai ghicit!")
                break
    else:
        from time import sleep
        sleep(1)
        print("Ai fost spanzurat")
        design_spanzuratoare(0)













