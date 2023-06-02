from flask import Flask,redirect, url_for, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("marks.html")

@app.route('/submit',methods=['POST','GET'])
def submit():
    avgerage=0
    if request.method=='POST':
        s=float(request.form['science'])
        m=float(request.form['maths'])
        c=float(request.form['chemistry'])
        ds=float(request.form['datascience'])
        average=(s+m+c+ds)
    res=""
    if average<50:
        res="Fail"
    else:
        res="Passed"
    
    return render_template("result.html",result=res)
        
        
        
    





if __name__=='__main__':
    app.run(debug=True)