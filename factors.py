import sys

def factorize(num):
    factors = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    return factors

def find_factors(num):
    factors = factorize(num)
    if len(factors) == 1:
        print(f'{num}={factors[0]}*{factors[0]}')
    else:
        print(f'{num}={factors[0]}*{factors[-1]}')

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            num = int(line.strip())
            find_factors(num)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: factors <file>')
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
