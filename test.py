from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='artgallery'

mysql = MySQL(app)
    
@app.route('/')
def root():
    return render_template('index.html')

@app.route('/display',methods=['GET', 'POST'])
def display():
    if request.method == "POST":
        details = request.form
        state = details['stateAb']
        cur = mysql.connection.cursor()
        cur.execute("SELECT C.* FROM CUSTOMER AS C, STATE AS S WHERE S.stateAb=C.stateAb AND S.stateAb='"+state+"'")
        result = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return render_template('display.html',result= result)

@app.route('/insert', methods = ['GET', 'POST'])
def insert():
    if request.method == "POST":
        details = request.form
        stateab = details['stateab']
        state = details['statename']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO state(stateAb, stateName) VALUES(%s, %s)",(stateab, state))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        details = request.form
        stateab = details['stateab']
        state = details['statename']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE state SET stateAb='"+stateab+"' WHERE stateName='"+state+"'")
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    if request.method == 'POST':
        details = request.form
        state = details['statename']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM state WHERE stateName='"+state+"'")
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

