#coding=utf-8
#python调用外部程序
import subprocess
pname="D:\Microsoft Visual Studio\MyProjects\weekPro\Debug\weekPro.exe"


def tansform(source):
    leng=len(source)#获取长度
    ss=source.encode('ascii')#转为二进制
    p = subprocess.Popen(pname, stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    result=p.communicate(input=ss)#打开，并通信
    res=result[0].decode()[0:leng]#获取结构，并处理
    return res