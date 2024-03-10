import string
import random

length = 2
string_list = ''.join([string.ascii_lowercase, string.ascii_uppercase, string.digits])
stop_code = "AB"

number = 1
while True:
    code = ''.join(random.choices(string_list, k=length))
    print(number, "-", code)
    number += 1
    if (code == stop_code):
        break