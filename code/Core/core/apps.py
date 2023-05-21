import pkg_resources
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
    plugini_ucitavanje = []
    plugini_vizualizacija = []

    def ready(self):
        self.plugini_ucitavanje = load_plugins("parse")
        self.plugini_vizualizacija = load_plugins("visualization") #TODO: promeniti ovo u pluginima
        print("AAAAAAAAA")
        print("br ucitavanje",len(self.plugini_ucitavanje))
        print("br visual", len(self.plugini_ucitavanje))

def load_plugins(group_tag):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=group_tag):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        print(group_tag)
        plugin = p()
        plugins.append(plugin)
    return plugins
