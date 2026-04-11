import rpyc
import sys
import time


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('Usage {} SERVER'.format(sys.argv[0]))
    server = sys.argv[1]
    conn = rpyc.connect(server, 18861)

    # Questão 1
    print(conn.root)
    print(conn.root.get_answer())
    print(conn.root.the_real_answer_though)

    """
    #Questão 2
    print(conn.get_question())
    
    #Questão 3
    num = int(input('Por favor entre o tamanho da lista de números: '))
    vector = list(range(num))
    sum_vec = conn.root.get_sum(vector)
    print(f'A soma de todos os valores da lista é {sum_vec}')
    """

    #Questão 4
    num = int(input('Por favor entre o tamanho da lista de números: '))
    start = time.time()
    vector = list(range(num))
    sum_vec = conn.root.get_sum(vector)
    end = time.time()
    print(f'A soma de todos os valores da lista é {sum_vec}\nDuração da execução do get_sum(): {end-start}  seconds')