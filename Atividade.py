print('Aqui esta minha atividade')

nome =  input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu sua altura: "))

print('Seu nome é: ',nome)
print('Sua idade é',idade)
print('Seu peso é: ' ,peso)
print('Sua altura é: ' ,altura)

print(f'Seu nome é {nome} \ne sua idade é {idade} anos.\nVocê pesa {peso} e tem a seguinte altura {altura} em cms')
print('Seu Nome é classe: ', type(nome))
print('Sua idade é classe: ', type(idade))
print('Seu peso é classe: ', type(peso))
print('Sua altura é classe: ', type(altura))