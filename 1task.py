class SpreadingOutNumbers:
    def __init__(self, N):
        self.N = N
        self.list_of_numbers = list(i for i in range(self.N + 1))

    def spreading_out(self,n):
        i = 2
        primfac = []
        while i * i <= n:
            while n % i == 0:
                primfac.append(i)
                n = n / i
            i = i + 1
        if n > 1:
            primfac.append(n)
        if len(primfac) == 1:
            primfac.insert(0, 1)
        return primfac

    def simple_factors(self):
        for number in self.list_of_numbers:
            print('Разложение числа {number}: {simple_factors}'.format(number=number, simple_factors = self.spreading_out(number)))

if __name__ == '__main__':
    SimpleFactors = SpreadingOutNumbers(int(input("Введите число N: ")))
    print(SimpleFactors.simple_factors())
    print("Сложность алгоритма O(sqrt(n))")