class Paciente:
    def __init__(self, id_paciente, nome, nivel_dor):
        self.id = id_paciente
        self.nome = nome
        self.nivel_dor = nivel_dor  # Prioridade (1 a 10)

    def __repr__(self):
        return f"[{self.nome} (Dor: {self.nivel_dor})]"


class TriagemMaxHeap:
    def __init__(self):
        self.heap = []
        # Mapeia o ID do paciente para o seu índice atual no array 'heap'
        self.posicao_paciente = {}

    def _subir(self, i):
        """Move o elemento para cima para manter a propriedade do Max-Heap."""
        while i > 0:
            pai = (i - 1) // 2
            if self.heap[i].nivel_dor > self.heap[pai].nivel_dor:
                # Troca os elementos no heap
                self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
                # Atualiza as posições no dicionário
                self.posicao_paciente[self.heap[i].id] = i
                self.posicao_paciente[self.heap[pai].id] = pai
                i = pai
            else:
                break

    def _descer(self, i):
        """Move o elemento para baixo para manter a propriedade do Max-Heap."""
        tamanho = len(self.heap)
        while 2 * i + 1 < tamanho:
            filho_esquerdo = 2 * i + 1
            filho_direito = 2 * i + 2
            maior = filho_esquerdo

            if filho_direito < tamanho and self.heap[filho_direito].nivel_dor > self.heap[filho_esquerdo].nivel_dor:
                maior = filho_direito

            if self.heap[maior].nivel_dor > self.heap[i].nivel_dor:
                # Troca os elementos
                self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
                # Atualiza as posições
                self.posicao_paciente[self.heap[i].id] = i
                self.posicao_paciente[self.heap[maior].id] = maior
                i = maior
            else:
                break

    def inserir_paciente(self, paciente):
        """Adiciona um novo paciente na fila de triagem."""
        self.heap.append(paciente)
        idx = len(self.heap) - 1
        self.posicao_paciente[paciente.id] = idx
        self._subir(idx)
        print(f"➕ {paciente.nome} deu entrada com nível de dor {paciente.nivel_dor}.")

    def atender_proximo(self):
        """Remove e retorna o paciente com maior dor (raiz do heap)."""
        if not self.heap:
            print("Fila vazia! Nenhum paciente para atender.")
            return None
        
        raiz = self.heap[0]
        ultimo_elemento = self.heap.pop()
        
        del self.posicao_paciente[raiz.id]

        if self.heap:
            self.heap[0] = ultimo_elemento
            self.posicao_paciente[ultimo_elemento.id] = 0
            self._descer(0)
            
        print(f"⚕️ Atendendo agora: {raiz.nome} (Dor: {raiz.nivel_dor})")
        return raiz

    def alterar_prioridade(self, id_paciente, novo_nivel_dor):
        """Meta do desafio: Modifica a dor de um paciente já na fila."""
        if id_paciente not in self.posicao_paciente:
            print("⚠️ Paciente não encontrado na fila de triagem.")
            return

        idx = self.posicao_paciente[id_paciente]
        paciente = self.heap[idx]
        dor_antiga = paciente.nivel_dor
        paciente.nivel_dor = novo_nivel_dor

        print(f"🔄 Atualizando {paciente.nome}: Dor foi de {dor_antiga} para {novo_nivel_dor}.")

        # Se a dor aumentou, tenta subir no heap. Se diminuiu, tenta descer.
        if novo_nivel_dor > dor_antiga:
            self._subir(idx)
        elif novo_nivel_dor < dor_antiga:
            self._descer(idx)

    def exibir_fila(self):
        print(f"📋 Fila atual (Representação do Heap): {self.heap}")


# --- SIMULAÇÃO DO CASO ---
if __name__ == "__main__":
    triagem = TriagemMaxHeap()

    # 1. Recebendo N pacientes
    p1 = Paciente(101, "Ana", 4)
    p2 = Paciente(102, "Bruno", 8)
    p3 = Paciente(103, "Carlos", 2)
    p4 = Paciente(104, "Daniela", 9)

    print("--- 🔴 CHEGADA DE PACIENTES ---")
    triagem.inserir_paciente(p1)
    triagem.inserir_paciente(p2)
    triagem.inserir_paciente(p3)
    triagem.inserir_paciente(p4)
    triagem.exibir_fila()
    print()

    # Meta: Ajustar a prioridade de um paciente na fila
    print("--- 🟡 META: ALTERANDO PRIORIDADES (Increase/Decrease Key) ---")
    # Caso 1: A dor do Carlos piorou muito (Increase Key)
    triagem.alterar_prioridade(103, 10) 
    triagem.exibir_fila()
    print()

    # Caso 2: A medicação inicial da Daniela fez efeito e a dor diminuiu (Decrease Key)
    triagem.alterar_prioridade(104, 3)
    triagem.exibir_fila()
    print()

    print("--- 🟢 ATENDIMENTO DOS PACIENTES ---")
    triagem.atender_proximo() # Deve ser o Carlos (Dor 10)
    triagem.atender_proximo() # Deve ser o Bruno (Dor 8)
    triagem.atender_proximo() # Deve ser a Daniela (Dor 3)
    triagem.atender_proximo() # Deve ser a Ana (Dor 4)