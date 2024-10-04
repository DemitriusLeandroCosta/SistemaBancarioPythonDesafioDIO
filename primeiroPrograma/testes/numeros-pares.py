numeros =[1,2,9,16,32,28,99,68]
pares=[]
pares2=[]

for numero in numeros:
    if numero %2 ==0:
        pares.append(numero)

        print(pares)


pares2 = [numero for numero in numeros if numero %2 == 0]
print()
print(pares2)

    
