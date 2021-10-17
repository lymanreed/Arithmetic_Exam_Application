for n in range(1, 11):
    with open(f'file{n}.txt', 'w', encoding='utf-8') as f:
        f.write(str(n))

