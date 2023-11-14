import funcion_parcial2
dna = []

for i in range(6):
    row = input(f"Ingrese la cadena de ADN {i+1}: ").upper()
    row = funcion_parcial2.dna_checker(row)
    dna.append(row)
    
print("Su secuencia de adn indica que: ")
for i in range (6):
    print(dna[i])
print("Vamos a comprobar si es mutante o no.")

if funcion_parcial2.is_mutant(dna) == True:
    print("ES MUTANTE")
elif funcion_parcial2.is_mutant(dna) == False:
    print("NO ES MUTANTE")
