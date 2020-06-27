from database import *
# insertOnInfo('0','2012-2013冬季')
# insertOnInfo('0','2012-2013秋季')
# insertOnInfo('0','2013-2014秋季')
def getScore(data):
    print(data)
    k=[]
    row=[]
    c=list(searchAll('c'))
    for item in list(searchOnE(iskh=True,iszpcj=True,ispscj=True,iskscj=True,xh=data['xh'],xq=data['xq'])):
        item = list(item)
        for C in c:
            print(c[0],item[0])
            if C[0]==item[0]:
                k.append({'kh':C[0],'km':C[1],'xf':C[2],'xs':C[3],'zpcj':item[4]})
                row.append({'课名':C[1],'平时成绩':item[2],'考试成绩':item[3],'总评成绩':item[4]})
    return {"list":k,"rows":row}
def getSelectedCourse(data):
    print(data)
    c = list(searchAll('c'))
    t = list(searchAll('t'))
    k = []
    for x in list(searchOnE(xq=data['xq'], xh=data['xh'])):
        kh = x[0]
        gh = x[1]
        for i in list(searchOnO(iskh=True, isgh=True, issksj=True, isrs=True, gh=gh, kh=kh, xq=data['xq'])):
            for C in c:
                if C[0] == i[0]:
                    for T in t:
                        if T[0] == i[1]:
                            k.append(
                                {'kh': i[0], 'km': C[1], 'xf': C[2], 'xs': C[3], 'gh': i[1], 'mz': T[1], "rs": i[3],
                                 'sj': i[2]})
    return k
    # if kh
def getCourse(data):
    c = list(searchAll('c'))
    t = list(searchAll('t'))
    k=[]
    if 'kh' in data and 'gh' in data:
        for i in list(searchOnO(iskh=True, isgh=True, issksj=True, isrs=True, gh=data['gh'],kh=data['kh'], xq=data['xq'])):
            for C in c:
                if C[0] == i[0]:
                    for T in t:
                        if T[0] == i[1]:
                            k.append(
                                {'kh': i[0], 'km': C[1], 'xf': C[2], 'xs': C[3], 'gh': i[1], 'mz': T[1], "rs": i[3],
                                 'sj': i[2]})
        return k
    if 'gh' in data:
        for i in list(searchOnO(iskh=True, isgh=True, issksj=True, isrs=True,gh=data['gh'],xq=data['xq'])):
            for C in c:
                if C[0] == i[0]:
                    for T in t:
                        if T[0] == i[1]:
                            k.append({'kh':i[0],'km':C[1],'xf':C[2],'xs':C[3],'gh':i[1],'mz':T[1],"rs":i[3],'sj':i[2]})
        return k
    if 'kh' in data:
        for i in list(searchOnO(iskh=True, isgh=True, issksj=True, isrs=True,kh=data['kh'], xq=data['xq'])):
            for C in c:
                if C[0] == i[0]:
                    for T in t:
                        if T[0] == i[1]:
                            k.append(
                                {'kh': i[0], 'km': C[1], 'xf': C[2], 'xs': C[3], 'gh': i[1], 'mz': T[1], "rs": i[3],
                                 'sj': i[2]})
        return k
    for i in list(searchOnO( iskh=True, isgh=True, issksj=True, isrs=True,xq=data['xq'])):
        for C in c:
            if C[0] == i[0]:
                for T in t:
                    if T[0] == i[1]:
                        k.append(
                            {'kh': i[0], 'km': C[1], 'xf': C[2], 'xs': C[3], 'gh': i[1], 'mz': T[1], "rs": i[3],
                             'sj': i[2]})
    return k
def select(data):
    print(data)
    k=insertOnE(xh=data['xh'],xq=data['xq'],kh=data['kh'],gh=data['gh'])
    if k==1:
        return '选课成功'
    if k==-1:
        return '该学生这学期已经选择过这门课程'
    if k==-2:
        return '学生课程课时冲突'
    return  '选课失败'
def delete(data):
    print(data)
    k=deleteOnE(xh=data['xh'],xq=data['xq'],kh=data['kh'],gh=data['gh'])
    if k:return '退课成功'
    else:return  '退课失败'

# print(searchAll('c'))
# print(searchOnE(iskh=True,iszpcj=True,ispscj=True,iskscj=True,xh='1102',xq='2012-2013冬季'))
# print(searchOnO(iskh=True,isgh=True,issksj=True,isrs=True,kh='08305002',xq='2012-2013冬季'))
# print(searchAll('t'))
# print(searchOnE(xq='2012-2013冬季',xh='1102'))
# print(len(searchOnE(xq='2012-2013冬季',xh='1102')))
# print(getCourse({"xq":'2013-2014冬季'}))
# print(deleteOnE(xh='1101',xq='2013-2014冬季',kh='08302001',gh='0201'))

