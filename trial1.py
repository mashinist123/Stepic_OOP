class Server:
    nums = [0]

    def __init__(self):
        self.IP = self.nums[-1] + 1
        self.nums.append(self.nums[-1] + 1)
        self.buffer = []
        self.link = None

    def send_data(self, data):
        self.link.buffer[data.ip] = self.link.buffer.get(data.ip, []) + [data.data]


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
            self.all_connections[i].buffer.extend(self.buffer[i])
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


assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router,
                                                                         'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server,
                                                                                'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"

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
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(msg_lst_from[0])
print(len(msg_lst_to))
print(msg_lst_to[0])
assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"

assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

assert msg_lst_from[0].data == "Hi" and msg_lst_to[
    0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

assert hasattr(router, 'buffer') and hasattr(sv_to,
                                             'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"

router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"
