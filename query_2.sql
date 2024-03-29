SELECT student_name, avg(grade) as average_grades
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.subject_name = 'hope'
GROUP BY student_name
ORDER BY average_grades DESC
LIMIT 1