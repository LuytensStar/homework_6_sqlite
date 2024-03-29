select avg(grade) as average_grade
from grades
join students on grades.student_id =students.id
join teachers on subjects.teacher_id = teachers.id
join subjects on grades.subject_id = subjects.id
where teachers.teacher_name = 'Andrea Lucero' and students.student_name = 'Angelica Martinez'