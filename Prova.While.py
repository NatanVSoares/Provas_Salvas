# LPIA-A03]Você está criando um programa em Python para simular um jogo simples de adivinhação.
# O programa deve gerar um número aleatório entre 1 e 10 e pedir ao jogador para adivinhar o número.
#  O jogador terá até 3 tentativas para acertar.

# Implemente o jogo utilizando um loop 'while' para permitir que o jogador faça múltiplas tentativas até acertar ou atingir o limite de tentativas.
#  Utilize a estrutura 'else' para exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo caso as 3 tentativas
# se esgotem sem sucesso.


numero_aleatorio = 7
tentativas = 3

usuario = int(input('Tente Adivinhar um número de 0 á 10: '))


while usuario != numero_aleatorio:
    print('Você errou tente novamente.')

    tentativas-= 1 
    print(f'Você tem mais {tentativas} chances')

    usuario = int(input('Tente Adivinhar um número de 0 á 10: ')) 
    
    if tentativas <= 0:
        print('Suas chances se esgotaram.')
        print(f'Infelizmente você excedeu as três tentativas não fique triste, quem sabe na proxíma :)')
        break

else:
    usuario == numero_aleatorio

    print(f' Parabéns o número Correto é {usuario}.')



    
   




        

    
        

        
   
    
        

