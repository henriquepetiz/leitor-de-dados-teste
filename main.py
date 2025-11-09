####leitor de dados pequenos


f = open("sinalizacao.csv")


###identificar data mais antiga

antiga = '' ### variavel para armazenar a data mais antiga
primeira = True ### variavel para identificar a primeira linha
ausente = [] ### identificar dados ausentes
interesse = [] ## identificar dados de interesse
for line in f:
  if primeira:
    primeira = False
    continue
  lista = line.strip().split(';')   ###cria lista 
  if antiga == '' or antiga > lista[4]:
    antiga = lista[4]
  if lista[13].strip() == '' or lista[14].strip() == '':
    ausente.append(lista)
  if lista[13].strip() != '' or lista[14].strip() != '':
    interesse.append(lista)
    


##Sinalliza a data mais antiga no arquivo
print(f"Data da primeira implementacao: {antiga}")
print() ## quebra de linha para melhor visualizacao
print(f"Dados sem latitude ou longitude:  {ausente}")
print() ## quebra de linha para melhor visualizacao
print(f"Dados com latitude ou longitude:  {interesse}")
