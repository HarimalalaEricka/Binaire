#Definition de la fontion binaire
def binaire(x) :
    bin = 0
    i = 0
    while x != 0 :
        temp = 2 ** i
        while temp <= x :
            i += 1
            temp = 2 ** i
        bin += 10 ** (i - 1)
        x -= 2 ** (i - 1)
        i = 0
    return "0b" + str(bin)

#Utilissation de la fonction
nb = 2796202
bin = binaire( x = nb)
print(bin)