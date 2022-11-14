-- SELECT course_name, teacher.name AS teacher_name, classes.time, classes.number_enrolled, classes.capacity
-- FROM enrollment, classes, student, teacher
-- WHERE enrollment.classes_id = classes.id
-- AND student.id = enrollment.student_id
-- AND teacher.id = classes.teacher_ID
-- AND student.name = "Ryan Chazen"

-- SELECT course_name, teacher.name, classes.time, classes.number_enrolled, classes.capacity
-- FROM  classes, teacher
-- WHERE teacher.id = classes.teacher_ID

-- SELECT course_name, teacher.name, classes.time, classes.number_enrolled, classes.capacity
-- FROM  classes, teacher
-- WHERE teacher.id = classes.teacher_ID
-- AND teacher_ID = 1

-- SELECT student.name, enrollment.grade
-- FROM student, enrollment, classes
-- WHERE student.id = enrollment.student_id
-- AND classes.id = enrollment.class_id
-- AND classes.id = 2

-- SELECT student.name, classes.course_name
-- FROM student, enrollment, classes
-- WHERE student.id = enrollment.student_id
-- AND classes.id = enrollment.classes_id
-- AND classes.id = 3

SELECT course_name, teacher.name, classes.time, classes.number_enrolled, classes.capacity, classes.id
FROM  classes, teacher
WHERE teacher.id = classes.teacher_ID



