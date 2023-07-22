print("Desafio de eliminar los duplicados y ordenar por numeros par e impar")

list = [3,2,5,1,2,4,6,1,3,5,7]
list2 =[]
list2= list [0:1]
pares = []
impares= []

for i in range(len(list)):
    if list [i] not in list2:
        list2.append(list[i])
print("lista de numeros elimando los duplicados")
print(list2)

for i in list2 :
    if i%2 == 0:
        pares.append(i)
    else:
        impares.append(i)
                
    pares.sort()
    impares.sort()
print("Numeros Pares e Impares")
print(pares,impares)

print("Union de numeros pares e impares")
print(pares + impares)


