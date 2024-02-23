from flask import Flask, request, jsonify
from flask_cors import CORS
import socket
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/post_endpoint', methods=['POST'])
def handle_post_request():
    if request.method == 'POST':
        data = request.json  # Assuming the incoming data is in JSON format
        title = data.get("title", None)  # Extract the "title" from the data
        print("Received title:", title)


        import time 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 8585 ))
        s.listen(0)                 
        
        while True:
            client, addr = s.accept()
            client.settimeout(5)
            while True:
                content = client.recv(1024)
                if len(content) ==0:
                    break
                if str(content,'utf-8') == '\r\n':
                    continue
                else:
                    print(str(content,'utf-8'))
                    client.send(title.encode('utf-8'))
                    break
            client.close()







        # Do something with the title, for example, save it to a variable or database

        response_data = {"message": "POST request received successfully"}

        return jsonify(response_data), 200

    else:
        return "Invalid request method", 400

if __name__ == '__main__':
    app.run(debug=True)
