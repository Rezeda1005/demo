class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()
        
    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for key in self.grades:
            grades_count += len(self.grades[key])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for key in self.grades:
            grades_count += len(self.grades[key])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


some_lecturer_1 = Lecturer('Some', 'Buddy')
some_lecturer_1.courses_attached += ['Python']

some_lecturer_2 = Lecturer('Elena', 'Nikitina')
some_lecturer_2.courses_attached += ['Java']
some_lecturer_2.courses_attached += ['Git']

some_lecturer_3 = Lecturer('Oleg', 'Sidorov')
some_lecturer_3.courses_attached += ['Python']





some_reviewer_1 = Reviewer('Some', 'Buddy')
some_reviewer_1.courses_attached += ['Python']
some_reviewer_1.courses_attached += ['Java']

some_reviewer_2 = Reviewer('Olga', 'Sokolova')
some_reviewer_2.courses_attached += ['Python']
some_reviewer_2.courses_attached += ['Java']
some_reviewer_2.courses_attached += ['Git']




stud_1 = Student('Ruoy', 'Eman')
stud_1.courses_in_progress += ['Python']
stud_1.courses_in_progress += ['Git']
stud_1.finished_courses += ['Введение в программирование']

stud_2 = Student('Rezeda', 'Zaripova')
stud_2.courses_in_progress += ['Python']
stud_2.finished_courses += ['Web-разработка']

stud_3 = Student('Ivan', 'Ivanov')
stud_3.courses_in_progress += ['Java']
stud_3.finished_courses += ['Web-разработка']

stud_4 = Student('Petr', 'Petrov')
stud_4.courses_in_progress += ['Git']
stud_4.finished_courses += ['Введение в программирование']




stud_1.rate_hw(some_lecturer_1, 'Python', 10)
stud_1.rate_hw(some_lecturer_1, 'Python', 9)
stud_1.rate_hw(some_lecturer_1, 'Python', 10)

stud_1.rate_hw(some_lecturer_2, 'Git', 9)
stud_1.rate_hw(some_lecturer_2, 'Git', 8)
stud_1.rate_hw(some_lecturer_2, 'Git', 7)

stud_2.rate_hw(some_lecturer_1, 'Python', 9)
stud_2.rate_hw(some_lecturer_1, 'Python', 8)
stud_2.rate_hw(some_lecturer_1, 'Python', 9)

stud_2.rate_hw(some_lecturer_3, 'Python', 9)
stud_2.rate_hw(some_lecturer_3, 'Python', 6)
stud_2.rate_hw(some_lecturer_3, 'Python', 7)

stud_3.rate_hw(some_lecturer_2, 'Java', 9)
stud_3.rate_hw(some_lecturer_2, 'Java', 8)
stud_3.rate_hw(some_lecturer_2, 'Java', 9)

stud_4.rate_hw(some_lecturer_2, 'Git', 10)
stud_4.rate_hw(some_lecturer_2, 'Git', 8)
stud_4.rate_hw(some_lecturer_2, 'Git', 9)






some_reviewer_1.rate_hw(stud_1, 'Python', 10)
some_reviewer_1.rate_hw(stud_1, 'Python', 9.5)
some_reviewer_1.rate_hw(stud_1, 'Python', 10)
some_reviewer_1.rate_hw(stud_1, 'Python', 10)
some_reviewer_1.rate_hw(stud_1, 'Python', 10)

some_reviewer_2.rate_hw(stud_2, 'Python', 8)
some_reviewer_2.rate_hw(stud_2, 'Python', 7)
some_reviewer_2.rate_hw(stud_2, 'Python', 9)

some_reviewer_2.rate_hw(stud_3, 'Java', 8)
some_reviewer_2.rate_hw(stud_3, 'Java', 7)
some_reviewer_2.rate_hw(stud_3, 'Java', 9)
some_reviewer_2.rate_hw(stud_3, 'Java', 8)
some_reviewer_2.rate_hw(stud_3, 'Java', 7)
some_reviewer_2.rate_hw(stud_3, 'Java', 9)


some_reviewer_2.rate_hw(stud_4, 'Git', 10)
some_reviewer_2.rate_hw(stud_4, 'Git', 7)
some_reviewer_2.rate_hw(stud_4, 'Git', 9)


print(f'Перечень студентов:\n\n{stud_1}\n\n{stud_2}\n\n{stud_3}\n\n{stud_4}')
print()
print()


print(f'Перечень лекторов:\n\n{some_lecturer_1}\n\n{some_lecturer_2}\n\n{some_lecturer_3}')
print()
print()

print(f'Перечень проверяющих:\n\n{some_reviewer_1}\n\n{some_reviewer_2}')
print()
print()


print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{stud_1.name} {stud_1.surname} > {stud_2.name} {stud_2.surname} = {stud_1 < stud_2}')
print()


print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{some_lecturer_1.name} {some_lecturer_1.surname} < {some_lecturer_2.name} {some_lecturer_2.surname} = {some_lecturer_1 > some_lecturer_2}')
print()




student_list = [stud_1, stud_2, stud_3, stud_4]
lecturer_list = [some_lecturer_1, some_lecturer_2, some_lecturer_3]

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()