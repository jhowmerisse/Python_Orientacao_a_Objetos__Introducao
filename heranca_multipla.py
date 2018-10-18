class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Tarefas Funcionario')

class Empresa1(Funcionario):
    def mostrar_tarefas(self):
        print('Tarefas da Empresa1')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Empresa2(Funcionario):
    def mostrar_tarefas(self):
        print('Tarefas da Empresa2')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
    def __str__(self):
        return f'Hipster,  {self.nome}'

class Junior(Empresa2):
    pass

class Pleno(Empresa2, Empresa1, Hipster):
    pass



jose = Junior('José')
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()

Maria = Pleno('Maria')
Maria.busca_perguntas_sem_resposta()
Maria.busca_cursos_do_mes()

Maria.mostrar_tarefas()

print(Maria)
