#Preguntas de rescate Fibonacci

f = [0,1]
n = int(input("give me a numbers:  "))
for _ in range (n):
    f.append (f[-1] + f[-2])
for num in f[:n]:
    print(num)

