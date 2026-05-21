class Paciente:
    def __init__(self, nome, dor):
        self.nome = nome
        self.dor = dor

    def __repr__(self):
        return f"{self.nome} - dor {self.dor}"


class MaxHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, paciente):
        self.heap.append(paciente)
        self._subir(len(self.heap) - 1)

    def atender(self):
        if not self.heap:
            return None

        maior_prioridade = self.heap[0]
        ultimo = self.heap.pop()

        if self.heap:
            self.heap[0] = ultimo
            self._descer(0)

        return maior_prioridade

    def alterar_prioridade(self, nome, nova_dor):
        for i, paciente in enumerate(self.heap):
            if paciente.nome == nome:
                dor_antiga = paciente.dor
                paciente.dor = nova_dor

                if nova_dor > dor_antiga:
                    self._subir(i)
                else:
                    self._descer(i)

                return True

        return False

    def _subir(self, i):
        while i > 0:
            pai = (i - 1) // 2

            if self.heap[i].dor <= self.heap[pai].dor:
                break

            self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
            i = pai

    def _descer(self, i):
        tamanho = len(self.heap)

        while True:
            maior = i
            esquerda = 2 * i + 1
            direita = 2 * i + 2

            if esquerda < tamanho and self.heap[esquerda].dor > self.heap[maior].dor:
                maior = esquerda

            if direita < tamanho and self.heap[direita].dor > self.heap[maior].dor:
                maior = direita

            if maior == i:
                break

            self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
            i = maior

    def mostrar_fila(self):
        print(self.heap)


fila = MaxHeap()

n = int(input("Digite a quantidade de pacientes: "))

for i in range(n):
    nome = input(f"Nome do paciente {i + 1}: ")
    dor = int(input("Nível de dor de 1 a 10: "))

    while dor < 1 or dor > 10:
        dor = int(input("Valor inválido. Digite dor de 1 a 10: "))

    fila.inserir(Paciente(nome, dor))

print("\nFila inicial:")
fila.mostrar_fila()

nome = input("\nDigite o nome do paciente para alterar prioridade: ")
nova_dor = int(input("Novo nível de dor de 1 a 10: "))

if fila.alterar_prioridade(nome, nova_dor):
    print("\nPrioridade alterada com sucesso.")
else:
    print("\nPaciente não encontrado.")

print("\nFila após alteração:")
fila.mostrar_fila()

print("\nOrdem de atendimento:")
while fila.heap:
    print(fila.atender())