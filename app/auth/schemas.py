
class ModuleSchema:
    def __init__(self, module, views=None):
        self.module = module

        if not views:
            self.views = []
        else:
            self.views = views

    def dump(self):
        serialize = {
            'id': self.module.idmodulo,
            'name': self.module.nombre,
            'views': []
        }
        views = list(map(lambda view: {'id': view.idvista, 'name': view.nombre}, self.views))
        serialize['views'] = views
        return serialize
