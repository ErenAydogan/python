user_info = {
    'name':'Joe',
    'surname' : 'Doe',
    'age' : 40,
    'job' : 'developer'
}

user_list = [(key, value) for key, value in user_info.items()]

print(user_list)