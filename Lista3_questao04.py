# Questao 4
# A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: 
# os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. 
# Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

fib = [1,1]
i = 0
num = int(input("Digite um numero: "))

while num > len(fib):
	fib.append(fib[i] + fib[i+1])
	i+=1

print ('Fibonacci(%d): %d' %(num,fib[num-1]))