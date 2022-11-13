SELECT course_name, teacher.name AS teacher_name, classes.time, classes.number_enrolled
FROM enrollment, classes, student, teacher
WHERE enrollment.class_id = classes.id
AND student.id = enrollment.student_id
AND teacher.id = classes.teacher_ID
AND student.name = "Jerry Armenta"