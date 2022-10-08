from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def Login():
    if request.method=='POST':
        user=request.form['username']
        password=request.form['password']
        return redirect (url_for('hello_world',name=user))
                         
    if request.method=='GET':
        return render_template('login.html')

@app.route('/hello/<name>')
def hello_world(name):
	return render_template('home.html',username=name)

@app.route('/admin')
def admin():
    return render_template('index.html')

@app.route('/user/<name>')
def hello_user(name):
    if name=='admin':
        return redirect (url_for('admin'))
    else:
        return redirect (url_for('hello_world',name=name))

@app.route('/page/<int:postID>')
def page(postID):
    return render_template('page.html',page=postID)
    


@app.route('/register')
def Register():
    return 'Registration page'



if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
	
