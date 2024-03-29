from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_SUBJECTS = 5
NUMBER_TEACHERS = 3
NUMBER_GRADES = 20

def generate_fake_data(number_groups, number_students, number_subjects, number_teachers, number_grades) -> tuple():
    fake_groups = []
    fake_students = []
    fake_subjects = []
    fake_teachers = []
    fake_grades = []

    fake_data = faker.Faker()

    for _ in range(number_groups):
        fake_groups.append(fake_data.word())

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.word())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_grades):
        fake_grades.append(randint(1, 5))

    return fake_groups, fake_students, fake_subjects, fake_teachers, fake_grades


fake_groups, fake_students, fake_subjects, fake_teachers, fake_grades = generate_fake_data(
                                                NUMBER_GROUPS, NUMBER_STUDENTS,
                                                NUMBER_SUBJECTS, NUMBER_TEACHERS,
                                                NUMBER_GRADES)


def prepare_data(groups,students,subjects,teachers,grades):
    for_groups = []
    for group in groups:
        for_groups.append((group, ))
    for_students = []
    for student in students:
        for_students.append((student, randint(1,NUMBER_GROUPS)))

    for_subjects = []
    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_grades = []
    for i in range(NUMBER_STUDENTS):
        for j in range(NUMBER_SUBJECTS):
            for_grades.append((i + 1, j + 1, choice(grades), datetime.now().strftime("%Y-%m-%d")))
    return for_groups, for_students,for_subjects,for_teachers,for_grades



def insert_data_to_db(groups,students,subjects,teachers,grades):
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name) VALUES (?)"""

        cur.executemany(sql_to_groups, groups)

        sql_to_students = """INSERT INTO students(student_name, group_id) VALUES (?,?)"""

        cur.executemany(sql_to_students, students)

        sql_to_teachers= """INSERT INTO teachers (teacher_name) VALUES (?)"""

        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)"""

        cur.executemany(sql_to_subjects , subjects)

        sql_to_grades = """INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_grades , grades)

        con.commit()


if __name__ == '__main__':
    groups, students, subjects, teachers, grades = prepare_data(
        *generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_SUBJECTS, NUMBER_TEACHERS, NUMBER_GRADES))
    insert_data_to_db(groups,students,subjects,teachers,grades)





# conn = sqlite3.connect('school.db')
# c = conn.cursor()
#
# # Insert the fake data into the database
# for group in fake_groups:
#     c.execute("INSERT INTO groups (group_name) VALUES (?)", (group,))
#
# for student in fake_students:
#     c.execute("INSERT INTO students (student_name, group_id) VALUES (?, ?)", (student, randint(1, NUMBER_GROUPS)))
#
# for teacher in fake_teachers:
#     c.execute("INSERT INTO teachers (teacher_name) VALUES (?)", (teacher,))
#
# for subject in fake_subjects:
#     c.execute("INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)", (subject, randint(1, NUMBER_TEACHERS)))
#
# for i in range(NUMBER_STUDENTS):
#     for j in range(NUMBER_SUBJECTS):
#         c.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)", (i+1, j+1, choice(fake_grades), datetime.now().strftime("%Y-%m-%d")))

#
# conn.commit()
# conn.close()
