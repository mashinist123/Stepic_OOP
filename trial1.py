class Server:
    nums = [0]

    def __init__(self):
        self.IP = self.nums[-1] + 1
        self.nums.append(self.nums[-1] + 1)
        self.buffer = []
        self.link = None

    def send_data(self, data):
        if data.ip in self.link.buffer:
            self.link.buffer[data.ip] += ' ' + data.data
        else:
            self.link.buffer[data.ip] = data.data

    def get_data(self):
        s = []
        while self.buffer:
            s.append(self.buffer.pop())
        return s

    def get_ip(self):
        return self.IP


class Router:
    def __init__(self, c=None):
        if c is None:
            self.all_connections = {}
            self.buffer = {}

    def link(self, server):
        server.link = self  # Делаем ссылку на объект класса Роутер для каждого сервера после его подключения
        self.all_connections[server.IP] = server

    def unlink(self, server):
        del self.all_connections[server.get_ip]

    def send_data(self):
        while len(self.buffer):
            i = list(self.buffer.keys())[0]
            self.all_connections[i].buffer.append(self.buffer[i])
            del self.buffer[i]


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip









# router = Router()
# router.link(Server())
# s2 = Server()
# router.link(s2)
# print(s2.link)
# router.link(Server())
# print(router.all_connections)
# print(Server.nums)
# print(router.all_connections[3].link)
# s4 = Server()
# router.link(s4)
# print(s4.link)
# s4.send_data(Data('Hello Server', s2.get_ip()))
# s4.send_data(Data('The second message', s4.get_ip()))
# print(router.buffer)
#
# router.send_data()
# print(s4.get_data())
# print(router.buffer)



router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("HelloP", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
print('Outpute:', sv_to.buffer)
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(router.buffer)

print(msg_lst_from, msg_lst_to)
print(sv_to.buffer)

print('other task!!!!!11')
rb = {1:'sd', 2:'12d', 3:'asdfsd'}

print(rb)

# i = rb.keys()
#
# while len(rb):
#     i = list(rb.keys())[0]
#     print(rb[i])
#     del rb[i]
#     print(rb)