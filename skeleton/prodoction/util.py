from math import floor
def str_to_int(string,round_down=True) :
    """
    Convert string number to integer
    """
    error_msg = "Unable to convert to integer: '%s' " % str(string)
    try:
        integer = float(string.replace(',','.'))
    except AttributeError:
        if isinstance(string,(int,float)):
            integer = string 
        else :
            raise RuntimeError(error_msg) 
            
    except (TypeError,ValueError):
        #logger.exception(error_msg)
        raise RuntimeError(error_msg)
    if round_down :
        integer = floor(integer)
    else :
        integer = round(integer)
    
    return int(integer)
    
# str_to_int('12.4')

# def say_hello():
    
    
#     print("Hello")
# say_hello()