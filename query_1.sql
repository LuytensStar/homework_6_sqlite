SELECT student_name, AVG(grade) as average_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY student_name
ORDER By average_grade DESC
LIMIT 5