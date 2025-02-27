from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/notify', methods=['POST'])
def notify_user():
    data = request.json
    # Здесь может быть логика по отправке уведомлений
    return jsonify({"message": "Notification sent"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
