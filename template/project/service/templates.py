from . import base, routes


class IndexTemplate(base.NormalBase):
    def get(self):
        return self.render("index.html")

routes.append((r'/', IndexTemplate))

