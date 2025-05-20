# app.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

destination_coords = {'destination':{'latDest':None, 'lngDest':None}}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/receive', methods=['POST'])
def receive_data():
    global destination_coords
    destination_coords = request.get_json(force=True, silent=True)
    latDest, lngDest = destination_coords['destination'].values()
    print(f"[INFO] Received data: {destination_coords}")
    return jsonify({"status": "success", "received": destination_coords}), 200

def run_server():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
