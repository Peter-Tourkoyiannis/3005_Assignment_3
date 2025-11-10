import pg8000

def connect():
    """Returns a connection to the database. """
    return pg8000.connect(user="postgres", password="postgres", host="localhost", port=5432, database="Students")

def getAllStudents():
    """ Gets all students and prints them out.
        Connect to database, get cursor to interact with database via query,
        then cleanup by closing cursor and connection. """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()

def addStudent(first_name, last_name, email, enrollment_date):
    """ Adds a student to the database.
        Connect to database, get cursor to interact with database via query,
        then cleanup by closing cursor and connection. """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s);
        """,
        (first_name, last_name, email, enrollment_date)
    )
    connection.commit()
    cursor.close()
    connection.close()

def updateStudentEmail(student_id, new_email):
    """ Updates a student email field in the database.
        Connect to database, get cursor to interact with database via query,
        then cleanup by closing cursor and connection. """
    connection = connect()
    cur = connection.cursor()
    cur.execute(
        """
        UPDATE students
        SET email = %s
        WHERE student_id = %s;
        """,
        (new_email, student_id)
    )
    connection.commit()
    cur.close()
    connection.close()

def deleteStudent(student_id):
    """ Removes a student from the database.
        Connect to database, get cursor to interact with database via query,
        then cleanup by closing cursor and connection. """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """
        DELETE FROM students
        WHERE student_id = %s;
        """,
        (student_id,)
    )
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    """ All the operations:

        getAllStudents()
        addStudent("Peter", "Tourkoyiannis", "peter.tourkoyiannis@example.com", "2025-11-09")
        updateStudentEmail(1, "doe.john@example.com")
        deleteStudent(2) """

    getAllStudents()



