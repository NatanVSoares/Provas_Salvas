#[PYIA-A02] Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, 
# o telefone e o email. Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, 
# o número de telefone e o endereço de email. Após coletar todas as informações necessárias,
#  exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.




# Solicita a entrada do usuário
nome=input('Digite seu nome:') 
print('---------------------------------------')

telefone=input('(tel):')
print('---------------------------------------')

email=input('E-mail:')
print('---------------------------------------')


# Cria o dicionário com os dados inseridos
dicionario= {   'Nome':nome,
                'Telefone':telefone,
                'e-mail':email
}

# Exibe o dicionário
print(dicionario)