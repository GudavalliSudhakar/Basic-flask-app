from flask import Flask,render_template,request
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
verifyotp ="0"
app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("home.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/registerdata",methods=["POST","GET"])
def registerdata():
    if request.method == "POST":
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        mobile = request.form['mobile']
        password = request.form['password']
        cpassword = request.form['confirm-password']
        if password == cpassword:
            otp = random.randint(111111,999999)
            global verifyotp
            verifyotp = str(otp)
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            sender_email = "20bec016@iiitdwd.ac.in"  
            sender_password = "klni qbip xops nxki"
            from_email = "20bec016@iiitdwd.ac.in" 
            to_email = email
            subject = "otp for verification"
            body = f"The otp for login is {verifyotp}"


            message = MIMEMultipart()
            message["From"] = from_email
            message["To"] = to_email
            message["Subject"] = subject
            message.attach(MIMEText(body,'plain'))

            server= smtplib.SMTP(smtp_server, smtp_port)
            server.starttls() 
            server.login(sender_email, sender_password)
            server.send_message(message)
            server.quit()
            return render_template("verifyemail.html",name=name,username=username,email=email,mobile=mobile,password=password)
        else:
            return "Make sure password and confirm password to be same"
    else:
        return "<h3 style='color:red'>Data got in wrong manner</h3>"
    

@app.route("/verifyemail",methods=["POST","GET"])
def verifyemail():
    if request.method =="POST":
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        mobile = request.form['mobile']
        password = request.form['password']
        otp = request.form['otp']
        if otp==verifyotp:
            return "correct otp"
        else:
            return "Wrong otp"
    else:
        return "<h3 style='color:red'>Data got in wrong manner</h3>"


if __name__ == "__main__":
    app.run()