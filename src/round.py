
def round_raw(number: float, mul: float) -> float:
    return number - number % mul

def round(number: float, mul: float=1, half: bool=False) -> float:

    if 0 < number:
        mul = -mul

    fst = round_raw(number, mul)
 
    if half:

        sec = round_raw(number, -mul)

        if abs(number - sec) < abs(number - fst):
            return sec

        else:
            return fst

    else:
        return fst

def builtin(number: float, digits: int=0) -> None:
    return round(number, 10 ** -digits, True)

