class AppStore:
    amount = []

    def add_application(self, app):
        self.amount.append(app)

    def remove_application(self, app):
        self.amount.remove(app)

    def block_application(self, app):
        i = self.amount.index(app)
        self.amount[i].blocked = True

    def total_apps(self):
        return len(self.amount)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked



# store = AppStore()
# app_youtube = Application("Youtube")
# app_youtube2 = Application("SAP")
# app_youtube3 = Application("Torrent")
# store.add_application(app_youtube)
# store.add_application(app_youtube2)
# store.add_application(app_youtube3)
# store.block_application(app_youtube2)
# print(app_youtube2.blocked)
# print(app_youtube3.blocked)
# print(store.total_apps())
# store.remove_application(app_youtube)
#
# store2 = AppStore
# print(store2.amount)


# print(AppStore.amount)


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