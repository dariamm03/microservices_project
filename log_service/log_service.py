from flask import Flask, request, jsonify

app = Flask(__name__)

logs = []

@app.route('/api/logs', methods=['POST'])
def create_log():
    data = request.json
    logs.append(data)
    return jsonify({"message": "Log created"}), 201

@app.route('/api/logs', methods=['GET'])
def get_logs():
    return jsonify(logs), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
