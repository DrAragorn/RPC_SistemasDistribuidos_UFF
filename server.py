import rpyc
from rpyc.utils.server import ThreadedServer
import time


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
    
    """
    # Questão 3
    def exposed_get_sum(self, vector):
        return sum(vector)
    """

    # Questão 4
    def exposed_get_sum(self, vector):
        start = time.time()
        sum_vec = sum(vector)
        end = time.time()
        print(f'Duração da execução do get_sum(): {end-start} seconds')
        return sum_vec


if __name__ == '__main__':
    server = ThreadedServer(MyService, port=18861)
    server.start()