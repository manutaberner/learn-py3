import web

urls = (
    '/', 'home'
)

render = web.template.render('views/templates', base='MainLayout')
app = web.application(urls, globals())

#Classes/routes

class home:
    def GET(self):
        return render.home()

if __name__ == '__main__':
    app.run()