#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, jsonify
import sqlite3
conn = sqlite3.connect('dhamma.db3', check_same_thread=False)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

app = Flask(__name__)

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def index():
    cur.execute("SELECT * FROM centers")
    retreats_info = cur.fetchall()
    return render_template('index.html', len=2, retreats=retreats_info)


@app.route('/retreats')
def retreats():
    return render_template('retreats.html')


if __name__ == "__main__":
    app.run(debug=True)
