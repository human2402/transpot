from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import json

from transport_task import solveTrans

app = Flask(__name__, template_folder=".\\static", static_folder=".\\static")
CORS(app)

# Route to serve the static HTML file
@app.route('/')
def index():
    return render_template("index.html")#send_from_directory('static', 'index.html')

# Route to handle the POST request with JSON data
@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    print("Received JSON array:")
    
    result = solveTrans(data['priceMatrix'], data['B'], data["A"])
    # print(jsonDict)
    # You can process the data here
    # For now, let's just send back a confirmation message
    # response = jsonify({"message": "Received the matrix successfully!"})
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True, host="192.168.0.200", port="5000")