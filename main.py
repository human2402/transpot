from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from transport_task import solveTrans

app = Flask(__name__)
CORS(app)

# Route to serve the static HTML file
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Route to handle the POST request with JSON data
@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    print("Received JSON array:")
    print(data)
    # You can process the data here
    # For now, let's just send back a confirmation message
    response = jsonify({"message": "Received the matrix successfully!"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)