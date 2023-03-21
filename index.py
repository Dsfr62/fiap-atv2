# Nome: Bruno Lago      - RM86810
# Nome: Eduardo Kentho  - RM551971
# Nome: Kayke Andrade   - RM550738
# Nome: Eduardo Sávio   - RM97833

def main(tempo_anos=0, valor_maco=0, quantidade_dia=0):
  if tempo_anos == 0:
    tempo_anos=float(input("\nHá quanto tempo você fuma? (anos)....: "))
  if valor_maco == quantidade_dia:
    quantidade_dia=float(input("Qual a quantidade de maços, em média, que você fuma por dia?....: "))
  if valor_maco == 0:
    valor_maco=float(input("Qual o valor atual de um maço de cigarro?....: "))

  tempo_dias = (tempo_anos * 12) * 30
  gasto_total = (valor_maco * quantidade_dia) * tempo_dias

  if(gasto_total < 20000):
    print(f"\nCom o valor R${gasto_total}, você poderia ter dado entrada em um carro.")
  elif(20000 < gasto_total < 50000):
    print(f"\nCom o valor R${gasto_total}, você poderia ter comprado um carro popular usado.")
  else:
    print(f"\nCom o valor R${gasto_total}, você poderia ter comprado um carro zero.")

main(2, 10, 1.5)
main(10.5, 9, 1)
main(8, 11, 2.5)
main()