select student_name
from students
join groups on groups.id = students.group_id
where groups.group_name = ''