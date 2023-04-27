import random
puncte_om = 0
puncte_pc= 0
optiuni = ("piatra","foarfeca","hartie")
rulare_joc = True 
print("_____________________________________________")
while rulare_joc:
    pc = random.choice(optiuni)
    om = input("alegerea ta: ")
    if om in optiuni:
        print("alegerea calculatorului: ",pc)
        if pc == om:
            print ("egal")
        elif pc == "piatra" and om == "foarfeca":
            puncte_pc +=1
        elif pc == "hartie" and om == "piatra":
            puncte_pc +=1
        elif pc == "foarfeca" and om == "hartie":
            puncte_pc +=1
        else:
            puncte_om +=1
        print("\n")
        print("punctele tale = ", puncte_om)
        print("puntctele calculatorului = ", puncte_pc)
        print("_____________________________________________")
    else:
        print("alege dintre piatra, foarfeca si hartie!!")
        print("_____________________________________________\n")
    if puncte_om == 3 or puncte_pc == 3:
        rulare_joc = False 

    
    
if puncte_om > puncte_pc:
    print("Bravo, ai castigat!")
else:
    print("Din pacate, ai pierdut")

