'''
Crie um programa que receba os dados de um usuário, armazene-os em um dicionário, e os informe na tela. Os dados cadastrais serão os mesmos encontrados no gerador de pessoas do site 4 devs (em anexo). Ao terminar, envie o link do repositório.
'''
pessoa = {}

# Nova chave
pessoa['nome'] = input('Informe o nome da Pessoa:')
pessoa['CPF'] = input('Informe o CPF:' )
pessoa['RG'] = input('Informe o RG:')
pessoa['Data de Nascimento'] = input('Informe a Data de Nascimento:' )
pessoa['Sexo'] = input('Informe o Sexo da pessoa:' )
pessoa['Signo'] = input('Informe o Signo da pessoa:' )
pessoa['Mãe'] = input('Informe o nome da Mãe:' )
pessoa['Pai'] = input('Informe o nome do Pai:' )
pessoa['Email'] = input('Informe o Email:' )
pessoa['Senha'] = input('Informe o Senha do Usuário:' )
pessoa['CEP'] = input('Informe o CEP:' )
pessoa['Endereço'] = input('Informe o Endereço:' ) 
pessoa['Número'] = input('Informe o Número da rua:' )
pessoa['Bairro'] = input('Informe o Bairro:' )
pessoa['Estado'] = input('Informe o Estado:' )
pessoa['Telefone'] = input('Informe o Telefone:' )
pessoa['Celular'] = input('Informe o Celular:' )
pessoa['Altura'] = input('Informe da Altura da pessoa:' )
pessoa['Peso'] = input('Informe o Peso da pessoa:' )
pessoa['Tipo Sanguineo'] = input('Informe o Tipo Sanguineo da pessoa:' )
pessoa['Cor Favorita'] = input('Informe a Cor Favorita:' )

# exibindo valores
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')