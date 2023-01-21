from sys import builtin_module_names

if 'posix' in builtin_module_names:
    from posix import urandom as bytes

elif 'nt' in builtin_module_names:
    from nt import urandom as bytes

else:
    raise ImportError('no os specific module found')

del builtin_module_names


def decode(number: bytes) -> int:

    if 1 == len(number):
        return number[0]
    
    else:
        return decode(number[:-1]) * 256 + number[-1]

def length(number: int, base: int) -> int:

    if base > number:
        return 1

    else:
        return 1 + length(number // base, base)


def bool() -> bool:
    return 0 == bytes(1)[0] % 2

def until(max: int, /) -> int:

    log = length(max, 256)

    psb = 256 ** log

    div = psb - psb % max

    while True:
        
        number = decode(bytes(log))
        
        if number < div:
            return number % max

def pick(stats: tuple[int]) -> int:

    den = sum(stats)
    idx = until(den)

    value = 0

    for i in range(len(stats)):

        value += stats[i]

        if idx < value:
            return i

def int(start: int, distance: int) -> int:
    
    if 0 > distance:
        return start + -until(-distance)

    else:
        return start + until(distance)

def rational(start: float, times: float, step: float=1) -> float:
    return int(start // step, times * step // step) * step

def choose(array: tuple):
    return array[until(len(array))]

def mix(array: list) -> None:
    
    length = len(array)

    for a in range(length):
        
        b = until(length)

        array[a], array[b] = array[b], array[a]
