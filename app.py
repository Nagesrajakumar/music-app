from flask import Flask, flash, jsonify, redirect, send_file, url_for, request, render_template
from flask_cors import CORS
import sqlite3
import os
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '12345'
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def root():
    return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home():
    search_string = request.args.get("search", default="", type=str)
    conn = get_db_connection()
    songs = conn.execute('SELECT * FROM songs').fetchall()
    conn.close()
    filtered_songs = filter(lambda song: search_string in song['title'] or search_string in song['artist'] or search_string in song['album'], songs)
    return render_template("home.html",songs=filtered_songs, search_string=search_string)

@app.route('/player/<id>', methods=['GET'])
def player(id):
    try:
        return send_file(str(id)+'.mp3')
    except Exception as e:
        return str(e)
    #return render_template("player.html",id=id)
@app.route('/delete/<id>',methods=['GET'])
def delete_song(id):
    conn = get_db_connection()
    delete_query = 'DELETE FROM songs WHERE id=?'
    cur = conn.cursor()
    cur.execute(delete_query, (id,))
    os.remove(str(id)+".mp3")
    conn.commit()
    return redirect(url_for('home'))
@app.route('/upload', methods=['GET','POST'])
def upload():
    if(request.method == 'POST'):
        title = request.form['title']
        artist = request.form['artist']
        album = request.form['album']
        if not title:
            response = jsonify("Title cannot be empty")
            return response;
        elif not artist:
            response = jsonify("Artist name cannot be empty")
            return response;
        elif not album:
            response = jsonify("Album cannot be empty")
            return response
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO songs (title,artist,album) VALUES (?, ?, ?) RETURNING id',(title,artist,album))
            row = cursor.fetchone()
            (inserted_id, ) = row if row else None
            file = request.files['file']
            print(file)
            if(file.filename != ""):
                file.save(str(inserted_id)+".mp3")

            response = jsonify("File received and saved!")
            response.headers.add('Access-Control-Allow-Origin', '*')
            conn.commit()
            conn.close()
            return response
    if(request.method):
        return render_template("upload.html")
# main driver function
if __name__ == '__main__':

    app.run()