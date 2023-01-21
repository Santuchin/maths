from . import absolute

def reduce(func, array, /, *args, **kwds):

    if 1 == len(array):
        return array[0]

    else:
        return func(array[0], reduce(func, array[1:], *args, **kwds), *args, **kwds)

def difference(a: tuple[float], b: tuple[float]) -> float:
    return sum(map(lambda a, b: absolute(a - b) ** 2, a, b)) ** 0.5
