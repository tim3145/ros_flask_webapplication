// WebSocket 연결
const socket = io.connect('http://localhost:5000');

// ROS 데이터 수신
socket.on('ros_data', (data) => {
    console.log("Received ROS data:", data.data);
    document.getElementById("rosData").innerText = data.data;
});

// 명령 전송
function sendCommand() {
    const command = document.getElementById("commandInput").value;
    fetch('/send_command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ command })
    }).then(response => response.json())
      .then(data => console.log("Command response:", data));
}

