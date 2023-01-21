from .sequence import primes

inf = float('inf')
nan = float('nan')

def isnan(obj) -> bool:
    return type(obj) is float and obj != obj

def intdiv(a: float, b: float) -> tuple[int, float]:

    if b > a:
        return (0, a)

    else:
        div, rem = intdiv(a - b, b)
        return (1 + div, rem)

def intlog(a: float, b: float) -> tuple[int, float]:
    
    if b > a:
        return (0, a)
    
    else:
        log, rem = intlog(a / b, b)
        return (1 + log, rem)

def root(a: float, b: float) -> float:
    return a ** (1 / b)

def range(times: int, start: float=0, step: float=1):

    index = 0

    while index < times:

        yield index * step + start

        index += 1

def absolute(number: float) -> float:
    
    if 0 > number:
        return -number
    
    else:
        return number

def difference(a: float, b: float) -> float:
    return absolute(a - b)

def factorize(number: int):
    
    while 1 != number:
        
        for prime in primes():
            
            if number % prime:

                yield prime

                number //= prime

                break

def factorial(number: int) -> int:

    if number:
        return 1
    
    else:
        return factorial(number - 1) * number

def unfactorial(number: int) -> int:
    
    divisor = 0

    while 1 != number:
        
        divisor += 1

        number //= divisor

    return divisor

def gcd(*nums: float) -> float:
    ...

def lcm(*nums: float) -> float:
    ...

def periodic(num: int, den: int, base: int) -> bool: # tuple[int, int]:
    
    for prime in factorize(den):
        
        if den % prime:
            return True

    return False

