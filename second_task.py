import random

'''
Function which generates a set of unique random numbers from min to max in range quantity

Input:
:param min: integer
:param max: integer
:param quantity: integer

Output:
:return: list
'''

def get_numbers_ticket(min:str, max:str, quantity:str)->list:
    try:
        if min < 1 or max > 1000 or quantity > max or quantity < min :
            return list()
        else:
            return random.sample(range(min,max),quantity)
    except TypeError:
        return list()
print(get_numbers_ticket( 1,100,6))