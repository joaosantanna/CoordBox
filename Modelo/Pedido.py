"""
Classe pedido , guarda os dados de cada pedido cadastrado no sistema

"""

from datetime import date


class Pedido:

    def __init__(self, nome, matricula='', email='', telefone='', whatsapp=False,
                 prioridade=1, anamnese='', encaminhamento=''):
        self.__nome = nome
        self.__matricula = matricula
        self.__email = email
        self.__telefone = telefone
        self.__whatsapp = whatsapp
        self.__prioridade = prioridade
        self.__anamnese = anamnese
        self.__encaminhamento = encaminhamento
        self.__data_abertura = date.today()
        self.__status = 'Novo'

    @property
    def nome(self):
        return self.__nome

    @property
    def data_abertura(self):
        return self.__data_abertura

    def modificar(self, nome, status, whatsapp, prioridade, matricula='', email='',
                  telefone='', anamnese='', encaminhamento=''):
        self.__nome = nome
        self.__matricula = matricula
        self.__email = email
        self.__telefone = telefone
        self.__whatsapp = whatsapp
        self.__prioridade = prioridade
        self.__anamnese = anamnese
        self.__encaminhamento = encaminhamento
        self.__status = status

    def print(self):
        print(self.__nome)
        print(self.__matricula)
        print(self.__email)
        print(self.__telefone)
        print('WhatsApp:', self.__whatsapp)
        print(self.__anamnese)
        print(self.__encaminhamento)
        print('data abertura:', self.data_abertura.day, '/', self.data_abertura.month)
        print(self.__prioridade)
        print(self.__status)
        print('===================')


# testes locais
p = Pedido('Bruno', '1234', 'bruno@hotmail.com', '3245-0987', True, 2)
p.print()
p.modificar('Mario', 'Em andamento', True, 2)
p.print()

# TODO: os contatos devem virar uma classe no futuro para poder ser buscada na hora de adicionar novo contato
