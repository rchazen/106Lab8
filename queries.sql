-- SELECT course_name, teacher.name AS teacher_name, classes.time, classes.number_enrolled, classes.capacity
-- FROM enrollment, classes, student, teacher
-- WHERE enrollment.class_id = classes.id
-- AND student.id = enrollment.student_id
-- AND teacher.id = classes.teacher_ID
-- AND student.name = "Eduardo"

-- SELECT course_name, teacher.name, classes.time, classes.number_enrolled, classes.capacity
-- FROM  classes, teacher
-- WHERE teacher.id = classes.teacher_ID

-- SELECT course_name, teacher.name, classes.time, classes.number_enrolled, classes.capacity
-- FROM  classes, teacher
-- WHERE teacher.id = classes.teacher_ID
-- AND teacher_ID = 1

SELECT student.name, enrollment.grade
FROM student, enrollment, classes
WHERE student.id = enrollment.student_id
AND classes.id = enrollment.class_id
AND classes.id = 2


