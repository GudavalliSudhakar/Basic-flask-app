from flask import Flask
import pymysql
app = Flask(__name__)

db_config ={
    'host': 'localhost',
    'database': 'flask',
    'user': 'root',
    'password': '984984'
}

@app.route("/")
def landing1():
    return "ABC"


@app.route("/senddata")
def senddata():
    try:
        with pymysql.connect(**db_config) as conn:
            with  conn.cursor() as cursor:
                rollno = int(input("Enter roll number: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                q = "INSERT INTO SAMPLE VALUES (%s,%s,%s)"
                cursor.execute(q,(rollno,name,age))
                conn.commit()
    except:
        return "Some random error Occured !"
    else:
        return "Data Inserted Successfully"


@app.route("/fetchdata")
def fetchdata():
    try:
        with pymysql.connect(**db_config) as conn:
            with  conn.cursor() as cursor:
                q = "SELECT * FROM SAMPLE"
                cursor.execute(q,)
                rows = cursor.fetchall()
                print(rows)
                conn.commit()
                cursor.close()
                conn.close()
    except:
        return "Some random error Occured !"
    else:
        return "Data fetch Successfully"

if __name__ == '__main__':
    app.run(debug=True)
