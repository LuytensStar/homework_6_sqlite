select student_name , grade
from students
join groups on students.group_id = groups.id
join grades on grades.student_id = students.id
join subjects on grades.subject_id = subjects.id
WHERE groups.group_name = 'bar' AND subjects.subject_name = 'hope' AND grades.grade_date = '2024-03-28'