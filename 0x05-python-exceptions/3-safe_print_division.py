#!/usr/bin/python3
def safe_print_division(a, b):
    if b != 0: 
        try:
            print("Inside result: {}".format(a / b))
        except:
            print("invalid process!")
        finally:
            return a / b
    else:
        try:
            print("Inside result: None")
        except:
            pass
        finally:
            return None
