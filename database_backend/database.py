# -*- coding: utf-8 -*-
'''
# Created on Feb-06-20 16:56
# util.py
# @author: ss
# 说明：这里主要后台对数据库的调用
'''

import pymysql, hashlib
import re


def md5(s, salt='Database2020!$%@#+'):
    '''
    这是一个md5哈希函数，主要是对文本进行哈希加密
    返回一个32位的十六进制加密字符串
    '''
    s = (str(s) + salt).encode()
    m = hashlib.md5(s)  # 加密
    return m.hexdigest()


class Database:
    """
    Tables used in the database:
    department: did; name
    student: sid; name; gender; did; password
    teacher: tid; name; gender; did; password
    course: cid; name; credit; tid; did; time
    selection: cid; sid; score
    """

    def __init__(self, mysql_info):
        self._connection = pymysql.connect(**mysql_info)

    def __del__(self):
        self._connection.close()

    def _execute(self, query):
        '''
        返回执行结果
        '''
        try:
            cursor = self._connection.cursor()
            cursor.execute(query)
            s = query.split()[0]

            res = None
            if s == 'update' or s == 'insert' or s == 'delete':
                self._connection.commit()
                cursor.close()
            elif s == 'select':
                res = cursor.fetchall()
                cursor.close()
            return (True, res)
        except Exception as e:
            self._connection.rollback()
            return (False, e)


mysql_info = {
    'host': 'localhost',  # 数据库地址
    'user': 'root',  # 数据库用户身份
    'password': 'root',  # 数据库用户对应的密码密码
    'db': 'edu',  # 数据库的名字
    'charset': 'utf8',  # 数据库编码方式
    'autocommit': True}
db = Database(mysql_info)


def op_mysql(sql: str):
    '''
    输入sql命令操作数据库返回对应结果
    '''
    return db._execute(query=sql)


def search(ser, tablename, jud=None, jres=None):
    '''
    # 功能：查询 \n
    # 接受参数：ser 查询条件, tablenmae 表名, jud判断条件, jres 判断对应  \n
    # 返回参数：\n
    '''
    sql = 'select ' + ser + ' from ' + tablename
    if jud and jres:
        sql = (sql + ' where ' + jud) % jres
    flag, res = op_mysql(sql)
    if flag:
        return res
    else:
        return None

def searchAll( tablename, jud=None, jres=None):
    '''
    # 功能：查询 \n
    # 接受参数：ser 查询条件, tablenmae 表名, jud判断条件, jres 判断对应  \n
    # 返回参数：\n
    '''
    sql = 'select ' + "*" + ' from ' + tablename
    flag, res = op_mysql(sql)
    if flag:
        return res
    else:
        return None

def update(tablename, upd, ures, jud, jres):
    '''
    # 功能：更新

    # 接受参数：

    # 返回参数：

    '''
    sql = "update %s set " % (tablename)
    sql = (sql + upd) % ures
    sql = (sql + ' where ' + jud) % jres
    print(sql)
    flag, res = op_mysql(sql)
    if flag:
        return True
    else:
        print(res)
        return False

def updatePass(tablename, upd, ures, jud, jres):
    '''
    # 功能：更新

    # 接受参数：

    # 返回参数：

    '''
    tablename="user"
    sql = "update %s set " % (tablename)
    sql = (sql + upd) % ures
    sql = (sql + ' where ' + jud) % jres
    print(sql)
    flag, res = op_mysql(sql)
    if flag:
        return True
    else:
        print(res)
        return False

def insert(tablename, ind, ires):
    '''
    # 功能：sql 插入语句

    # 接受参数：

    # 返回参数：

    '''
    sql = "insert into " + tablename
    sql = sql + "(" + ind + ")" + " values " + str(ires)
    flag, res = op_mysql(sql)
    if flag == False:
        print(res)
    return flag


def delete(tablename, jud, jres):
    '''
    # 功能：删除指令拼接

    # 接受参数：

    # 返回参数：

    '''
    sql = 'delete from ' + tablename
    sql = (sql + ' where ' + jud) % jres
    flag, res = op_mysql(sql)
    if flag == False:
        print(res)
    return flag


def register(usr: str, pwd: str, cpwd: str, typename: str) -> int:
    '''
    # 功能：
    # 接受参数：用户名, 密码, 二次密码, 用户类型
    # 返回参数：
    返回int类型代表各种情况
    -2 数据库端程序错误
    -1 输入字段存在空
    0 成功注册
    1 输入两次密码不一致
    2 用户名已经存在数据库之中
    3 用户不在对应数据表之中
    '''
    if usr and pwd and cpwd:
        if pwd != cpwd:
            return 1  # 两次输入密码不一致

        query = ""
        if typename == 'student':
            query = "select xh from s where xh = '%s'" % (usr)
        elif typename == 'teacher':
            query = "select gh from t where gh = '%s'" % (usr)

        flag, res = op_mysql(query)
        if flag:
            if len(res) == 0:
                return 3  # 用户对应的数据表之中

        usr = md5(usr)
        select_usr_sql = "select * from user where usr = '%s' and type = '%s'" % (usr, typename)
        flag, res = op_mysql(select_usr_sql)
        if flag == False:
            print(res)
            return -2  # 数据库查询的有问题
        else:
            if res:
                for x in res:
                    if x[0] == usr:
                        return 2  # 用户名已经存在
            else:
                pwd = md5(pwd)
                ins_sql = "insert into user(usr, pwd, type) values ('%s', '%s', '%s')" % (usr, pwd, typename)
                flag, res = op_mysql(ins_sql)
                if flag:
                    return 0  # 注册成功
                else:
                    print(res)
                    return -2  # 出了bug
    else:
        return -1  # 存在输入为空


def login(usr: str, pwd: str, typename: str) -> int:
    '''
    # 功能：用户登录验证
    # 接受参数：
    # 返回参数：
    -2 数据库端查询错误
    -1 输入字段存在空
    0 密码正确, 可以登录
    1 密码错误, 不可登录
    2 此用户不存在
    '''
    query = ""
    if typename == 'student':
        query = "select xh from s where xh = '%s'" % (usr)
    elif typename == 'teacher':
        query = "select gh from t where gh = '%s'" % (usr)
    flag, res = op_mysql(query)
    if flag:
        if len(res) == 0:
            return 2  # 此用户不存在

    usr = md5(usr)
    pwd = md5(pwd)
    if usr and pwd:
        select_usr_sql = "select * from user where usr = '%s' and type = '%s'" % (usr, typename)
        flag, res = op_mysql(select_usr_sql)
        if flag == False:
            return -2  # 数据库查询出错
        else:
            if res:
                for x in res:
                    if x[0] == usr:
                        if x[1] == pwd:
                            return 0  # 密码正确, 可以登录
                        else:
                            return 1  # 密码错误, 不可登录
            return 2  # 此用户不存在
    else:
        return -1  # 用户名或者密码不能为空


def searchOnS(isxh=True, isxm=True, isxb=True, iscsrq=False, isjg=False, issjhm=False, isyxh=True,
              xh=None, xm=None, xb=None, csrq=None, jg=None, sjhm=None, yxh=None):
    '''
    # 功能：查询学生表的对应信息, is标志查询返回项，没有is的标志判断项
    # 接受参数：
    # 返回参数：
    '''
    ser = []
    if isxh or isxm or isxb or iscsrq or isjg or issjhm or isyxh:
        if isxh:
            ser.append('xh')
        if isxm:
            ser.append('xm')
        if isxb:
            ser.append('xb')
        if iscsrq:
            ser.append('csrq')
        if isjg:
            ser.append('jg')
        if issjhm:
            ser.append('sjhm')
        if isyxh:
            ser.append('yxh')
    else:
        ser.append('*')
    ser = ','.join(ser)

    jud = []
    jres = []
    if xh or xm or xb or csrq or jg or sjhm or yxh:
        if xh:
            jud.append("xh='%s'")
            jres.append(xh)
        if xm:
            jud.append("xm='%s'")
            jres.append(xm)
        if xb:
            jud.append("xb='%s'")
            jres.append(xb)
        if csrq:
            jud.append("csrq='%s'")
            jres.append(csrq)
        if jg:
            jud.append("jg='%s'")
            jres.append(jg)
        if sjhm:
            jud.append("sjhm='%s'")
            jres.append(sjhm)
        if yxh:
            jud.append("yxh='%s'")
            jres.append(yxh)
    jud = ' and '.join(jud)
    jres = tuple(jres)
    return search(ser, 's', jud, jres)


def searchOnC(iskh=False, iskm=False, isxf=False, isxs=False, isyxh=False,
              kh=None, km=None, xf=None, xs=None, yxh=None
              ):
    '''
    # 功能：查询课程表的对应信息, is标志查询返回项，没有is的标志判断项
    # 接受参数：
    # 返回参数：
    '''
    ser = []
    if iskh or iskm or isxf or isxs or isyxh:
        if iskh:
            ser.append('kh')
        if iskm:
            ser.append('km')
        if isxf:
            ser.append('xf')
        if isxs:
            ser.append('xs')
        if isyxh:
            ser.append('yxh')
    else:
        ser.append('*')
    ser = ','.join(ser)

    jud = []
    jres = []
    if kh or km or xf or xs or yxh:
        if kh:
            jud.append("kh='%s'")
            jres.append(kh)
        if km:
            jud.append("km='%s'")
            jres.append(km)
        if xf:
            jud.append("xf='%s'")
            jres.append(xf)
        if xs:
            jud.append("xs='%s'")
            jres.append(xs)
        if yxh:
            jud.append("yxh='%s'")
            jres.append(yxh)
    jud = ' and '.join(jud)
    jres = tuple(jres)
    return search(ser, 'c', jud, jres)


def searchOnT(isgh=True, isxm=True, isxl=False, isyxh=False,
              gh=None, xm=None, yxh=None
              ):
    '''
    # 功能：查询教师表T的对应信息, is标志查询返回项，没有is的标志判断项
    # 接受参数：
    # 返回参数：
    '''
    ser = []
    if isgh or isxm or isxl or isyxh:
        if isgh:
            ser.append('gh')
        if isxm:
            ser.append('xm')
        if isxl:
            ser.append('xl')
        if isyxh:
            ser.append('yxh')
    else:
        ser.append('*')

    ser = ','.join(ser)

    jud = []
    jres = []
    if gh or xm or yxh:
        if gh:
            jud.append("gh='%s'")
            jres.append(gh)
        if xm:
            jud.append("xm='%s'")
            jres.append(xm)
        if yxh:
            jud.append("yxh='%s'")
            jres.append(yxh)
    jud = ' and '.join(jud)
    jres = tuple(jres)

    return search(ser, 't', jud, jres)


def searchOnO(isxq=False, iskh=False, isgh=False, issksj=False, isrs=False,  # 前面四is代表查询返回项
              xq=None, kh=None, gh=None, sksj=None  # 后面代表要查询项对应条件
              ):
    '''
    # 功能：查询开课表的对应信息, is标志查询返回项，没有is的标志判断项
    # 接受参数：
    # 返回参数：
    '''
    if xq == None and kh == None and gh == None and sksj == None:
        return None

    ser = []
    if isxq or iskh or isgh or issksj:
        if isxq:
            ser.append('xq')
        if iskh:
            ser.append('kh')
        if isgh:
            ser.append('gh')
        if issksj:
            ser.append('sksj')
        if isrs:
            ser.append('rs')
    else:
        ser.append('*')

    ser = ','.join(ser)

    jud = []
    jres = []
    if xq or kh or gh or sksj:
        if xq:
            jud.append("xq='%s'")
            jres.append(xq)
        if kh:
            jud.append("kh='%s'")
            jres.append(kh)
        if gh:
            jud.append("gh='%s'")
            jres.append(gh)
        if sksj:
            jud.append("sksj='%s'")
            jres.append(sksj)
    jud = ' and '.join(jud)
    jres = tuple(jres)

    return search(ser, 'o', jud, jres)


def searchOnE(isxh=False, isxq=False, iskh=True, isgh=True, ispscj=False, iskscj=False, iszpcj=False,
              xh=None, xq=None, kh=None, gh=None
              ):
    '''
    # 功能：在e表中进行查询(查询条件不包含对成绩的判断，但是可以返回课程成绩) \n
    # 接受参数：is 表示查询返回项, 非is表示判断项 \n
    # 返回参数：
    '''
    if xq == None and kh == None and gh == None and xh == None:
        return None

    ser = []
    if isxh or isxq or iskh or isgh:
        if isxh:
            ser.append('xh')
        if isxq:
            ser.append('xq')
        if iskh:
            ser.append('kh')
        if isgh:
            ser.append('gh')
        if ispscj:
            ser.append('pscj')
        if iskscj:
            ser.append('kscj')
        if iszpcj:
            ser.append('zpcj')
    else:
        ser.append('*')

    ser = ','.join(ser)

    jud = []
    jres = []
    if xh or xq or kh or gh:
        if xh:
            jud.append("xh='%s'")
            jres.append(xh)
        if xq:
            jud.append("xq='%s'")
            jres.append(xq)
        if kh:
            jud.append("kh='%s'")
            jres.append(kh)
        if gh:
            jud.append("gh='%s'")
            jres.append(gh)
    jud = ' and '.join(jud)
    jres = tuple(jres)

    return search(ser, 'e', jud, jres)


def searchOnInfo(isxq=False, isyxh=False, issx=False,
                 flag=None, xq=None, yxh=None, sx=None):
    '''
    # 功能：查询info表里的信息

    # 接受参数：

    # 返回参数：

    '''
    if xq == None and yxh == None and flag == None and sx == None:
        return None

    ser = []
    if isxq or isyxh or issx:
        if isxq:
            ser.append('xq')
        if isyxh:
            ser.append('yxh')
        if issx:
            ser.append('sx')
    else:
        ser.append('*')

    ser = ','.join(ser)

    jud = []
    jres = []
    if flag or xq or yxh or sx:
        if flag:
            jud.append("flag=%s")
            jres.append(flag)
        if xq:
            jud.append("xq='%s'")
            jres.append(xq)
        if yxh:
            jud.append("ykh='%s'")
            jres.append(yxh)
        if sx:
            jud.append("sx=%s")
            jres.append(sx)
    jud = ' and '.join(jud)
    jres = tuple(jres)

    return search(ser, 'info', jud, jres)

def searchOnD(isyxh=True, ismc=False, isdz=False, islxdh=False,
                 yxh=None, mc=None, dz=None, lxdh=None):
    '''
    # 功能：查询info表里的信息

    # 接受参数：

    # 返回参数：

    '''
    if yxh == None and mc == None and dz == None and lxdh == None:
        return None

    ser = []
    if isyxh or ismc or isdz:
        if isyxh:
            ser.append('yxh')
        if ismc:
            ser.append('mc')
        if isdz:
            ser.append('dz')
    else:
        ser.append('*')

    ser = ','.join(ser)

    jud = []
    jres = []
    if yxh or mc or dz or lxdh:
        if yxh:
            jud.append("yxh=%s")
            jres.append(yxh)
        if mc:
            jud.append("mc='%s'")
            jres.append(mc)
        if dz:
            jud.append("dz='%s'")
            jres.append(dz)
        if lxdh:
            jud.append("lxdh=%s")
            jres.append(lxdh)
    jud = ' and '.join(jud)
    jres = tuple(jres)
    print(ser, 'd', jud, jres)
    return search(ser, 'd', jud, jres)

def getclasstime(data):
    '''
    # 功能：获取课程时间 \n
    # 接受参数：\n
    # 返回参数：\n
    eg: \n
    接受: 星期一6-10 \n
    返回[0, 6, 10], 0映射星期一
    '''
    data = data.split('星期')
    res = []
    lis = ['一', '二', '三', '四', '五', '六', '日']
    for x in data:
        if x != '':
            tmp = []
            for i in range(len(lis)):
                if x[0] == lis[i]:
                    tmp.append(i)
                    break
            x = x[1:].split('-')
            tmp.append(int(re.sub("\D", "", x[0])))
            tmp.append(int(re.sub("\D", "", x[1])))
            res.append(tmp)
    return res


def judgeclasstime(time1, time2):
    '''
    两个课程时间是否冲突
    time = [(day, st, ed)]
    '''
    time1 = getclasstime(time1)
    time2 = getclasstime(time2)
    for x in time1:
        for y in time2:
            if x[0] != y[0]:
                continue
            if x[1] <= y[1] and y[1] <= x[2]:
                return False
            if y[1] <= x[1] and x[1] <= y[2]:
                return False
            if x[1] <= y[2] and y[2] <= x[2]:
                return False
            if y[1] <= x[2] and x[2] <= y[2]:
                return False
    return True  # 不冲突


def getClassLists(xq, kh, gh, iscj=False):
    '''
    # 功能：在选课表e中获取某个老师某门课程的班级信息
    (会将成绩也一并返回，如果不需要，则注意舍弃) \n
    # 接受参数：iscj为真表示需要返回成绩，否则只返回学号，姓名 \n
    # 返回参数：
    '''
    sql = "select xh, pscj, kscj, zpcj from e where xq='%s' and kh='%s' and gh='%s'" % (xq, kh, gh)
    flag, res = op_mysql(sql)
    if flag and len(res) == 0:
        return []
    elif flag == False:
        return []
    data = []
    for x in res:
        tmp = []
        tmp.append(x[0])
        sql = "select xm from s where xh = '%s'" % (x[0])
        _, y = op_mysql(sql)
        tmp.append(y[0][0])
        if iscj:
            for i in range(1, 4):
                if x[i] != None:
                    tmp.append(str(x[i]))
                else:
                    tmp.append('null')
        data.append(tmp)
    return data


def updateStuScore(xh, xq, kh, gh, pscj, kscj, zpcj):
    '''
    # 功能：更新学生的成绩 \n
    # 接受参数：\n
    # 返回参数：\n
    '''
    sql = '''update e set pscj=%s, kscj=%s, zpcj=%s 
                where xh='%s' and xq='%s' and kh='%s' and gh='%s' 
            ''' % (pscj, kscj, zpcj, xh, xq, kh, gh)
    flag, e = op_mysql(sql)
    return flag, e

def updatePwd(usr, pwd):
    '''
    # 功能：更新学生的成绩 \n
    # 接受参数：\n
    # 返回参数：\n
    '''
    usr=md5(usr)
    pwd=md5(pwd)
    sql = '''update user set pwd='%s' 
                where usr='%s' 
            ''' % (pwd, usr)
    flag, e = op_mysql(sql)
    return flag, e

def updateOnC(old_kh=None, old_km=None, old_xf=None, old_xs=None,
              new_kh=None, new_km=None, new_xf=None, new_xs=None):
    '''
    # 功能：更新C表

    # 接受参数：

    # 返回参数：

    '''
    sql = "SET FOREIGN_KEY_CHECKS=0"  # 强制取消外键约束
    op_mysql(sql)

    upd = []
    ures = []
    if new_kh:
        upd.append("kh='%s'")
        ures.append(new_kh)
    if new_km:
        upd.append("km = '%s'")
        ures.append(new_km)
    if new_xf:
        upd.append("xf = '%s'")
        ures.append(new_xf)
    if new_xs:
        upd.append("xs = '%s'")
        ures.append(new_xs)

    upd = ','.join(upd)
    ures = tuple(ures)

    jud = []
    jres = []
    if old_kh:
        jud.append("kh = '%s'")
        jres.append(old_kh)
    if old_km:
        jud.append("km='%s'")
        jres.append(old_km)
    if old_xf:
        jud.append("xf = '%s'")
        jres.append(old_xf)
    if old_xs:
        jud.append("xs = '%s'")
        jres.append(old_xs)

    jud = ' and '.join(jud)
    jres = tuple(jres)

    ok = update('c', upd, ures, jud, jres)

    if ok == False:
        sql = "SET FOREIGN_KEY_CHECKS=0"  # 强制取消外键约束
        op_mysql(sql)
        return False
    if new_kh:
        ok = updateOnO(old_kh=old_kh, new_kh=new_kh)
        if ok == False:
            sql = "SET FOREIGN_KEY_CHECKS=0"  # 强制取消外键约束
            op_mysql(sql)
            return False
    sql = "SET FOREIGN_KEY_CHECKS=0"  # 强制取消外键约束
    op_mysql(sql)
    return True


def updateOnE(old_xq=None, old_kh=None, old_gh=None, old_xh=None,
              new_xq=None, new_kh=None, new_gh=None, new_pscj=None, new_kscj=None, new_zpcj=None):
    '''
    # 功能：更新E表

    # 接受参数：

    # 返回参数：

    '''
    upd = []
    ures = []
    if new_xq:
        upd.append("xq='%s'")
        ures.append(new_xq)
    if new_kh:
        upd.append("kh = '%s'")
        ures.append(new_kh)
    if new_gh:
        upd.append("gh = '%s'")
        ures.append(new_gh)
    if new_pscj:
        upd.append("pscj='%s'")
        ures.append(new_pscj)
    if new_kscj:
        upd.append("kscj = '%s'")
        ures.append(new_kscj)
    if new_zpcj:
        upd.append("zpcj = '%s'")
        ures.append(new_zpcj)
    upd = ','.join(upd)
    ures = tuple(ures)

    jud = []
    jres = []
    if old_xh:
        jud.append("xh='%s'")
        jres.append(old_xh)
    if old_xq:
        jud.append("xq='%s'")
        jres.append(old_xq)
    if old_kh:
        jud.append("kh = '%s'")
        jres.append(old_kh)
    if old_gh:
        jud.append("gh = '%s'")
        jres.append(old_gh)
    jud = ' and '.join(jud)
    jres = tuple(jres)

    ok = update('e', upd, ures, jud, jres)
    if ok == True:
        return True
    else:
        return False


def updateOnO(old_xq=None, old_kh=None, old_gh=None, old_sksj=None, old_rs=None,
              new_xq=None, new_kh=None, new_gh=None, new_sksj=None, new_rs=None):
    '''
    # 功能：更新O表

    # 接受参数：

    # 返回参数：

    '''
    sql = "SET FOREIGN_KEY_CHECKS=0"  # 强制取消外键约束
    op_mysql(sql)

    upd = []
    ures = []
    if new_xq:
        upd.append("xq='%s'")
        ures.append(new_xq)
    if new_kh:
        upd.append("kh = '%s'")
        ures.append(new_kh)
    if new_gh:
        upd.append("gh = '%s'")
        ures.append(new_gh)
    if new_sksj:
        upd.append("sksj = '%s'")
        ures.append(new_sksj)
    if new_rs:
        upd.append("rs = %s")
        ures.append(new_rs)
    upd = ','.join(upd)
    ures = tuple(ures)

    jud = []
    jres = []
    if old_xq:
        jud.append("xq='%s'")
        jres.append(old_xq)
    if old_kh:
        jud.append("kh = '%s'")
        jres.append(old_kh)
    if old_gh:
        jud.append("gh = '%s'")
        jres.append(old_gh)
    if old_sksj:
        jud.append("sksj = '%s'")
        jres.append(old_sksj)
    if old_rs:
        jud.append("rs = %s")
        jres.append(old_rs)
    jud = ' and '.join(jud)
    jres = tuple(jres)

    ok = update('o', upd, ures, jud, jres)
    if ok == False:
        sql = "SET FOREIGN_KEY_CHECKS=1"  # 恢复外键约束
        op_mysql(sql)
        return False
    ok = updateOnE(old_xq, old_kh, old_gh, new_xq, new_kh, new_gh)
    sql = "SET FOREIGN_KEY_CHECKS=1"  # 恢复外键约束
    op_mysql(sql)
    if ok == False:
        return False
    else:
        return True


def updateOnInfo(old_flag=None, old_xq=None, old_yxh=None, old_sx=None,
                 new_flag=None, new_xq=None, new_yxh=None, new_sx=None):
    '''
    # 功能：更新信息表

    # 接受参数：

    # 返回参数：

    '''
    upd = []
    ures = []
    if new_flag:
        upd.append("flag ='%s'")
        ures.append(new_flag)
    if new_xq:
        upd.append("xq ='%s'")
        ures.append(new_xq)
    if new_yxh:
        upd.append("yxh ='%s'")
        ures.append(new_yxh)
    if new_sx:
        upd.append("sx = %s")
        ures.append(new_sx)

    upd = ','.join(upd)
    ures = tuple(ures)

    jud = []
    jres = []
    if old_flag:
        jud.append("flag = '%s'")
        jres.append(old_flag)
    if old_xq:
        jud.append("xq = '%s'")
        jres.append(old_xq)
    if old_yxh:
        jud.append("yxh = '%s'")
        jres.append(old_yxh)
    if old_sx:
        jud.append("sx = '%s'")
        jres.append(old_sx)

    jud = ' and '.join(jud)
    jres = tuple(jres)

    ok = update('info', upd, ures, jud, jres)
    return ok


def insertOnInfo(flag, xq, yxh=None, sx=None):
    '''
    # 功能：往信息表info中插入一条数据

    # 接受参数：

    # 返回参数：

    '''
    ind = []
    ires = []
    ind.append('flag')
    ires.append(flag)
    ind.append('xq')
    ires.append(xq)
    if yxh:
        ind.append('yxh')
        ires.append(yxh)
    if sx:
        ind.append('sx')
        ires.append(sx)

    ind = ' , '.join(ind)
    ires = tuple(ires)

    return insert('info', ind, ires)

def insertOnUser(usr, pwd, type):
    '''
    # 功能：往信息表info中插入一条数据

    # 接受参数：

    # 返回参数：

    '''
    ind = []
    ires = []
    ind.append('usr')
    ires.append(md5(usr))
    ind.append('pwd')
    ires.append(md5(pwd))
    ind.append('type')
    ires.append(type)
    ind = ' , '.join(ind)
    ires = tuple(ires)
    return insert('user', ind, ires)
# def insertOnS(xh, xm, xb, csrq, yxh):
def insertOnS(xh, xm, csrq, yxh, jg, sjhm):
    '''
    # 功能： 往学生表s中添加数据

    # 接受参数：

    # 返回参数：
    1 成功插入
    0 插入失败
    -1 学号冲突
    '''
    sql = "select xh from s where xh = '%s'" % (xh)
    flag, res = op_mysql(sql)
    if flag and len(res) > 0:
        return -1  # 学号冲突
    ind = []
    ires = []
    ind.append('xh')
    ires.append(xh)
    ind.append('xm')
    ires.append(xm)
    # ind.append('xb')
    # ires.append(xb)
    ind.append('csrq')
    ires.append(csrq)
    ind.append('jg')
    ires.append(jg)
    ind.append('sjhm')
    ires.append(sjhm)
    ind.append('yxh')
    ires.append(yxh)

    ind = ' , '.join(ind)
    ires = tuple(ires)

    ok = insert('s', ind, ires)
    if ok == True:
        return 1
    else:
        return 0


# def insertOnT(gh, xm, xb, csrq, xl, yxh):
def insertOnT(gh, xm, yxh, csrq, xl, jbgz):
    '''
    # 功能：往T表中插入数据

    # 接受参数：

    # 返回参数：
    1 成功插入
    0 插入失败
    -1 工号冲突
    '''
    sql = "select gh from t where gh = '%s'" % (gh)
    flag, res = op_mysql(sql)
    if flag and len(res) > 0:
        return -1  # 学号冲突
    ind = []
    ires = []
    ind.append('gh')
    ires.append(gh)
    ind.append('xm')
    ires.append(xm)
    # ind.append('xb')
    # ires.append(xb)
    ind.append('csrq')
    ires.append(csrq)
    ind.append('xl')
    ires.append(xl)
    ind.append('jbgz')
    ires.append(jbgz)
    ind.append('yxh')
    ires.append(yxh)

    ind = ' , '.join(ind)
    ires = tuple(ires)

    ok = insert('t', ind, ires)
    if ok == True:
        return 1
    else:
        return 0


def insertOnC(kh, km, xf, xs, yxh):
    '''
    # 功能：往C表中添加数据

    # 接受参数：

    # 返回参数：
    1 成功插入
    0 插入失败
    -1 课程号冲突
    '''
    sql = "select kh from c where kh = '%s'" % (kh)
    flag, res = op_mysql(sql)
    if flag and len(res) > 0:
        return -1  # 学号冲突
    ind = []
    ires = []
    ind.append('kh')
    ires.append(kh)
    ind.append('km')
    ires.append(km)
    ind.append('xf')
    ires.append(xf)
    ind.append('xs')
    ires.append(xs)
    ind.append('yxh')
    ires.append(yxh)

    ind = ' , '.join(ind)
    ires = tuple(ires)

    ok = insert('c', ind, ires)
    if ok == True:
        return 1
    else:
        return 0


def insertOnO(xq, kh, gh, sksj, rs):
    '''
    # 功能：往C表中添加数据

    # 接受参数：

    # 返回参数：
    1 成功插入
    0 插入失败
    -1 课程号不存在
    -2 教师开设的存在课时冲突
    '''
    sql = "select kh from c where kh = '%s'" % (kh)
    flag, res = op_mysql(sql)
    if flag and len(res) == 0:
        return -1  # 课程号不存在

    time1 = sksj
    res = searchOnO(0, 0, 0, 1, xq=xq, gh=gh)
    for x in res:
        time2 = x[0]
        if judgeclasstime(time1, time2) == False:
            return -2  # 课时冲突

    ind = []
    ires = []
    ind.append('xq')
    ires.append(xq)
    ind.append('kh')
    ires.append(kh)
    ind.append('gh')
    ires.append(gh)
    ind.append('sksj')
    ires.append(sksj)
    ind.append('rs')
    ires.append(rs)

    ind = ' , '.join(ind)
    ires = tuple(ires)

    ok = insert('o', ind, ires)
    if ok == True:
        return 1
    else:
        return 0


def insertOnE(xh, xq, kh, gh):
    '''
    # 功能：在E表中插入如数据

    # 接受参数：xh, xq, kh, gh

    # 返回参数：
    1 插入成功
    0 插入失败
    -1 该学生这学期已经选择过这门课程
    -2 学生课程课时冲突
    '''
    res = searchOnE(0, 0, 1, xh=xh, xq=xq, kh=kh)  # 获取课号
    if len(res):
        return -1
    time1 = searchOnO(0, 0, 0, 1, xq=xq, kh=kh, gh=gh)[0][0]  # 返回当前门课程的上课时间
    res = searchOnE(0, 0, 1, 1, xh=xh, xq=xq)
    for x in res:
        k=searchOnO(0, 0, 0, 1, xq=xq, kh=x[0], gh=x[1])
        if len(k)>0:
            time2 = k[0][0]
        else:time2=''
        if judgeclasstime(time1, time2) == False:
            return -2

    sql = "insert into e values('%s', '%s',	'%s', '%s', null, null, null)" % (xh, xq, kh, gh)
    flag, res = op_mysql(sql)
    if flag:
        return 1
    else:
        print(res)
        return 0


def searchCourse(xq, cnum=None, cname=None, tname=None, ctime=None):
    '''
    # 功能：查询已选课程

    # 接受参数：

    # 返回参数：

    '''
    kh = cnum
    if (kh is None or kh == '') and (cname and cname != ''):
        res = searchOnC(iskh=True, iskm=False, km=cname)
        if res:
            kh = res[0][0]
        else:
            return []

    gh = None
    if tname is not None and tname != '':
        res = searchOnT(isgh=True, isxm=False, xm=tname)
        if res:
            gh = res[0][0]
        else:
            return []

    res = searchOnO(xq=xq, kh=kh, gh=gh, sksj=ctime)
    ans = []
    for x in res:
        tmp = []
        tmp.append(x[0])  # 课号
        # 课名
        if cname:
            tmp.append(cname)
        else:
            tmp.append(searchOnC(iskh=False, iskm=True, kh=x[0])[0][0])
        # 教师号
        tmp.append(x[1])
        if tname:
            tmp.append(tname)
        else:
            tmp.append(searchOnT(isgh=False, isxm=True, gh=x[1])[0][0])
        # 上课时间
        tmp.append(x[2])
        ans.append(tmp)
    return ans


def showSelectCourse(usr, term, isstu=True):
    '''
    展示某学生已选修课程 在e表中进行课程查询 \n
    或者是某老师开设的所有课程 在o表中进行查询 \n
    参数 isstu 表示是学生查询还是老师查询 \n
    '''
    if isstu:
        sql = "select kh, gh from e where xh='%s' and xq = '%s'" % (usr, term)
        flag, res = op_mysql(sql)
        if flag == False or len(res) == 0:
            return []
        data = []
        for x in res:
            tmp = []
            tmp.append(x[0])  # 课号
            tmp.append(searchOnC(iskh=False, iskm=True, kh=x[0])[0][0])  # 课程名
            tmp.append(x[1])  # 工号
            tmp.append(searchOnT(isgh=False, isxm=True, gh=x[1])[0][0])  # 教师名
            tmp.append(searchOnO(iskh=False, isgh=False, issksj=True, xq=term, kh=x[0], gh=x[1])[0][0])  # 上课时间
            data.append(tmp)
        return data
    else:
        sql = "select kh from o where gh='%s' and xq='%s'" % (usr, term)
        flag, res = op_mysql(sql)
        if flag == False or len(res) == 0:
            return []
        data = []
        for x in res:
            tmp = []
            tmp.append(x[0])  # 课号
            tmp.append(searchOnC(iskh=False, iskm=True, kh=x[0])[0][0])  # 课程名
            tmp.append(searchOnO(iskh=False, isgh=False, issksj=True, xq=term, kh=x[0], gh=usr)[0][0])  # 上课时间
            data.append(tmp)
        return data


def finishedCourse(usr):
    '''
    查询某学生已经修过的课程
    定义: 总分大于60才能算修过
    '''
    sql = "select xq, kh, gh from e where xh = '%s' and (zpcj >= 60)" % (usr)
    flag, res = op_mysql(sql)
    if flag == False or len(res) == 0:
        return []
    data = []
    for x in res:
        tmp = []
        tmp.append(x[0])  # 学期
        tmp.append(x[1])  # 课号
        tmp.append(searchOnC(iskh=False, iskm=True, kh=x[1])[0][0])  # 课程名
        tmp.append(x[2])  # 工号
        tmp.append(searchOnT(isgh=False, isxm=True, gh=x[2])[0][0])  # 教师名
        tmp.append(searchOnO(iskh=False, isgh=False, issksj=True, xq=x[0], kh=x[1], gh=x[2])[0][0])  # 上课时间
        data.append(tmp)
    return data


def deleteOnO(xq, kh, gh, sksj):
    '''
    # 功能：在O表中删除一条记录

    # 接受参数：

    # 返回参数：

    '''
    sql = "SET FOREIGN_KEY_CHECKS=0"
    op_mysql(sql)

    sql = "delete from e where xq = '%s' and gh = '%s' and kh = '%s'" % (xq, gh, kh)
    op_mysql(sql)

    sql = "delete from o where xq = '%s' and kh = '%s' and gh = '%s' and   sksj = '%s'" % (xq, kh, gh, sksj)
    flag, e = op_mysql(sql)

    sql = "SET FOREIGN_KEY_CHECKS=1"
    op_mysql(sql)

    return flag, e


def deleteOnE(xh=None, xq=None, kh=None, gh=None):
    '''
    # 功能：从E表中删除一条记录

    # 接受参数：

    # 返回参数：

    '''
    jud = []
    jres = []
    if xh:
        jud.append("xh='%s'")
        jres.append(xh)
    if xq:
        jud.append("xq='%s'")
        jres.append(xq)
    if kh:
        jud.append("kh = '%s'")
        jres.append(kh)
    if gh:
        jud.append("gh = '%s'")
        jres.append(gh)
    jud = ' and '.join(jud)
    jres = tuple(jres)

    return delete('e', jud, jres)

def deleteOnT(xh=None, xq=None, kh=None, gh=None):
    '''
    # 功能：从E表中删除一条记录

    # 接受参数：

    # 返回参数：

    '''
    jud = []
    jres = []
    if xh:
        jud.append("xh='%s'")
        jres.append(xh)
    if xq:
        jud.append("xq='%s'")
        jres.append(xq)
    if kh:
        jud.append("kh = '%s'")
        jres.append(kh)
    if gh:
        jud.append("gh = '%s'")
        jres.append(gh)
    jud = ' and '.join(jud)
    jres = tuple(jres)

    return delete('t', jud, jres)

def deleteOnS(xh=None, xq=None, kh=None, gh=None):
    '''
    # 功能：从E表中删除一条记录

    # 接受参数：

    # 返回参数：

    '''
    jud = []
    jres = []
    if xh:
        jud.append("xh='%s'")
        jres.append(xh)
    if xq:
        jud.append("xq='%s'")
        jres.append(xq)
    if kh:
        jud.append("kh = '%s'")
        jres.append(kh)
    if gh:
        jud.append("gh = '%s'")
        jres.append(gh)
    jud = ' and '.join(jud)
    jres = tuple(jres)

    return delete('s', jud, jres)

def deleteOnC(xh=None, xq=None, kh=None, gh=None):
    '''
    # 功能：从E表中删除一条记录

    # 接受参数：

    # 返回参数：

    '''
    jud = []
    jres = []
    if kh:
        jud.append("kh = '%s'")
        jres.append(kh)

    jud = ' and '.join(jud)
    jres = tuple(jres)

    return delete('c', jud, jres)

def test():
    print('test')
    # print(register('1101', '123456', '123456', 'student'))
    # print(register('admin', '123456', '123456', 'admin'))
    # print(login('1101', '123456', 'student'))
    # print(login('admin', '123456', 'admin'))
    # print(searchOnO(xq='2012-2013秋季'))
    # print(searchOnS(xh='1101'))
    # print(getClassLists('2012-2013冬季', '08305002',	'0103'))
    # print(updateOnO('2012-2013秋季',	'08305001',	 '0102',	'星期三5-8', 30,
    # '2012-2013秋季', '08305002',	 '0102',	'星期三5-8', 25))
    # print(updateOnC(old_kh='08301011', new_kh='08301001'))
    # 08301001
    # print(insertOnInfo(1, '2013-2014冬季'))
    # print(updateOnInfo(1, '2013-2014冬季', new_yxh='01', new_sx=25))
    # print(searchOnInfo(flag=1)[0])
    # print(searchOnInfo(flag="1"))
    # for item in searchOnInfo(flag="1"):
    #     print(item[0])
    print(searchAll("D"))
    print(updateOnO)
    # print(insertOnS(2333,	'ss',	'男',	'1993-03-06',	'上海',	'13613005486',	'02'))
    # print(insertOnT('0233', 'ss', '男', '1973-03-06',	'副教授', 3567.00, '01'))
    # print(insertOnC('08305011',	'计算机体系结构',	4,	40,	'01'))
    # print(insertOnO('2012-2013秋季',	'08305001',	 '0103',	'星期三5-8', 20))
    # print(insertOnE(1106,	'2013-2014冬季',	'08302001',	'0201'))
    # print(deleteOnE(1107,	'2013-2014秋季',	'08305004',	'0101'))


if __name__ == "__main__":
    test()