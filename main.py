#"coding=utf-8"
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options
import os.path
import temp
from Transform import tansform

#连接mysql数据库
import torndb
db = torndb.Connection(host = 'localhost',database ='stitp',user = 'root',password = 'testpassword')

from tornado.options import define, options

define("port", default=9000, type=int)#定义监听端口


class IndexHandler(tornado.web.RequestHandler):#主页类
    def get(self):
        self.render("index.html")
class TargetHandler(tornado.web.RequestHandler):#转换后显示结果
    def post(self):
        source=self.get_argument('source')
        res=tansform(source)
        temp.ss=source
        temp.rs=res
        self.render('target.html',re=res)

class SaveHandler(tornado.web.RequestHandler):#保存
    def get(self):
        sql="insert into weekpro (source,target) values ('%s','%s')"%(temp.ss,temp.rs)
        db.execute(sql)
        self.redirect('/')

class HistoryHandler(tornado.web.RequestHandler):#查看历史
    def get(self):
        sql="select * from weekpro"
        re=db.query(sql)
        self.render('history.html',re=re)

if __name__ == "__main__":#主函数
    settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    }#设置路径
    Handlers = [(r'/', IndexHandler),
                (r'/result',TargetHandler),
                (r'/save',SaveHandler),
                (r'/history',HistoryHandler)
                ]#设置路由
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=Handlers, **settings )
    http_sever = tornado.httpserver.HTTPServer(app)
    http_sever.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()