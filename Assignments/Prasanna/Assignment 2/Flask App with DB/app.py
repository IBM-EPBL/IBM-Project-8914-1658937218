from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #fetch user data
        studentDetails = request.form
        name = studentDetails['name']
        email = studentDetails['email']

        try:
            with sql.connect("student_database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,email) VALUES (?,?)",(name,email) )
                con.commit()
                msg = "Record successfully added!"
        except:
            con.rollback()
            msg = "Error in INSERT Operation"
        finally:
            return msg;
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)