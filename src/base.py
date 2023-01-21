# TODO: encode_int, decode_int, periodic, encode_rational, decode_rational

BINARY = '01'
DECIMAL = '0123456789'
HEXADECIMAL = '0123456789abcdef'
BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
BYTES = bytes(range(0, 256))

def encode(number: int, symbols: str, /) -> str:

    base = len(symbols)
    
    if base > number:
        return symbols[number]
    
    else:
        return encode(number // base, symbols) + symbols[number % base]

def decode(number: str, symbols: str, /) -> int:

    if 1 == len(number):
        return symbols.index(number)
    
    else:
        return decode(number[:-1], symbols) * len(symbols) + symbols.index(number[-1])

def valid(number: str, symbols: str) -> bool:
    return False if '' == number else all(map(symbols.__contains__, number))

def encode_limited(number: int, symbols: str, length: int, /) -> str:

    base = len(symbols)
    
    if 1 == length:
        return symbols[number % base]
    
    else:
        return encode_limited(number // base, symbols, length - 1) + symbols[number % base]

def length(number: int, base: int) -> int:

    if base > number:
        return 1

    else:
        return 1 + length(number // base, base)

def encode_void(number: int, symbols: bytes, /) -> str:

    base = len(symbols)
    
    if base > number:
        return symbols[number - 1:number]
    
    else:
        div, mod = divmod(number - 1, base)
        return symbols[mod:mod + 1] + encode_void(div, symbols)

def decode_void(number: str, symbols: bytes, /) -> int:

    if b'' == number:
        return 0
   
    else:
        return 1 + symbols.index(number[0]) + decode_void(number[1:], symbols) * len(symbols)

