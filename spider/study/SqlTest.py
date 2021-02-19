# Coding : utf-8
# Author : chyh
# Date   : 2021/2/14 0:31

from myTools import mySql

if __name__ == '__main__':
    result = mySql.MyPythonSql().query(sql="select * from POST_ID;")
    # result = mySql.MyPythonSql().insert(sql="insert into pythonTest(name) values('bbbbbbbb');")
    print(result)
