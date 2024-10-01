# lista = conjunto de valores
# lista = [valor1 , valor2, ...]
# lista = list(valor1, valor2, ...)

ListaVazia = [] # cria lista vazia

ListaComElementos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ListaComElementosMista = [7, "Python", 3.14159, True, 'c']

ListaComElementos[0] #pega o primeiro elemento
ListaComElementos[-1] #pega o ultimo elemento
ListaComElementos[:4] #pega os 3 primeiros
ListaComElementos[3:] #pega do terceiro item em diante
ListaComElementos[3:6] #pega do terceiro até o quinto
ListaComElementos[3:8:2] #pega do terceiro ao sétimo de 2 em 2 

print(ListaComElementos[3:8:2])

len(ListaComElementos) # retorna numero de elementos
print(len(ListaComElementos))

max(ListaComElementos) #retorna o maior valor
print(max(ListaComElementos))

min(ListaComElementos) #retorna o menor valor
sum(ListaComElementos)# retorna a soma de todos os elementos 

print(sum(ListaComElementos))
sorted(ListaComElementos) # retorna a lista em ordem crescente
