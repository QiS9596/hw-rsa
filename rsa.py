import random
import fractions
class keyGenerator:
    lst = []
    def __init__(self):
        for i in range(2,10000):
            if self.isProbablePrime(i):
                self.lst.append(i)

    def isProbablePrime(self,n, trials = 5):
        assert n >=2
        if n == 2 :
            return True
        if n%2 == 0:
            return False
        s = 0
        d = n-1
        while True:
            quotient, remainder = divmod(d,2)
            if remainder == 1:
                break
            s +=1
            d = quotient

        assert(2**s*d == n-1)

        def try_composite(a):
            if pow(a,d,n) == 1:
                return False
            for i in range(s):
                if pow(a,2**i*d,n) == n-1:
                    return False
            return True

        for i in range(trials):
            a = random.randrange(2,n)
            if try_composite(a):
                return False

        return True

    def random_N_digits(self,n):
        start = 10**(n-1)
        end = (10**n)-1
        return random.randint(start, end)

    def primeGeneration(self,digit):
        while True:
            p = self.random_N_digits(digit)
            for i in self.lst:
                if p%i == 0:
                    p = p+2
                    continue
                if self.isProbablePrime(p):
                    return p
                else: p = p+2

    def keyGeneration(self,digit):
        p = self.primeGeneration(digit)
        q = self.primeGeneration(digit)
        n = p*q
        phin = (p-1)*(q-1)
        e = phin-1
        for i in range(2,phin -1):
            if(fractions._gcd(i,phin) == 1):
                e = i
                break
        privateKey = 0
        for i in range(1,1000):
            product = i*phin+1
            print(product)
            if(product%e == 0):
                privateKey = product
                break
        file = open('n.txt','w')
        file.write(n.__str__())
        file.close()
        file = open('e.txt','w')
        file.write(e.__str__())
        file.close()
        file = open('d.txt','w')
        file.write(privateKey.__str__())
        file.close()

def squareAndMultiply(exponent, base, modulus):
    exponent2 = bin(exponent)
    exponent2 = exponent2[2:exponent2.__len__()]
    result = 1
    for i in range(exponent2.__len__()-1, -1, -1):
        result = result*result%modulus
        if exponent2[i] == '1':
            result = result*base%modulus
    return result

a = keyGenerator()
a.keyGeneration(500)