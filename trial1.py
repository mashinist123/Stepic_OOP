class Server:
    nums = [0]

    def __init__(self):
        self.IP = self.nums[-1] + 1
        self.nums.append(self.nums[-1] + 1)
        self.s_bufer = []
        self.link = None

    def send_data(self, data):
        self.link.r_bufer[data.ip] = data.data

    def get_data(self):
        if self.s_bufer:
            return self.s_bufer
        else:
            self.s_bufer = []

    def get_ip(self):
        return self.IP


class Router:
    def __init__(self, c=None):
        if c is None:
            self.all_connections = {}
            self.r_bufer = {}

    def link(self, server):
        server.link = self  # Делаем ссылку на объект класса Роутер для каждого сервера после его подключения
        self.all_connections[server.IP] = server

    def unlink(self, server):
        del self.all_connections[server.get_ip]

    def send_data(self):
        while len(self.r_bufer):
            i = list(self.r_bufer.keys())[0]
            # for i, x in self.r_bufer.items():
            self.all_connections[i].s_bufer.append(self.r_bufer[i])
            del self.r_bufer[i]


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip









router = Router()
router.link(Server())
s2 = Server()
router.link(s2)
print(s2.link)
router.link(Server())
print(router.all_connections)
print(Server.nums)
print(router.all_connections[3].link)
s4 = Server()
router.link(s4)
print(s4.link)
s4.send_data(Data('Hello Server', s2.get_ip()))
s4.send_data(Data('The second message', s4.get_ip()))
print(router.r_bufer)

router.send_data()
print(s4.get_data())
print(router.r_bufer)



# sv_from = Server()
# sv_from2 = Server()
# router.link(sv_from)
# router.link(sv_from2)
# router.link(Server())
# router.link(Server())
# sv_to = Server()
# router.link(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))
# sv_to.send_data(Data("Hi", sv_from.get_ip()))
# router.send_data()
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()
#
# print(msg_lst_from, msg_lst_to)

# print('other task!!!!!11')
# rb = {1:'sd', 2:'12d', 3:'asdfsd'}
# i = rb.keys()
#
# while len(rb):
#     i = list(rb.keys())[0]
#     print(rb[i])
#     del rb[i]
#     print(rb)