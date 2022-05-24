book = {}


def avg(value):
    return sum(value) / len(value)


for x in range(int(input())):
    student = input().split()
    name = student[0]
    grade = float(student[1])
    if name not in book:
        book[name] = []
    book[name].append(grade)

for name, grades in book.items():
    grades_formated = [f'{x:.2f}'for x in grades]

    print(f'{name} -> {" ".join(grades_formated)} (avg: {avg(grades):.2f})')
