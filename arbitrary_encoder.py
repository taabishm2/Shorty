#Converts a given value from one base sytem to an arbitrary base system. Symbols can be custom defined
import string

def base_to_decimal(val, base = 73, symbols = None):

    if symbols is None:

        symbols = [str(i) for i in range(0,10)] + list(string.ascii_lowercase) + list(string.ascii_uppercase) + list("$-_.+!*'(),")

        if base < len(symbols):
            symbols = symbols[:base]

    if base > len(symbols):
        raise Exception("Base_SymbolArray_Error:Base does not equal Symbol Set Size.")

    symbol_dic = { symbols[i]:i for i in range(base) } #Dictionary for fast access of key-values

    dec = 0
    val = str(val)[::-1]

    try:
        for i in range(len(val)): dec += symbol_dic[val[i]] * pow(base,i)
    except:
        raise Exception("Symbol_set_deficient:One or more Symbols are not present in the Current Symbol-Set")

    return(dec)


def decimal_to_base(d, base, symbols = None):
    ''' Convert decimal value 'd' into a form with base = "base". If not provided, symbols are defined by the provided-list 'symbols' (ordered sequentially) into
    decimal representation. By default, symbol set is composed of digits(0-9),lower-case alphabets(a-z), upper-case alphabets(A-Z) and
    safe-symbols( $, -, _, ., +, !, *, ', (, ), , ), (in this order). For base>73, user must provide symbol set. Returns result as a string'''

    if symbols is None:

        symbols = [str(i) for i in range(0,10)] + list(string.ascii_lowercase) + list(string.ascii_uppercase) + list("$-_.+!*'(),")

        if base < len(symbols):
            symbols = symbols[:base]

    if base > len(symbols):
        raise Exception("Base_SymbolArray_Error:Base does not equal Symbol Set Size.")

    symbol_dic = { i:symbols[i] for i in range(base) } #Dictionary for fast access of key-values

    res = []

    try:
        while d > 0:
            res.append(symbol_dic[d%base])
            d //= base
    except:
        raise Exception("Symbol_set_deficient:One or more Symbols are not present in the Current Symbol-Set")

    return ''.join(res[::-1])

def base_change(val, ibase, fbase, isymbols = None, fsymbols = None):
    ''' Converts the string 'val' from current base = 'ibase' to a different base 'fbase'. Base 'ibase' has symbol-set 'isymbols' list to represent symbols and base
    'fbase' uses 'fsymbols' list to represent symbols '''

    return( decimal_to_base( base_to_decimal(val, ibase, isymbols) ,fbase,fsymbols) )
