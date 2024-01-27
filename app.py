from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)


# Connect to MySQL
connection = pymysql.connect(
    host='mysqldb.cd2pfftf5k62.us-east-2.rds.amazonaws.com', 
    port=3306,
    user="admin", 
    password="adminadmin", 
    database="mysqldb"
    )
cursor = connection.cursor()

# Create a table if not exists
create_table_query = '''
CREATE TABLE IF NOT EXISTS form_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255),
    username VARCHAR(255),
    fullname VARCHAR(255)
)
'''
cursor.execute(create_table_query)
connection.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        fullname = request.form['fullname']

        # Insert data into the database
        insert_query = 'INSERT INTO form_data (email, username, fullname) VALUES (%s, %s, %s)'
        cursor.execute(insert_query, (email, username, fullname))
        connection.commit()

        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
