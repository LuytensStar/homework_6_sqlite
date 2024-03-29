select student_name, grade
from students
join groups on students.group_id = groups.id
join grades on students.id = grades.student_id
join subjects on grades.subject_id = subjects.id
where groups.group_name = 'bar' and subjects.subject_name = 'hope'