
def primes():

    yield 2

    prev = []
    number = 3

    while True:

        for prime in prev:
            
            if 0 == number % prime:
                break

        else:
            yield number
            prev.append(number)

        number += 2

def fibonacci():

    a = 0
    b = 1

    while True:
        
        yield a

        a, b = b, a + b
