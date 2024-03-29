SELECT group_name, AVG(grade) as average_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.subject_name = 'hope'
GROUP BY group_name
