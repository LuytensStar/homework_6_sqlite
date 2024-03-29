select subject_name
from subjects
join teachers on subjects.teacher_id = teachers.id
join grades on grades.subject_id = subjects.id
join students on grades.student_id = students.id
where students.student_name = 'Angelica Martinez' and teachers.teacher_name  = 'Andrea Lucero'