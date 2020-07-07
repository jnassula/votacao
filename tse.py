idade = int(input('Qual a sua idade?\n '))

if idade < 16:
    print('Você não tem idade para votar!')
elif idade < 18:
    print('Seu voto é facultativo!')
elif idade < 70:
    print('Seu voto é obrigatório!')
else:
    print('Seu voto não é amis obrigatório!')

print('FIM')