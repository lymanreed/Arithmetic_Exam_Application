import random
random.seed()


def run_test(lvl):
    right = 0
    for _ in range(5):
        if lvl == '1':
            task = f"{random.randint(2, 9)} {random.choice(['+', '-', '*'])} {random.randint(2, 9)}"
            print(task)
        else:
            num = random.randint(11, 29)
            print(num)
            task = f'{num} ** 2'
        while True:
            try:
                answer = int(input())
                if eval(task) == answer:
                    right += 1
                    print('Right!')
                else:
                    print('Wrong!')
                break
            except ValueError:
                print('Wrong format! Try again.')
    return right


while True:
    print('''Which level do you want? Enter a number:
    1 - simple operations with numbers 2-9
    2 - integral squares of 11-29''')
    level = input()
    if level == '1' or level == '2':
        break
    print('Incorrect format.')

correct = run_test(level)

print(f'Your mark is {correct}/5')
print('Would you like to save your result to the file? Enter yes or no.')
if input() in ('yes', 'YES', 'y', 'Yes'):
    print('What is your name?')
    name = input()
    with open('results.txt', 'a') as results_file:
        s = f'{name}: {correct}/5 in level '
        s += '1 (simple operations with numbers 2-9).' if level == 1 \
            else '(2 - integral squares of 11-29).'
        results_file.write(s)
    print('The results are saved in "results.txt".')
