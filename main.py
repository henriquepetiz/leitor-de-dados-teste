####leitor de dados pequenos


f = open("sinalizacao.csv")


###identificar data mais antiga

antiga = ''
primeira = True
for line in f:
  if primeira:
    primeira = False
    continue
  lista = line.strip().split(';')   ###cria lista 
  if antiga == '' or antiga > lista[4]:
    antiga = lista[4]
  print(lista)


print (antiga)