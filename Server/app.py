from flask import Flask,request, jsonify
import SparkApi as SparkApi

#以下密钥信息从控制台获取
appid = "35122103"     #填写控制台中获取的 APPID 信息
api_secret = "ZDdjZWIyMmFhZjNjY2Q2YjkzNGQ5ZWE2"   #填写控制台中获取的 APISecret 信息
api_key ="ecd2035adc843cae2ab6909b39994aa5"    #填写控制台中获取的 APIKey 信息

#用于配置大模型版本，默认“general/generalv2”
domain = "generalv3"   # v1.5版本
#云端环境的服务地址
Spark_url = "wss://spark-api.xf-yun.com/v3.1/chat"  # v1.5环境的地址

#Flask server
app = Flask(__name__)
@app.route('/')
def index():
    req = []

    jsoncon_system = {}
    jsoncon_system["role"] = "system"
    jsoncon_system["content"] = "你是一个虚拟助手，你擅长解决问题并提供简洁的回复，最长的回复不超过100字。"
    req.append(jsoncon_system)

    jsoncon_user = {}
    jsoncon_user["role"] = "user"
    user_query = request.args.get('query', 'No question provided')
    jsoncon_user["content"] = user_query
    req.append(jsoncon_user)

    response = SparkApi.request(appid,api_key,api_secret,Spark_url,domain,req)
    return jsonify({"response": response})
    


if __name__ == '__main__': 
    app.run(port=8000, host='0.0.0.0')