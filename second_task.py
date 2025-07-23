import random

'''
A function that generates a set of unique random numbers from a minimum to a maximum

Input:
:param min: integer
:param max: integer
:param quantity: integer

Output:
:return: list
'''

def get_numbers_ticket(min:int, max:int, quantity:int)->list:
    try:
        if min < 1 or max > 1000 or (max-min+1) < quantity:
            return list()
        else:
            return random.sample(range(min,max+1),quantity)
    except TypeError:
        return list()
print(get_numbers_ticket( 1,100,6))
print(get_numbers_ticket( 10,20,5))
print(get_numbers_ticket( 1,5,5))
print(get_numbers_ticket( 1000,1200,10))
print(get_numbers_ticket( 10,4,5))
print(type(get_numbers_ticket( 10,13,4)))