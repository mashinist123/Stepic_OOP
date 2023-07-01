class AppStore:

    app = {}

    def add_application(self, app):
        self.app[app.name] = app

    def remove_application(self, app):
        del self.app[app.name]

    def block_application(self, app):
        self.app.get(app.name).blocked = True

    def total_apps(self):
        return len(self.app)


class Application:

    def __init__(self, name, blocked = False):
        self.name = name
        self.blocked = blocked



store = AppStore()
app_youtube = Application("Youtube")
app_youtube2 = Application("SAP")
app_youtube3 = Application("Torrent")
store.add_application(app_youtube)
store.add_application(app_youtube2)
print(store.app)
store2 = AppStore()
store2.add_application(app_youtube3)
print(store2.app)


print(AppStore.app)


class color:
    lst = (1, 2, 3)

    def adding(self, obj):
        self.lst += obj,

a = color()
a.lst = 2
print(a.lst)
b = color()
c = color()
b.adding(3)
c.adding(4)
print(b.lst)
print(color.lst)



'''Versionn #2 more properly'''


class AppStore:
    amount = tuple()

    def add_application(self, app):
        self.amount += (app,)

    def remove_application(self, app):
        self.amount = tuple(x for x in self.amount if x != app)

    @staticmethod
    def block_application(app):
        app.blocked = True

    def total_apps(self):
        return len(self.amount)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked