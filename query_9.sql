select subject_name
from subjects
join grades on subjects.id = grades.subject_id
join students on grades.student_id = students.id
where student_name = 'Thomas Byrd'
group by subject_name