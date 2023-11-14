#Chequeo de errores
def dna_checker(row):
    while True:             
        if len(row)==6:        # Acá verifica que la longitud sea la correcta
            row = list(row)
            for i in range (6):     # Acá verifica que el caracter ingresado sea el correcto
                while True:         
                    if row[i]=="A" or row[i]=="T" or row[i]=="C" or row[i]=="G":    
                        break
                    else:
                        row[i] = input(f"ERROR, {i+1} ({row[i]}) es incorrecto. Ingréselo nuevamente: ").upper()
                        continue
            break
        else:
            row = input(f"Incorrecto, ingrese solo 6 caracteres ").upper()
            continue
    return row
#-----------------------------
def is_mutant(dna): #Chequeo si hay presencia de ser mutante o no
    mutant = True
    check = row_check(dna) + column_check(dna) + diagonal_check(dna) + reverse_diagonal_check(dna)
    if check < 2:
        return False
    elif check >=2:
        return True
#-----------------------------
def row_check (dna):  #Chequeo de fila
    row_counter = 0
    for i in range(6):
        for j in range(3):
            if dna[i][j]==dna[i][j+1] and dna[i][j]==dna[i][j+2] and dna[i][j]==dna[i][j+3]:
                row_counter = row_counter + 1
                break
    return row_counter

#-----------------------------
def column_check(dna):  #Chequeo de columna
    column_counter = 0
    for i in range(6):
        for j in range(3):
            if dna[i][j]==dna[i][j+1] and dna[i][j]==dna[i][j+2] and dna[i][j]==dna[i][j+3]:
                column_counter = column_counter + 1
                break
    return column_counter
#-----------------------------
def diagonal_check(dna):  #Chequeo de diagonal (derecha)
    diagonal_counter = 0
    for i in range(3):
        for j in range(3):
            if dna[i][j]==dna[i+1][j+1] and dna[i][j]==dna[i+2][j+2] and dna[i][j]==dna[i+3][j+3]:
                diagonal_counter = diagonal_counter + 1
    return diagonal_counter
#-----------------------------
def reverse_diagonal_check(dna):   #Chequeo de diagonal invertida (izquierda)
    reverse_diagonal_counter = 0
    for i in range(5, 2, -1):
        for j in range(3):
            if dna[i][j]==dna[i-1][j+1] and dna[i][j]==dna[i-2][j+2] and dna[i][j]==dna[i-3][j+3]:
                reverse_diagonal_counter = reverse_diagonal_counter + 1
    return reverse_diagonal_counter

