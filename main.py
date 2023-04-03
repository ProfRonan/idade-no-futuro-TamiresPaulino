anoAtual = int(input('Digite o ano atual:'))
idade = int(input('Qual a sua idade? '))
anoFuturo = int(input('Digite um ano futuro: '))
nome = input('Digite seu nome?')

novaIdade = (anoFuturo - anoAtual) + idade 

print(nome +  ', no ano de ' + str(anoFuturo) + ' você terá ' + str(novaIdade) + ' anos')
