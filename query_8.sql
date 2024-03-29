select avg(grade) as average_grade
from grades
join teachers on teachers.id = subjects.teacher_id
join subjects on subjects.teacher_id = subjects.id
where teachers.teacher_name = 'Jason Sloan'