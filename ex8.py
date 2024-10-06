x = float(input('informe o valor da conta:R$'))
porcent_gorjeta = float(input("Quanto cobra pela gorjeta: "))

valor_gorjeta = x * porcent_gorjeta/100

total = valor_gorjeta + x

print(f'valor da conta mais a gorjeta deu R${total}')