tempo_anos = float(input("Há quanto tempo você fuma? (anos)....: "))

valor_maco = float(input("Qual o valor atual de um maço de cigarro?....: "))
quantidade_dia = float(input("Qual a quantidade de maços, em média, que você fuma por dia?....: "))

tempo_dias = (tempo_anos * 12) * 30
gasto_total = (valor_maco * quantidade_dia) * tempo_dias

if(gasto_total < 20000):
  print(f"Com o valor R${gasto_total}, você poderia ter dado entrada em um carro.")
elif(20000 < gasto_total < 50000):
  print(f"Com o valor R${gasto_total}, você poderia ter comprado um carro popular usado.")
else:
  print(f"Com o valor R${gasto_total}, você poderia ter comprado um carro zero.")
