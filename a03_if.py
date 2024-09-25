# Controle de fluxo "if"

habilitado = True
if habilitado:
    print("Está habilitado!")

print("Esta linha sempre será impressa")

if habilitado:
    print("Ok. Habilitado")
else:
    print("Nada feito. Não está habilitado")

media = 8 
if media >= 6: 
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
elif media >= 4:
    print("Trabalho de recuperação")
else:
    print("Reprovado")

print("Terminado")