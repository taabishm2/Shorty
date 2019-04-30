#Converts a given value from one base sytem to an arbitrary base system. Symbols can be custom defined
import string

def base_to_decimal(val, base = 73, symbols = None):
    ''' Converts string 'val' with base = 'base' and symbol-set defined by the provided-list 'symbols' (ordered sequentially) into decimal representation.
    By default, symbol set is composed of digits(0-9),lower-case alphabets(a-z), upper-case alphabets(A-Z) and safe-symbols( $, -, _, ., +, !, *, ', (, ), , ),
    (in this order) thus, the max base with default symbols is 73 (also the default conversion base). If base < 73 given without symbol-set, default-5set is truncated.
    Enclose the 'val' in double quotes as single quotes may be part of string.'''

    if symbols is None:
        
        symbols = [str(i) for i in range(0,10)] + list(string.ascii_lowercase) + list(string.ascii_uppercase) + list("$-_.+!*'(),")

        if base < len(symbols):
            symbols = symbols[:base]
        
    if base > len(symbols):
        raise Exception("Base_SymbolArray_Error:Base does not equal Symbol Set Size.")

    symbol_dic = { symbols[i]:i for i in range(base) } #Dictionary for fast access of key-values

    dec = 0
    val = str(val)[::-1]
    for i in range(len(val)): dec += symbol_dic[val[i]] * pow(base,i)

    return(dec)


    
