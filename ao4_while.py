# Uso do laço de repetição while()

contador = 0
while contador <= 5:
    contador = contador + 1
print(contador)

while True:
    contador = contador -1
    if contador <= 0:
        break
    print(contador)

# while alinhado
linha = 1 
while linha <= 5:
    coluna = 1
    while coluna <= linha:
        print("*", end=" ")
        coluna = coluna + 1
    print()
    linha = linha + 1

print("fim")
