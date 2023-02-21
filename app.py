from flask import Flask, redirect, url_for, request, render_template
import sqlite3
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def root():
    return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home():
    conn = get_db_connection()
    songs = conn.execute('SELECT * FROM songs').fetchall()
    conn.close()
    return render_template("home.html",songs=songs)

@app.route('/player/<id>', methods=['GET'])
def player(id):
    return render_template("player.html",id=id)

@app.route('/upload')
def upload():
    return render_template("upload.html")
# main driver function
if __name__ == '__main__':

    app.run()