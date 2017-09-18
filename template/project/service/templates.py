from . import base, route


@route(r'/')
class IndexTemplate(base.NormalBase):
    def get(self):
        return self.render("index.html")

