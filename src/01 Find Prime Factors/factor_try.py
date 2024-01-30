#Prime factor class
class Factor:
  FIRST_PRIME = 2

  def __init__(self, value) -> None:
    self.value = value
    self.primeNums = [2]

  def findPrimeFactors(self):
    self.primeFactors = []
    curValue = self.value
    # for num in self.primeNums:
      # if curValue % num != 0:
      #   continue
      # self.primeFactors.append(num)
      # getPrimeNums()
    # curPrime = 0
    # primeNums = getPrimeNums()
    for curPrime in self.primeNums:
      # curPrime = Factor.getnextleastprimefactor(curPrime, self.getPrimeNums())
      while curValue % curPrime == 0:
        self.primeFactors.append(curPrime)
        curValue = int(curValue / curPrime)
    return self.primeFactors

  def getPrimeNums(self): 
    sqrt = self.value ** 0.5
    for n in range(Factor.FIRST_PRIME + 1, self.value):
        for m in self.primeNums:
          if n % m == 0:
            break
          else:
            self.primeNums.append(n)
    return self.primeNums

  # def getnextleastprimefactor(curPrime, primeNums):
  #   if curPrime == 0:
  #     return Factor.FIRST_PRIME
  #   for n in primeNums:
  #     if n > curPrime:
  #       return n

print(Factor(10).findPrimeFactors())
print(Factor(460).findPrimeFactors())
print(Factor(13).findPrimeFactors())
print(Factor(630).findPrimeFactors())
print(Factor(24).findPrimeFactors())
