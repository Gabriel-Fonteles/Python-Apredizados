def collatz(number) :
    if number % 2 == 0:
        print(number//2)
        return number//2
    elif number % 2 == 1:
        print(3*number + 1)
        return 3 * number + 1
    
print ('Digite um numero inteiro:')
try:
    number = int(input())
    while number != 1:
      number = collatz (number)
except ValueError:
    print("Você deve digitar um número inteiro.")