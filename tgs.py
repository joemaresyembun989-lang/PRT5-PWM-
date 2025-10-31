from flask import Flask, jsonify, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskmysql'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()

    users = []
    for row in data:
        users.append({
            'id': row[0],
            'username': row[1],
            'password': row[2],
            'email': row[3],
            'alamat': row[4],
            'no_tlpn': row[5]
        })

    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
