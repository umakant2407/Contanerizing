from flask import Flask, jsonify
import time
app = Flask(__main__)

@app.route("/")
def hello():
    return jsonify({"Time of Call": time.time()})


//Calling Main function
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

