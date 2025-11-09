####leitor de dados pequenos


f = open("sinalizacao.csv")


###identificar data mais antiga

antiga = ''
for line in f:
  campos = line.strip().split(';')
  if len(campos) > 4 and campos[4]:
    if antiga == '' or antiga > campos[4]:
      antiga = campos[4]

print (antiga)