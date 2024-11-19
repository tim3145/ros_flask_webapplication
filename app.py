from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from threading import Thread
from ros_node import ROS2Node, ros2_runner  # ROS 2 관련 코드 가져오기

# Flask 앱 초기화
app = Flask(__name__)
socketio = SocketIO(app)

# REST API 엔드포인트
@app.route('/send_command', methods=['POST'])
def send_command():
    command = request.json.get('command')
    if command:
        ros_node.publish_command(command)
        return jsonify({"status": "success", "command": command}), 200
    return jsonify({"status": "failure", "message": "Invalid command"}), 400

@app.route('/get_latest_message', methods=['GET'])
def get_latest_message():
    return jsonify({"latest_message": ros_node.latest_message}), 200

# WebSocket 이벤트
@socketio.on('connect')
def on_connect():
    print("Client connected")

@socketio.on('disconnect')
def on_disconnect():
    print("Client disconnected")

if __name__ == '__main__':
    # ROS 2 실행 스레드 시작
    ros_thread = Thread(target=ros2_runner, daemon=True)
    ros_thread.start()

    # Flask-SocketIO 실행
    socketio.run(app, host='0.0.0.0', port=5000)

