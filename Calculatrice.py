

print("\n******************* Python Calcolatrice *******************")

def addizione(x, y):
	return x + y

def sottrazione(x, y):
	return x - y

def moltiplicazione(x, y):
	return x * y

def divisione(x, y):
	return x / y

print("\nScegli il numero di operazione desiderato: \n")
print("1 - Addizione")
print("2 - Sottrazione")
print("3 - Moltiplicazione")
print("4 - Divisione")

scelta = input("\nInserisci l'opzione (1/2/3/4): ")


num1 = int(input("\nImmettere il primo numero: "))
num2 = int(input("\nImmettere il primo numero: "))

if scelta == '1':
	print("\n")
	print(num1, "+", num2, "=", addizione(num1, num2))
	print("\n")

elif scelta == '2':
	print("\n")
	print(num1, "-", num2, "=", sottrazione(num1, num2))
	print("\n")

elif scelta == '3':
	print("\n")
	print(num1, "*", num2, "=", moltiplicazione(num1, num2))
	print("\n")

elif scelta == '4':
	print("\n")
	print(num1, "/", num2, "=", divisione(num1, num2))
	print("\n")

else:
	print("\nOpzione non valida!")

	
	
