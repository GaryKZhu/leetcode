import sys
sys.setrecursionlimit(1501)

n = 1500

Fibbonaccil = []
Fibbonaccil.append(0)
Fibbonaccil.append(1)
#Fibbonacid = {}
#Fibbonacid[1] = 0
#Fibbonacid[2] = 1
def Fibbonacci(n):
    if n in Fibbonaccil:
        return Fibbonaccil

    if n <= 2:
        return Fibbonaccil
    
    else:
        #Fibbonacid[n] = Fibbonacci(n-1) + Fibbonacci(n-2)
        val = Fibbonacci(n-1)
        Fibbonaccil.append(val[-2]+val[-1])
        return Fibbonaccil
##print(Fibbonacci(n)
print(Fibbonacci(n))
