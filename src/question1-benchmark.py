import timeit
import random
from question1 import Contracts, Contract

# Criando um conjunto de contratos para teste
def generate_random_contracts(num_contracts):
    contracts = []
    for i in range(num_contracts):
        contracts.append(Contract(i, random.randint(1, 100)))
    return contracts

# Execução de benchmark
def benchmark():

    # Número de contratos no teste
    num_contracts = 100_000

    # Fazendo com que 10% dos contratos sejam renegociados em média
    renegotiated_contracts = random.sample(range(num_contracts), num_contracts // 10)
    contracts = generate_random_contracts(num_contracts)
    contracts_instance = Contracts()

    # Excutando 100 iterações
    num_iterations = 100
   
    for n in [10, 100, 1000, 10_000]:

        total_time_method1 = 0
        total_time_method2 = 0
        
        # Calculando a média de vários iterações
        for _ in range(num_iterations):
            # Método com ordenação dos contratos
            start_time = timeit.default_timer()
            contracts_instance.get_top_N_open_contracts(contracts, renegotiated_contracts, n)
            end_time = timeit.default_timer()
            total_time_method1 += (end_time - start_time)

            # Method utilizando heap para manter top n
            start_time = timeit.default_timer()
            contracts_instance.get_top_N_open_contracts_alternative(contracts, renegotiated_contracts, n)
            end_time = timeit.default_timer()
            total_time_method2 += (end_time - start_time)

        # Calculando tempo médio
        avg_time_method1 = total_time_method1 / num_iterations
        avg_time_method2 = total_time_method2 / num_iterations

        print(f"=============n={n}=================")
        print(f"Método da Ordenação: {avg_time_method1:.3f} segundos")
        print(f"Método do Heap: {avg_time_method2:.3f} segundos")
        print()


# Executar benchmark
if __name__ == '__main__':
    benchmark()