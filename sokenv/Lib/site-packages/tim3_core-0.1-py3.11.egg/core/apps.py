import pkg_resources
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
    plugini_ucitavanje = []
    plugini_vizualizacija = []

    def ready(self):
        self.plugini_ucitavanje = load_plugins("tim03.ucitavanje")
        self.plugini_vizualizacija = load_plugins("tim03.vizualizacija") #TODO: promeniti ovo u pluginima

def load_plugins(oznaka):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins
