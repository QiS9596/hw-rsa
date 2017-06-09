import random
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
