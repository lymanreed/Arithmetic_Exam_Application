def check():
    msg = 'Correct the error!'
    try:
        a = int(input())
        if a not in range(25, 38):
            print(msg)
        else:
            print(a)
    except ValueError:
        print(msg)
