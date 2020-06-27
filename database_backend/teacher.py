from database import *
# print(insertOnUser('0202','111111','teacher'))
# print(insertOnUser(usr='0101',pwd='111111',type='teacher'))
def getClass(data):
    print(data)
    # print(searchOnO(iskh=True,isrs=True,issksj=True,gh=data['gh'],xq=data['xq']))
    c = list(searchAll('c'))
    k=[]
    for i in list(searchOnO(iskh=True,isrs=True,issksj=True,gh=data['gh'],xq=data['xq'])):
        i=list(i)
        for C in c:
            if C[0]==i[0]:
                k.append({'kh':C[0],'km':C[1],'sksj':i[1],'rs':i[2]})
    return k
# print(getClass({'gh':'0101','xq':'2012-2013冬季'}))
def getStudent(data):
    print(data)
    if 'xh' in data:
        tmp = list(searchOnE(isxh=True,iskscj=True,ispscj=True,iszpcj=True,xq=data['xq'],xh=data['xh'],kh=data['kh'],gh=data['gh']))
    else:
        tmp = list(
            searchOnE(isxh=True, iskscj=True, ispscj=True, iszpcj=True, xq=data['xq'], kh=data['kh'],
                      gh=data['gh']))
    s = list(searchAll('s'))
    d = list(searchAll('d'))
    k = []
    for i in tmp:
        for S in s:
            if S[0] == i[0]:
                for D in d:
                    if D[0] == S[6]:
                        k.append(
                            {'xh': S[0], 'xm': S[1], 'yx': D[1], 'zpcj': i[5], 'pscj': i[3], 'kscj': i[4]})
    score=[0]*4
    for i in tmp:
        i = list(i)
        if int(i[5])>90:
            score[0]=score[0]+1
        elif int(i[5])>80:
            score[1]=score[1]+1
        elif int(i[5])>60:
            score[2]=score[2]+1
        else:score[3]=score[3]+1
    rows= [
        {'分段': '优', '人数': score[0]},
        {'分段': '良', '人数': score[1]},
        {'分段': '及格', '人数': score[2]},
        {'分段': '失败', '人数': score[3]}
    ]
    return {'list':k,'rows':rows}
def updateScore(data):
    print(data)
    zpcj=0.5*int(data['pscj'])+0.5*int(data['kscj'])
    if updateOnE(old_xq=data['xq'],old_gh=data['gh'],old_kh=data['kh'],old_xh=data['xh'],new_zpcj=str(zpcj),new_kscj=data['kscj'],new_pscj=data['pscj']):
        return '修改成功'
    return '修改失败'
# print(getStudent({'xq':'2012-2013冬季','xh':'1102','kh':'08305002','gh':'0101'}))
# print(getStudent({'xq':'2012-2013冬季','kh':'08305002','gh':'0101'}))
# print(searchAll('s'))
# print(updateScore({'pscj':'60','kscj':'70','xq':"2013-2014秋季",'gh':'0101','kh':'08305004','xh':'1102'}))