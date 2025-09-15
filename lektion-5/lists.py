li1 = [1, 2, 3, 4, 5]
li2 = list((1, 2, 3, True, 4.9))
li3 = list('Python')

print(li1, li2, li3)

li1 = ['value'] * 5
li2 = [4] * 5

print(li1)
print(li2)

li1 = [1, 2, 3, 4, 5]
print(li1[0])
print(li1[1:4])

li = []

li.append(5)
print(li)

li.insert(0, 4)
print(li)

li.extend([6, 7, 8])
print(li)

li[1] = 5.5
print(li)

li.clear()
print(li)

li1 = [1, 2, 3, 4, 5]

li1.remove(4)
print(li1)

popped = li1.pop(1)
print(popped)
print(li1)

del [li1[0]]
print(li1)

li = ['apple', 'banana', 'cherry', 'banana', 'date']
print('Start:', li)

for item in li[:]:
    if item == 'banana':
        li.remove(item)
        print(f'Removed {item}')
    elif item == 'cherry':
        popped = li.pop(li.index(item))
        print(f'Popped {popped}')

print('Done:', li)

scores = [3, 5, 1, 4]
stars = ['⭐' * score for score in scores if score % 2 != 0]
print(stars)

li = [i for i in range(10)]
print(li)

li = [(x, y) for x in range(5) for y in range(5)]

for x in range(5):
    for y in range(5):
        print(f'({x}.{y})', end=' ')
    print()

li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(li)

li2 = [val for row in li for val in row]
print(li2)

students = [
    ['Alice', [85, 92, 78]],
    ['Bob', [70, 88, 90]],
    ['Clara', [95, 100, 98]],
]

for student in students:
    name = student[0]
    grades = student[1]
    print(f'{name} has grades: {grades}')

for student in students:
    name = student[0]
    grades = student[1]
    average = sum(grades) / len(grades)
    print(f'{name}: {average:.2f}')

students.sort(key=lambda s: sum(s[1])/len(s[1]), reverse=True)

print(students)

