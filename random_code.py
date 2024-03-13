import string
import random

length = 16
string_list = ''.join([string.ascii_lowercase, string.ascii_uppercase, string.digits])


i = 1
times = 3
while (i <= times):
    code = ''.join(random.choices(string_list, k=length))
    i += 1
    print(code)