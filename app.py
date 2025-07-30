from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

# Replace with your Railway DB credentials
db = mysql.connector.connect(
    host="mysql.railway.internal",
    user="root",
    password="pfmqLhKJDRVoAXnkUwHnjhcHvDlQqMvT",
    database="railway",
    port=3306
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        return redirect('/')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        if user:
            return "Login successful!"
        else:
            return "Login failed!"
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


