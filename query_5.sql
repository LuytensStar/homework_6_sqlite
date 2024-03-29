select subject_name
from subjects
join teachers ON teachers.id = subjects.teacher_id
where teachers.teacher_name = 'Jason Sloan'
