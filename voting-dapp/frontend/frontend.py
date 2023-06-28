from flask import Flask,render_template,request,redirect,session
import urllib3 

app=Flask(__name__)
app.secret_key='makeskilled'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registerform',methods=['get','post'])
def registerform():
    username=request.form['username']
    password=request.form['password']
    print(username,password)
    http=urllib3.PoolManager()
    response=http.request('get','http://127.0.0.1:5001/signup?username='+str(username)+'&password='+password)
    data=response.data.decode('utf-8')
    if(data=='Account Created'):
        return render_template('register.html',res='Account Registered')
    else:
        return render_template('register.html',err='Account Exist')

@app.route('/loginform',methods=['post','get'])
def loginform():
    username=request.form['username']
    password=request.form['password']
    print(username,password)
    http=urllib3.PoolManager()
    response=http.request('get','http://127.0.0.1:5001/login?username='+str(username)+'&password='+password)
    data=response.data.decode('utf-8')
    if(data=='False'):
        return render_template('login.html',err='Invalid Credentials')
    else:
        session['username']=username
        return redirect('/votepage')

@app.route('/votepage')
def votepage():
    return render_template('voting.html')

@app.route('/logout')
def logout():
    session['username']=None
    return redirect('/')

@app.route('/vote/<id>')
def vote(id):
    wallet=session['username']
    http=urllib3.PoolManager()
    response=http.request('get','http://127.0.0.1:5001/castvote?id='+id+'&wallet='+wallet)
    data=response.data.decode('utf-8')
    if (data=='You have already voted'):
        return render_template('voting.html',err='You have already casted your vote')
    else:
        return render_template('voting.html',res='You have voted')

@app.route('/results')
def results():
    http=urllib3.PoolManager()
    response=http.request('get','http://127.0.0.1:5001/displayvotes?wallet='+session['username'])
    data=response.data.decode('utf-8')
    data=data.split(',')
    return render_template('results.html',v0=data[0][1:],v1=data[1],v2=data[2][:-1])

if __name__=="__main__":
    app.run(
        host='0.0.0.0',
        port=5002,
        debug=True
    )