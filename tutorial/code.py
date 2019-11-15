import web
render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/add', 'add'
)

db = web.database(
        dbn='postgres',
        host='127.0.0.1',
        port=5432,
        user='postgres',
        pw='proton09',
        db='test',
)

class index:
    def GET(self):
       todos = db.select('todo')
       return render.index(todos)
       
class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
