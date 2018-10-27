import pymysql

from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/add', methods=['POST'])
def add_user():
    try:
        data = request.json
        name = data['name']
        email = data['email']
        pwd = data['pwd']
        if name and email and pwd and request.method == 'POST':
            sql = "INSERT INTO user_table(user_name, user_email, user_password) VALUES(%s, %s, %s)"
            data = (name, email, pwd)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/list')
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user_table")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/user/<id>')
def user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user_table WHERE user_id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['POST'])
def update_user():
    try:
        data = request.json
        id = data['id']
        name = data['name']
        email = data['email']
        pwd = data['pwd']
        if name and email and pwd and _id and request.method == 'POST':
            # save edits
            sql = "UPDATE user_table SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
            data = (name, email, pwd, id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete/')
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user_table WHERE user_id=%s", (id,))
        conn.commit()
        resp = jsonify('User deleted!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run()
