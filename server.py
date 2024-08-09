from flask import Flask, render_template, request, jsonify
import json
from solver import *

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.json # Get the json in dictionary format
            cnf = encode_sudoku(data)
            raw = solve_sudoku(cnf)
            sol = decode_sudoku(raw)
            return jsonify(sol)
    else:
        return render_template('index.html')
    