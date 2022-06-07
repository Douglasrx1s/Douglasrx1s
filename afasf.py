print('Bem Vindo a Loja do Douglas Reis')
	
#Valor3394180 optei por entrada flutuante pois se trata de dinheiro e pode ter centavos no preço do produto
valor3394180 = float(input('Entre com valor do produto R$ '))
#quantidade optei por uma entrada de numero inteiro pra receber a quantidade de produtos
quantidade = int(input('Entre com a quantidade: '))

#condiçoes
if (quantidade < 10):
  desconto =  0  # 0% de desconto
elif (quantidade >= 10 and quantidade <= 99):
    desconto = 0.05 # 5% de desconto
elif (quantidade >= 100 and quantidade <= 999):
    desconto = 0.10 # 10% de desconto
else:
  desconto = 0.15 # 15% de desconto
# valor sem desconto seria o valor do produto multiplicado pela quantidade de produto
sdesconto =  valor3394180 * quantidade
# valor com desconto seria o valor sem desconto multiplicado pelo desconto menos sem desconto
cdesconto = sdesconto - (sdesconto * desconto)
#o desconto multipliquei o valor do desconto por 100 e limitei as casa pra nao fica os zeros depois da virgula
print('O valor sem desconto foi R${:.2f}'. format(sdesconto))
print('O valr com desconto foi R${:.2f} ( Desconto {:.0f} %)'. format(cdesconto, desconto * 100))
