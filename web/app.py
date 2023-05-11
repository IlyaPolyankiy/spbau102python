#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
from flask import Flask, request
from gauss import vector_gauss, array

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def root():
    if request.method == 'GET':
        data = request.args.get('data')
        if data == None:
            answ = ""
        else:
            try:
                data = data.split('\r\n')
                a = []
                for line in data[:-1]:
                    a.append([float(i) for i in line.split()])
                a = array(a)
                b = array([float(i) for i in array(data[-1].split())])
                answ = vector_gauss(a, b)
            except:
                answ = "Incorrect data"
           
    return flask.render_template(
        'gauss.html',
        answer = answ)

if __name__ == '__main__':
   app.run(debug = True)
