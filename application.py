from flask import Flask
app = Flask(__name__)

@app.route("/")
def landing():
    return "This is my second flask application"

@app.route("/Aboutus")
def aboutus():
    return "About Us Page"

@app.route("/contact us")
def contactus():
    return "<h1 style='color:red'> +91 6305408955 </h1>"

@app.route("/collectiondata")
def collectiondata():
    return "Enter Your name: "

@app.route("/response/<name>")
def response(name):
    print("Hello " + name)
    return f"Hello {name}"


if __name__=="__main__":
    app.run()
