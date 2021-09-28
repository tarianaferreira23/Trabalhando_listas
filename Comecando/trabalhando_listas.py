nomes = ['Tariana', 'Francisco', 'Hamilton', 'Carlos']
nome = input('Informe um nome: ')

resultado = nome in nomes

if resultado == True:
    print('O nome digitalizado já está registrado')
elif resultado == False:
    print('Este nome não se encontra registrado')
    novo = input('quer fazer o registro com este nome: ')
    if novo == 'Sim':
        nomes.append(nome)
        print(nomes)
        print('Seja bem vindo', nome)