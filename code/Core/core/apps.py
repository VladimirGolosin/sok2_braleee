import pkg_resources
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
    plugini_ucitavanje = []
    plugini_vizualizacija = []
    ucitani_grafovi = []
    trenutni_iscrtan_graf = None
    trenutni_graf = None
    trenutni_vizualizator = None

    def ready(self):
        self.plugini_ucitavanje = load_plugins("parsiranje")
        self.plugini_vizualizacija = load_plugins("vizualizacija")
        print("#### Plugini ####")
        print("ucitavanje", len(self.plugini_ucitavanje))
        print("visual", len(self.plugini_vizualizacija))


def load_plugins(group_tag):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=group_tag):
        p = ep.load()
        # print("{} {}".format(ep.name, p))
        # print(group_tag)
        plugin = p()
        plugins.append(plugin)
    return plugins
