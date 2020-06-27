from flask import Flask,url_for,request,render_template,make_response,jsonify
from database import *
from flask_cors import CORS
import json
import admin
import student
import teacher
app = Flask(__name__)

# 跨域支持
token_list=["student","admin","teacher"]
def right_res(data):
    res = {"data": data, "code": 20000}
    return jsonify(res)
def wrong_res(data):
    res = {"message": data, "code": 20001}
    return jsonify(res)
# def after_request(resp):
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     return resp
# @app.after_request(after_request)


CORS(app, resources=r'/*')
@app.route('/login',methods=['POST'])
def Login():
    if request.method == 'POST':
        data=json.loads(request.data)
        print(data["username"],data["password"],data["identification"])
        usr,pwd,type=data["username"],data["password"],data["identification"]
        print(str(usr),str(pwd),str(type))
        if login(data["username"],data["password"],data["identification"])==0:
            token=data["username"]
            res={"code":20000,"data":{"token":token}}
            token_list.append(token)
            return jsonify(res)
        if login(data["username"],data["password"],data["identification"])==1:
            res={"code":20001,"message":"密码错误"}
            return jsonify(res)
        if login(data["username"], data["password"], data["identification"]) == 2:
            res={"code":20002,"message":"用户不存在"}
            return jsonify(res)

@app.route('/getInfo',methods=['GET'])
def getInfo():
    print(json.dumps(request.args) )
    if request.method == 'GET':
        data=json.loads(json.dumps(request.args))
        print(data)
        if data["token"] in token_list:
            print(data["token"])
            data = {
                    "roles": ['admin'],
                    "introduction": 'I am a super administrator',
                    "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                    "name": 'Super Admin'
                    }
            return right_res(data)
        else:
            return 'No such user!'

@app.route('/getTerm',methods=['GET'])
def getTerm():
    print(json.dumps(request.args) )
    if request.method == 'GET':
        data=json.loads(json.dumps(request.args))
        # print(data)
        # print(data["token"])
        term = []
        tmp = searchOnInfo(flag="1")
        for item in tmp:
            if item[2] not in term:
                term.append(item[2])
        tmp = searchOnInfo(flag="0")
        for item in tmp:
            if item[2] not in term:
                term.append(item[2])
        if data["token"] in token_list:
            data = {"terms":term}
            return right_res(data)

@app.route('/getCollege',methods=['GET'])
def getCollege():
    print(json.dumps(request.args) )
    if request.method == 'GET':
        data=json.loads(json.dumps(request.args))
        print(data)
        print(data["token"])
        college = []
        tmp = searchAll('D')
        for item in tmp:
            college.append({'yxh': item[0], 'display_name': item[1]})
        if data["token"] in token_list:
            data = {"college":college}
            return right_res(data)
# { yxh: '000', display_name: '计算机' }
@app.route('/changePassword',methods=['POST'])
def changePassword():
    print(json.dumps(request.args) )
    data = json.loads(request.data)
    if updatePwd(data["usr"],data["pwd"])[0]:
        return right_res("修改成功")
    else:
        return wrong_res("修改失败")
    return right_res(updatePwd(data["usr"],data["pwd"])[0])

@app.route('/admin/setSx',methods=['POST'])
def adminupdatexf():
    if request.method == 'POST':
        data=json.loads(request.data)
        print(data)
        # print(data["term"],data["xy"],data["xf"])
        k = admin.updatexf(data["term"],data["xy"],data["xf"])
        if k == 0:
            return right_res("修改成功")

@app.route('/admin/getCourseByTerm',methods=['POST'])
def admingetCourseByTerm():
    if request.method == 'POST':
        data=json.loads(request.data)
        print(data)
        # print(data["term"],data["xy"],data["xf"])
        if "kh" in data:
            k = admin.getCourseByTerm(data["term"],data["kh"],'')
        if "km" in data:
            k = admin.getCourseByTerm(data["term"],'',data["km"])
        else:
            k = admin.getCourseByTerm(data["term"], '', '')
        return right_res(k)


@app.route('/admin/createCourse',methods=['POST'])
def admincreateCourse():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.createCourse(data)
        if k ==1:
            return right_res("修改成功")
        else:
            return right_res("修改失败")

@app.route('/admin/createClass',methods=['POST'])
def admincreateClass():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.createClass(data)
        if k ==1:
            return right_res("修改成功")
        else:
            return right_res("修改失败")

@app.route('/admin/createStudentInClass',methods=['POST'])
def admincreateStudentInClass():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.createStudentInClass(data)
        if k ==1:
            return right_res("修改成功")
        else:
            return right_res("修改失败")

@app.route('/admin/getAllCourse',methods=['POST'])
def admingetAllCourse():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.getAllCourse(data)
        return right_res(k)
@app.route('/admin/getClass',methods=['POST'])
def admingetClass():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.getClass(data)
        return right_res(k)
@app.route('/admin/getStudent',methods=['POST'])
def admingetStudent():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.getStudent(data)
        return right_res(k)


@app.route('/admin/deletCourse',methods=['POST'])
def admindeletCourse():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.deletCourse(data)
        return right_res(k)

@app.route('/admin/deletClass',methods=['POST'])
def admindeletClass():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.deletClass(data)
        return right_res(k)

@app.route('/admin/deletStudentFromClass',methods=['POST'])
def admindeletStudentFromClass():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.deletStudentFromClass(data)
        return right_res(k)
@app.route('/admin/getAllStudent',methods=['POST'])
def admingetAllStudent():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.getAllStudent(data)
        return right_res(k)
@app.route('/admin/getAllTeacher',methods=['POST'])
def admingetAllTeacher():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.getAllTeacher(data)
        return right_res(k)
@app.route('/admin/creatTeacher',methods=['POST'])
def admincreatTeacher():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.creatTeacher(data)
        return right_res(k)
@app.route('/admin/creatStudent',methods=['POST'])
def admincreatStudent():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.creatStudent(data)
        return right_res(k)
@app.route('/admin/deleteStudent',methods=['POST'])
def admindeleteStudent():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.deleteStudent(data)
        return right_res(k)
@app.route('/admin/deleteTeacher',methods=['POST'])
def admindeleteTeacher():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = admin.deleteTeacher(data)
        return right_res(k)

@app.route('/student/getScore',methods=['POST'])
def SgetScore():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = student.getScore(data)
        return right_res(k)

@app.route('/student/getCourse',methods=['POST'])
def SgetCourse():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = student.getCourse(data)
        return right_res(k)
@app.route('/student/getSelectedCourse',methods=['POST'])
def SgetSelectedCourse():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = student.getSelectedCourse(data)
        return right_res(k)
@app.route('/student/select',methods=['POST'])
def Sselect():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = student.select(data)
        return right_res(k)

@app.route('/student/delete',methods=['POST'])
def Sdelete():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = student.delete(data)
        return right_res(k)

@app.route('/teacher/getClass',methods=['POST'])
def TgetClass():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = teacher.getClass(data)
        return right_res(k)

@app.route('/teacher/getStudent',methods=['POST'])
def TgetStudent():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = teacher.getStudent(data)
        return right_res(k)

@app.route('/teacher/updateScore',methods=['POST'])
def TupdateScore():
    if request.method == 'POST':
        data=json.loads(request.data)
        k = teacher.updateScore(data)
        return right_res(k)

if  __name__  ==  '__main__':

    app.run(host='127.0.0.1',  debug=True)
    searchOnInfo(flag=1)
