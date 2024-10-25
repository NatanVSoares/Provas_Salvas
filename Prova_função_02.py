# [PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos. 
# Esta função deve comparar os três números e identificar qual deles é o maior.
#  Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois.
#  A função deve então retornar o maior número encontrado.


#A função maior_numero recebeu seus parametros a,b,c
def maior_numero(a,b,c):

#Foi criado uma condição de qual argumento(numero)é maior:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

#Mostro na tela qual dos argumentos que coloquei é maior:
print(maior_numero(10,90,100))

#Ass Neitan ;)