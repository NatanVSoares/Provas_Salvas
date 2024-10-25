# [PYIA-A04] Crie uma função chamada media que receberá três números como argumentos. 
# Esta função deve calcular a média aritmética desses três números.
#  Para fazer isso, some os três números e, em seguida, divida o resultado por três.
#  Por fim, a função deve retornar o valor da média aritmética calculada.


#Criei uma função chamada média que recebe os parametros a,b,c
def media(a,b,c):
    #retorna a média aritmética dos 3 numeros que os chamei de parametro a,b,c.
    return (a+b+c)/3

#o programa não pede para criar usúario, mas fiz por conta de ser mais interessante,
#mas sei que na prática devo fazer o que o cliente pede do jeito que pedir !

num_01 = int(input('Digite um número: '))
print('-----------------------------------------')
num_02 = int(input('Digite um número: '))
print('-----------------------------------------')
num_03 = int(input('Digite um número: '))
print('-----------------------------------------')

#Mostro na tela o calculo da média.
print(f'A média aritmética é {media(num_01,num_02,num_03):.2f}')


#Ass Neitan ;)


