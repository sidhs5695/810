from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route('/summary')
def instructor_summary():
    db_path = r"C:\Users\12012\Desktop\Python\810\Hw11.db"
    try:
        db = sqlite3.connect(db_path)
    except sqlite3.OperationalError as oe:
        print(oe)
    else:
        query = """select s.Name, s.CWID, g.Course,  g.Grade, i.Name from students s join grades g on s.CWID=StudentCWID join instructors i on InstructorCWID=i.CWID order by s.Name"""

        data = [{"cwid": cwid, "name": name, "courses": courses, "grade": grade,"instructor":instructor} for name, cwid, courses, grade, instructor in db.execute(query)]
        print(data)
        db.close()

    return render_template(
        'instructor-summary.html',
        title="Stevens Repository",
        table_title="Courses, Courses, Grades and Instructors",
        students=data)


app.run(debug=False)