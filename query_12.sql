with last_date as( 
    select max(grade_date) as max_date
    from grades
    join students on grades.student_id = students.id
    join groups on grades.group_id = groups.id
    join subjects on grades.subject_id =subjects.id
    where groups.group_name = 'bar' and subjects.subject_name ='hope' 
) 
select student_name , grade
from students
join groups on students.group_id = groups.id
join grades on grades.student_id = students.id
join subjects on grades.subject_id = subjects.id
WHERE students.group_id IN (
    SELECT id FROM groups WHERE group_name = 'bar'
)
AND grades.subject_id IN (
    SELECT id FROM subjects WHERE subject_name = 'hope'
)
ORDER BY students.student_name;

