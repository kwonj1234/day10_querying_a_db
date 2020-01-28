## SQL Joins

If I have courses and students and students are in many courses and courses have many students a table layout might look like:

```
CREATE TABLE students (
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255)
    );

CREATE TABLE courses (
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(32)
    );

CREATE TABLE students_courses (
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    students_pk INTEGER,
    courses_pk INTEGER
    FOREIGN KEY(students_pk) REFERENCES(students.pk),
    FOREIGN KEY(courses_pk) REFERENCES(courses.pk)
    );
```

Where if student S with pk=5 is in course C with pk=10, there will be a row in `students_courses` where `students_pk` = 5 and `courses_pk` = 10

To select across these connections you SELECT on the three tables JOINED together

To see all pairs of course titles and student names where a student is taking that course you would use the command:

```
SELECT students.name, courses.title FROM courses JOIN students_courses ON courses.pk = students_courses.courses_pk JOIN students ON students.pk = students_courses.students_pk;
```

To see all courses Carter is taking you would use

```
SELECT students.name, courses.title FROM courses JOIN students_courses ON courses.pk = students_courses.courses_pk JOIN students ON students.pk = students_courses.students_pk WHERE students.name = 'Carter';
```

the first part of the join, `courses JOIN students_courses ON courses.pk = students_courses.courses_pk` looks at elements of the courses table paired with elements of the students_courses table where the students_courses entry is referencing that course.

the second part of the join, `... JOIN students ON students.pk = students_courses.students_pk` now looks at the elements of that first join combined with the values of the students table where the students_pk element of students_courses is equal to a student's pk.

this produces a virtual table that has all the columns from all three tables for every pairing of students and courses that has an entry in students_courses. you can then select specific columns based on WHERE clauses from that virtual table.
