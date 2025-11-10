casa=float(input("Valor da casa : "))
salario=float(input("Seu salario :  "))
anos= int(input("Quantos anos de financiamento ?  "))
prestracao = casa/(anos*12)
minimo=salario * 30/100
print(f"Para pagar uma casa de RS{casa: .2f} em {anos} anos")
print(f"A prestação sera de R${prestracao: .2f}")
if prestracao <= minimo:
    print("Emprestimo pode ser aprovado. ")
else:
    print("Emprestimo negado. ")
print(input("Deseja fazer uma nova consulta ? Digite S/N: "))
while True:
    break
    continue