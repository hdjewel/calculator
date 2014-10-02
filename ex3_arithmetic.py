def add(x , y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y

def divide(divisor, dividend):
    # this only returns the quotient not the remainder
    return divisor / dividend  

    return square(base) * base

def cube(x):
    return x ** 3

def power(base, exponent):
    
    return_value = 1
    quotient = exponent / 3

    if quotient == 0:
        remainder = exponent % 3

        if remainder == 0:
            return_value = 1
        elif remainder == 1:
            return_value = base
        else:
            return_value = base * base
    else:
        for num in range (0, quotient):
            return_value = return_value * cube(base)
        remainder = exponent % 3
        if remainder == 1:
            return_value = return_value * base
        elif remainder ==2:
            return_value = return_value * base * base


    return return_value

            #base ** exponent

            # if expo 1
               #return base
            #if expo even
                #return...
            #if expo odd
                #return...
# this is the end of the function power

def mod(divisor, dividend):
    return divisor % dividend  # this will return the remainder

def main():
    


main()