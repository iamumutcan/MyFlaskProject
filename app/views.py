from flask import Flask, render_template, redirect, url_for, request, make_response
from itsdangerous import Signer
app = Flask(__name__)
@app.route("/")
def Definition():
    # name=request.cookies.get('name')
    # print('name',name)
    signer=Signer("keyXXXX")
    signed_name=signer.sign('Can')
    response = make_response("Flask denemeesi")
    response.set_cookie('name',signed_name)
    return response

@app.route("/hello")
def Hello():
    return render_template("hello.html")

@app.route("/hello-admin")
def HelloAdmin():
    return render_template("hello-admin.html")

@app.route("/hello/<name>")
def HelloUser(name):
    if name.lower()=="admin":
        return redirect(url_for("HelloAdmin"))
    return render_template("hello-user.html",username=name)
'''
@app.route("/add/<int:number1>/<int:number2>")
def Add(number1,number2):
    return render_template("add.html",number1=number1,number2=number2)
'''
@app.route("/add")
def Add():
    number1=int(request.args["number1"])
    number2=int(request.args["number2"])
    calculation_result=number2+number1
    return render_template("add.html",number1=number1,number2=number2,calculation_result=calculation_result)

@app.route("/login",methods= ['POST','GET'])
def Login():
    if request.method=='POST':
        username = request.form["username"]
        return redirect(url_for("HelloUser", name=username))
    else:
        return render_template("login.html")

@app.route("/student")
def Student():
    return render_template("student.html")

@app.route("/result",methods=['POST'])
def Result():
    ContextData={
        'name': request.form["name"],
        'physics': request.form["physics"],
        'mathematics' : request.form["mathematics"],
        'chemistry': request.form["chemistry"]
    }

    return render_template("student_result.html",**ContextData)
