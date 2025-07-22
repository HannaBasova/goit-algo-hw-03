import re
'''
function that normalizes phone numbers to a standard format +38XXXXXXXXXX'

Input:
:param phone_number: str
Output:
:param formatted_phone_number: str
'''
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
     "38050 111 22 11   "
]

def normalize_phone(phone_number: str) -> str:
    pattern =r'[^\d+]'
    replacement = ''
    formatted_phone_number = re.sub(pattern, replacement, phone_number)
    if not formatted_phone_number.startswith('+38'):
        formatted_phone_number = '+38' + formatted_phone_number
    return formatted_phone_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
