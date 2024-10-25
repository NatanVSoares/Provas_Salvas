#[PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos. 
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# À medida que o usuário fornece os dados,
#  armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. 
# Após a inserção de todos os produtos e preços,
#  calcule o valor total da compra somando todos os preços armazenados no dicionário.
#  Por fim, exiba o valor total da compra.


# Solicita a entrada do usuário
fruta_01=input('Qual fruta: ') 
preço_01= float(input('Qual o valor: '))
print('---------------------------------------')

fruta_02=input('Qual fruta:') 
preço_02= float(input('Qual o valor:'))
print('---------------------------------------')

fruta_03=input('Qual fruta:') 
preço_03= float(input('Qual o valor:'))
print('---------------------------------------')

fruta_04=input('Qual fruta:') 
preço_04= float(input('Qual o valor:'))
print('---------------------------------------')

fruta_05=input('Qual fruta:') 
preço_05= float(input('Qual o valor:'))
print('---------------------------------------')



# Cria o dicionário com os dados inseridos
dicionario= {
                fruta_01:preço_01,
                fruta_02:preço_02,
                fruta_03:preço_03,
                fruta_04:preço_04,
                fruta_05:preço_05,

                }


valor_total_da_compra = sum(dicionario.values())


# Exibe o dicionário
print(f'O Valor total da compra foi: {valor_total_da_compra:.2f}')