import heapq

class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)
    
    def __lt__(self, other):
        return self.debt < other.debt

class Contracts:
    
    def get_top_N_open_contracts(
        self, 
        open_contracts: list[Contract], 
        renegotiated_contracts: list[int],
        top_n: int
    ) -> list[int]:

        # Utilizando um conjunto para evitar múltiplas buscas sequenciais
        renegotiated_contracts_set = set(renegotiated_contracts)

        # Filtrando contratos já renegociados
        filtered_open_contracts = [
            contract for contract in open_contracts if contract.id not in renegotiated_contracts_set
        ]

        # Ordenando os contratos de forma decrescente com base no valor da dívida 
        open_contracts_sorted = sorted(filtered_open_contracts, key=lambda c: c.debt, reverse=True)

        # Usando operador slice para obter os N primeiros contratos
        return [contract.id for contract in open_contracts_sorted[:top_n]]
    

    def get_top_N_open_contracts_alternative(
        self, 
        open_contracts: list[Contract], 
        renegotiated_contracts: list[int],
        top_n: int
    ) -> list[int]:
        
        # Utilizando um conjunto para evitar múltiplas buscas sequenciais
        renegotiated_contracts_set = set(renegotiated_contracts)

        # Filtrando contratos já renegociados
        filtered_open_contracts = [
            contract for contract in open_contracts if contract.id not in renegotiated_contracts_set
        ]

        # Utilizando uma heap para manter os top N elementos
        heap = []
        heapq.heapify(heap)

        # Iterando pelos contratos (não ordenados)        
        for open_contract in filtered_open_contracts:
            # Caso existam menos que N elementos no heap, adicionar
            if len(heap) < top_n:
                heapq.heappush(heap, open_contract)
                continue
                
            # Caso o menor elemento do heap, seja menor que o contrato atual,
            # remover o menor e adicionar o atual
            smaller_in_heap = heap[0]    
            if open_contract.debt > smaller_in_heap.debt:
                heapq.heappop(heap)
                heapq.heappush(heap, open_contract)

        
        # Retornando conteúdo do heap ordenado
        heap.sort()
        return [contract.id for contract in reversed(heap)]



if __name__ == '__main__':
 
    n_cases = [3, 4, 1, 0, 5]
    renegotiated_cases = [[3], [1, 2], [4, 5], [1], []]
    contracts_cases = [[Contract(i, i) for i in range(1, 6)]] * 5
    expected_cases = [[5, 4, 2], [5, 4, 3], [3], [], [5, 4, 3, 2, 1]]

    for n, renegotiated, contracts, expected in zip(n_cases, renegotiated_cases, contracts_cases, expected_cases):
        actual = Contracts().get_top_N_open_contracts(contracts, renegotiated, n)            
        print(actual, " == ", expected)
        assert actual == expected
    