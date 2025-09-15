from school import students, print_student_info, calculate_average, safe_execute, divide, string_to_int

print('All students: \n')
for name, grades in students.items():
    print_student_info(name, grades)

students['Eva'] = {'math': 90, 'english':87, 'history': 93}

top_student = max(students.items(), key=lambda x: calculate_average(x[1]))

print(f'Top student: {top_student[0]} with average {calculate_average(top_student[1]):.2f}' )

students.pop('Bob')
for name, grades in students.items():
    print_student_info(name, grades)

# Test
safe_execute(divide, 10, 0)

safe_execute(divide, 10, 'hello')

safe_execute(string_to_int, 'abc')




if __name__ == '__main__':
    print('\n Script was run directly')