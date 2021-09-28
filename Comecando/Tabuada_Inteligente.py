print("------------------------------")
print('Seja bem vindo a Tabuada Inteligente')
print('-------------------------------------')

def tabuadas():
    num = int(input('Queres ver quantas tabuadas {}? \n'.format(user.title())))
    i= 1
    while i<=num:
        numero = int(input('Digite o {}º número {}: '.format(i, user.title())))
        i +=1
        for cont in range(1,13):
            valor = numero * cont
            print('{} X {} = {}'.format(numero, cont,valor))


user = input('Digite o seu nome: ')
tabuada_resultado = tabuadas()
print(tabuada_resultado)

resposta = input('Ainda quer continuar {}? \n'.format(user.title()))

if resposta =='Sim' or 'sim':
    tabuada_resultado = tabuadas()
    print(tabuada_resultado)
    resposta = input('Ainda quer continuar {}? \n'.format(user.title()))
elif resposta =='n':
    print('Muito obrigada, espero que tenha gostado {}'.format(user.title()))