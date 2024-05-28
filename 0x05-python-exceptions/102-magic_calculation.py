#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0  # LOAD_CONST 1 (0), STORE_FAST 2 (result)
    for i in range(1, 3):  # SETUP_LOOP
        try:  # SETUP_EXCEPT
            if i > a:  # LOAD_FAST, LOAD_FAST, COMPARE_OP
                raise Exception('Too far')  # LOAD_GLOBAL, LOAD_CONST, CALL_FUNCTION, RAISE_VARARGS
            else:
                result += (a ** b) / i  # LOAD_FAST, LOAD_FAST, LOAD_FAST, BINARY_POWER, BINARY_TRUE_DIVIDE, LOAD_FAST, BINARY_ADD, INPLACE_ADD,
        except:  # POP_TOP, POP_TOP, POP_TOP
            pass
        result += b + a  # LOAD_FAST, LOAD_FAST, BINARY_ADD, STORE_FAST, BREAK_LOOP, POP_EXCEPT, JUMP_ABSOLUTE, END_FINALLY
    return result  # LOAD_FAST, RETURN_VALUE
