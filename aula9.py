a = 'AAAAA'
b = 'BBBBB'
c = 1.1
string = 'a = {nome1} a ={nome1} b = {nome2} a={nome1} {nome3:.2f}' #pode se adcionar quantos argumentos quiser.
formato = string.format( nome1 = a, nome2 = b, nome3 =c) # a,b e c são argumentos de formato, ''é a string,
#é usado .format(), para não depender da ordem
#pode os colocar em qualquer ordem 
print(formato)