import sqlite3
from flask import *


def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database Successfully")
    conn.execute("CREATE TABLE IF NOT EXISTS students(name TEXT, address TEXT, city TEXT, pin TEXT)")
    print("Table created successfully")
    conn.close()


init_sqlite_db()
app = Flask(__name__)


@app.route('/enter-new/')
def enter_new_student():
    return render_template('student.html')


@app.route('/add-new-record/', methods=['POST'])
def add_new_record():
    if request.method == "POST":
        try:
            name = request.form['name']
            address = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name, address, city, pin) VALUES (?, ?, ?, ?)", (name, address, city,
                                                                                                    pin))
                con.commit()
                msg = "Record successfully added."

        except Exception as e:
            con.rollback()
            msg = "Error occurred in insert operation: " + str(e)
        finally:
            con.close()
            return render_template('result.html', msg=msg)
