from flask import Flask,request, jsonify
import SparkApi as SparkApi
from MoonShotApi import MoonShotAI
from SparkApi import SparkAI

#Flask server
app = Flask(__name__)

# Use Spark LLM
@app.route('/Spark',methods=['GET', 'POST'])
def Spark_callback():
    data = request.get_json(silent=True)
    query = data['query']
    Spark_client = SparkAI()
    response = Spark_client.chat_once(query)
    return jsonify({"response": response})


# Use MoonShot LLM -- - Kimi
@app.route('/MoonShot',methods=['GET', 'POST'])
def MoonShot_callback():
    data = request.get_json(silent=True)
    query = data['query']
    moonShot_client = MoonShotAI()
    response = moonShot_client.chat_once(query)
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')