with open('salary.txt') as m_salary, open('salary_year.txt', 'w') as y_salary:
    for line in m_salary:
        y_salary.write(f'{int(line) * 12}\n')
