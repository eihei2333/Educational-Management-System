import database
from database import *
# print(insertOnUser('1101','111111',"student"))
# print(updatePwd("ss","123456"))
# print(login("ff","123456","admin"))
# print(insertOnUser('admin','111111','admin'))
# print(insertOnUser('0101','111111','teacher'))
def updatexf(term,xy,xf):
    # xy = searchOnD(isyxh=True, mc=xy)[0][0]
    if searchOnInfo(xq=term,yxh=xy):
        updateOnInfo(old_xq=term,old_yxh=xy,new_sx=xf)
    else:
        Flag=searchOnInfo(xq=term)[0][1]
        insertOnInfo(flag=Flag,xq=term,yxh=xy,sx=xf)
    return 0
def getCourseByTerm(term,kh,km):
    if kh=='' and km=='':
        tmp = list(searchOnO(iskh=True,xq=term))
        k=[]
        for item in tmp:
            if item[0] not in k:
                k.append(list(searchOnC(kh=item[0])[0]))
        res=[]
        D=list(searchAll("D"))
        for item in k:
            item[4] = D[int(item[4])-1][1]
            if {"kh":item[0],"km":item[1],"xf":item[2],"xs":item[3],"mc":item[4]} not in res:
                res.append({"kh":item[0],"km":item[1],"xf":item[2],"xs":item[3],"mc":item[4]})
        return res
    if kh=='':
        tmp = list(searchOnO(iskh=True,xq=term,km=km))
        k=[]
        for item in tmp:
            if item[0] not in k:
                k.append(list(searchOnC(kh=item[0])[0]))
        res=[]
        D=list(searchAll("D"))
        for item in k:
            item[4] = D[int(item[4])-1][1]
            if {"kh": item[0], "km": item[1], "xf": item[2], "xs": item[3], "mc": item[4]} not in res:
                res.append({"kh": item[0], "km": item[1], "xf": item[2], "xs": item[3], "mc": item[4]})
        return res
    if km=='':
        tmp = list(searchOnO(iskh=True,xq=term,kh=kh))
        k=[]
        for item in tmp:
            if item[0] not in k:
                k.append(list(searchOnC(kh=item[0])[0]))
        res=[]
        D=list(searchAll("D"))
        for item in k:
            item[4] = D[int(item[4])-1][1]
            if {"kh": item[0], "km": item[1], "xf": item[2], "xs": item[3], "mc": item[4]} not in res:
                res.append({"kh": item[0], "km": item[1], "xf": item[2], "xs": item[3], "mc": item[4]})
        return res
    tmp = list(searchOnO(iskh=True, xq=term, kh=kh))
    k = []
    for item in tmp:
        if item[0] not in k:
            k.append(list(searchOnC(kh=item[0])[0]))
    res = []
    D = list(searchAll("D"))
    for item in k:
        item[4] = D[int(item[4]) - 1][1]
        if {"kh": item[0], "km": item[1], "xf": item[2], "xs": item[3], "mc": item[4]} not in res:
            res.append({"kh": item[0], "km": item[1], "xf": item[2], "xs": item[3], "mc": item[4]})
    return res
def getAllCourse(data):
    k=list(searchAll('c'))
    kk=[]
    for item in k:
        kk.append(list(item))
    res = []
    D = list(searchAll("D"))
    for item in kk:
        item[4]= D[int(item[4]) - 1][1]
        if {"kh": item[0], "km": item[1], "xf": item[2], "xs": item[3], "mc": item[4]} not in res:
            res.append({"kh": item[0], "km": item[1], "xf": item[2], "xs": item[3], "mc": item[4]})
    return res
def createCourse(data):
    print(data)
    D =list(searchAll('D'))
    for item in D:
        if item[1]==data['yx']:
            yxh=item[0]
    k=insertOnC(data['kh'],data['km'],data['xf'],data['xs'],yxh)
    print(k)
    return k
def createClass(data):
    print(data)
    k=insertOnO(xq=data['xq'],kh=data['kh'],sksj=data['sksj'],gh=data['gh'],rs='0')
    print(k)
    return k
def createStudentInClass(data):
    print(data)
    k=insertOnE(kh=data['kh'],xh=data['xh'],xq=data['xq'],gh=data['gh'])
    print(k)
    return k
def getClass(data):
    print(data)
    if 'gh' not in data:
        tmp = searchOnO(xq = data['term'],kh = data['kh'])
    else:tmp = searchOnO(xq = data['term'],kh = data['kh'],gh=data['gh'])
    k = []
    for item in tmp:
        x=searchOnC(kh=item[1])[0][1]
        print()
        k.append({'km':x,'kh':item[1],'gh':item[2],'sksj':item[3],'rs':item[4]})
    return k
def getStudent(data):
    print(data)
    S = searchAll('S')
    D = list(searchAll('D'))
    res=[]
    if 'xh'not in data:
        for item in searchOnE(isxh=True,xq=data['term'],kh=data['kh'],gh=data['gh']):
            for j in S:
                if j[0]==item[0]:
                    res.append({'xh':item[0],'xm':j[1],'yx':D[int(list(j)[6])-1][1]})
    else:
        for item in searchOnE(isxh=True,xq=data['term'],kh=data['kh'],gh=data['gh'],xh=data['xh']):
            for j in S:
                if j[0]==item[0]:
                    res.append({'xh':item[0],'xm':j[1],'yx':D[int(list(j)[6])-1][1]})
    return res
def deletCourse(data):
    print(data)
    k=deleteOnC(kh=data['kh'])
    if k:
        return '删除成功'
    else:
        return  '删除失败'
def deletClass(data):
    print(data)
    k=deleteOnO(xq=data['xq'],kh=data['kh'],gh=data['gh'],sksj=data['sksj'])
    if k:
        return '删除成功'
    else:
        return  '删除失败'
def deletStudentFromClass(data):
    print(data)
    k=deleteOnE(xq=data['xq'],kh=data['kh'],gh=data['gh'],xh=data['xh'])
    if k:
        return '删除成功'
    else:
        return  '删除失败'
def getAllStudent(data):
    D = searchAll('D')
    s=[]
    for item in list(searchAll('s')):
        item=list(item)
        if 'xh' in data:
            if item[0]==data['xh']:
                s.append({'xh':item[0],'xm':item[1],'yx':D[int(item[6])-1][1]})
        else:
            s.append({'xh': item[0], 'xm': item[1], 'yx': D[int(item[6]) - 1][1]})
    return s
def getAllTeacher(data):
    print('teacher',data)
    D = searchAll('D')
    t=[]
    for item in list(searchAll('t')):
        item=list(item)
        if 'gh' in data:
            if item[0] == data['gh']:
                t.append({'gh': item[0], 'xm': item[1], 'yx': D[int(item[6]) - 1][1]})
        else:
            t.append({'gh': item[0], 'xm': item[1], 'yx': D[int(item[6]) - 1][1]})
    return t
def creatTeacher(data):
    print(data)
    k=insertOnT(gh=data['gh'],yxh=data['yx'],xm=data['xm'],csrq='2020-06-27',xl='教授',jbgz='5000')
    if k==1 :
        return 'success'
    if k==-1:
        return 'failed 工号冲突'
    else:return 'failed 字段非法'
def creatStudent(data):
    print(data)
    k=insertOnS(xh=data['xh'],yxh=data['yx'],xm=data['xm'],csrq='2020-06-27',jg='上海',sjhm='10000000000')
    if k==1 :
        return 'success'
    if k==-1:
        return 'failed 学号冲突'
    else:return 'failed 字段非法'
def deleteTeacher(data):
    print(data)
    k=deleteOnT(gh=data['gh'])
    if k:
        return 'success'
    else:return 'failed'
def deleteStudent(data):
    print(data)
    k=deleteOnS(xh=data['xh'])
    if k:
        return 'success'
    else:return 'failed'
# print(searchOnO(iskh=True,xq='2013-2014冬季'))
# print(searchCourse(xq='2013-2014冬季'))
# print(searchOnO(iskh=True,xq='2013-2014冬季'))
# # print(int('01'))
# print(searchAll('D'))
# print(searchOnC(kh='08301001')[0][1])
# {'term': '2013-2014冬季', 'kh': '08302001', 'gh': '0201'}
# print(searchAll('S'))
# print(searchOnE(isxh=True,xq='2013-2014冬季',kh='08302001',gh='0201'))
# print(getAllStudent())insertOnS(gh=data['gh'],yxh=data['yxh'],xm=data['xm'],csrq='2020-06-27')
# print(insertOnS(xh='0202',yxh='01',xm='02',csrq='2020-06-27',jg='上海',sjhm='1000000000'))