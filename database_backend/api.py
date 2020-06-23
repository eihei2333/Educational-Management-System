from flask import Flask,url_for,request,render_template,make_response,jsonify
import json
app = Flask(__name__)

# 跨域支持
token_list=["student","admin","teacher"]

# def after_request(resp):
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     return resp
# @app.after_request(after_request)

from flask_cors import CORS
CORS(app, resources=r'/*')
@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        data=json.loads(request.data)
        # print(data)
        # print(data["username"])

        if data["username"] == 'admin':
            token=data["username"]+" "+data["identification"]
            res={"code":20000,"data":{"token":token}}
            token_list.append(token)
            return jsonify(res)
        else:
            return 'No such user!'

@app.route('/getInfo',methods=['GET'])
def getInfo():
    print(json.dumps(request.args) )
    if request.method == 'GET':
        data=json.loads(json.dumps(request.args))
        print(data)
        print(data["token"])

        if data["token"] in token_list:
            data = {
                    "roles": ['admin'],
                    "introduction": 'I am a super administrator',
                    "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                    "name": 'Super Admin'
                    }
            res={"data":data,"code":20000}
            return jsonify(res)
        else:
            return 'No such user!'

if  __name__  ==  '__main__':

    app.run(host='127.0.0.1',  debug=True)
