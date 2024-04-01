select avg(grade) as average_grade
from grades
join teachers on subjects.teacher_id = teachers.id
join subjects on grades.subject_id = subjects.id
where teachers.teacher_name = 'Jason Sloan'