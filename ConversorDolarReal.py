dolar = input("Quantos dólares você tem? ")
dolar = float(dolar)
cotacaoReal = input("Qual a cotação do real? ")
cotacaoReal = float(cotacaoReal)
real = dolar * cotacaoReal
real = round(real, 2)
real = str(real)
print ("Você terá R$" + real + " reais.")