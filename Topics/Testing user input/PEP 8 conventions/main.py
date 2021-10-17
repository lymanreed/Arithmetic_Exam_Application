def check_name(variable_name):
    if variable_name in 'lOI':
        print("Never use the characters 'l', 'O', or 'I' as single-character variable names")
    elif variable_name.islower():
        print('It is a common variable')
    elif variable_name.isupper():
        print('It is a constant')
    else:
        print('You shouldn\'t use mixedCase')
