from flask import Flask, request, jsonify, send_from_directory, render_template, url_for, redirect
from flask_cors import CORS
import json
import traceback

# from transport_task import solveTrans
from transport_task1 import solveTrans
from task_rewrite import solveTask

app = Flask(__name__, template_folder=".\\static", static_folder=".\\static")
CORS(app)

# Route to serve the static HTML file
@app.route('/')
def index():
    with app.test_request_context():
        return redirect(url_for('static', filename='index.html'))
    # return render_template("index.html")#send_from_directory('static', 'index.html')

# Route to handle the POST request with JSON data
@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    print("Received JSON array:")
    print(data['priceMatrix'])
    print (data['B'], data["A"])
    # result = solveTrans(data['priceMatrix'], data['B'], data["A"])
    result = solveTask(data['priceMatrix'], data['B'], data["A"])
    print (result)
    # result = {}
    # try:
    # # Your code here
    #     result = solveTrans(data['priceMatrix'], data['B'], data["A"])
    # except Exception as e:
    #     result = {
    #         "error": str(e),
    #         "tracebacK": traceback.print_exc()
    #     }
    #     print(traceback.print_exc())

    
    
    # print(jsonDict)
    # You can process the data here
    # For now, let's just send back a confirmation message
    # response = jsonify({"message": "Received the matrix successfully!"})
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5099", debug=True)
