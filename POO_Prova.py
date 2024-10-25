# [PYIA-A11] Crie uma classe base chamada Animal que tenha um método chamado falar,
#  o qual imprime uma mensagem genérica, como "Este animal faz um som." Em seguida, 
# crie duas subclasses chamadas Cachorro e Gato que herdem de Animal. Dentro de cada uma dessas subclasses,
#  sobrescreva o método falar para que ele imprima uma mensagem específica para cada animal. 
# Por exemplo, na classe Cachorro, o método falar pode imprimir "O cachorro late." e, na classe Gato,
# pode imprimir "O gato mia."


class Animal:

    def falar(self):
        print('Este animal faz um som')

class Cachorro(Animal):
    def falar(self):
        return('Au au au auuuuu')

class Gato(Animal):
    def falar(self):
        return('Miau miau miaaaaau')


cao = Cachorro()
print(f' O meu cachorro diz {cao.falar()}')

print('-'*100)


gatinho = Gato()
print(f'O meu gato diz {gatinho.falar()}')






