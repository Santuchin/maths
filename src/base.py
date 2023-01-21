
BINARY = '01'
DECIMAL = '0123456789'
HEXADECIMAL = '0123456789abcdef'
BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
ASCII = bytes(range(0, 127))
BYTES = bytes(range(0, 256))

def encode(number: int, symbols: str | bytes, /) -> str | bytes:

    base = len(symbols)
    
    if base > number:
        return symbols[number:number + 1]
    
    else:
        div, mod = divmod(number, base)
        return encode(div, symbols) + symbols[mod:mod + 1]

def decode(number: str | bytes, symbols: str | bytes, /) -> int:

    if 1 == len(number):
        return symbols.index(number)
    
    else:
        return decode(number[:-1], symbols) * len(symbols) + symbols.index(number[-1])

def valid(number: str | bytes, symbols: str | bytes) -> bool:
    return False if not number else all(map(symbols.__contains__, number))

def encode_limited(number: int, symbols: str | bytes, length: int, /) -> str | bytes:

    base = len(symbols)
    mod = number % base

    if 0 == length:
        return type(symbols)()
    
    else:
        return encode_limited(number // base, symbols, length - 1) + symbols[mod:mod + 1]

def length(number: int, base: int) -> int:

    if base > number:
        return 1

    else:
        return 1 + length(number // base, base)

def encode_void(number: int, symbols: str | bytes, /) -> str | bytes:

    base = len(symbols)
    
    if base > number:
        return symbols[number - 1:number]
    
    else:
        div, mod = divmod(number - 1, base)
        return symbols[mod:mod + 1] + encode_void(div, symbols)

def decode_void(number: str | bytes, symbols: str | bytes, /) -> int:

    if not number:
        return 0
   
    else:
        return 1 + symbols.index(number[0]) + decode_void(number[1:], symbols) * len(symbols)

def length_void(number: int, base: int) -> int:
    ...

def encode_float(number: float, symbols: str | bytes, sep: str | bytes, per: str | bytes) -> str | bytes:
    ...

def encode_float(number: float, symbols: str | bytes, sep: str | bytes, per: str | bytes) -> str | bytes:
    ...

def length_float(number: float, base: int, sep: int, per: int) -> int:
    ...

