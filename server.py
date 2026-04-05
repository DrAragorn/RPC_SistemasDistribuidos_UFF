import rpyc
from rpyc.utils.server import ThreadedServer


class MyService(rpyc.Service):
    def on_connect(self, conn):
        print('Cliente conectado')
    def on_disconnect(self, conn):
        print('Cliente desconectado')
    def exposed_get_answer(self):
        return 42
    exposed_the_real_answer_though = 43
    def get_question(self):
        return 'Qual é a cor do cavalo branco de Napoleão?'


if __name__ == '__main__':
    server = ThreadedServer(MyService, port=18861)
    server.start()