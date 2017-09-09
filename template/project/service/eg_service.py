from . import base, routes
from ..model.eg_model import Hello


class HelloService(base.NormalBase):
    def get(self):
        self.logger.info("Tornado Said Hi ~")
        self.logger.error("You Should Not Use This Part!")
        return self.write(Hello().say())

routes.append((r'/hello', HelloService))

