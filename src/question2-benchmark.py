import timeit
import random
from question2 import Orders

# Criando um conjunto de pedidos para teste
def generate_random_orders(num_orders):
    orders = []
    for i in range(num_orders):
        orders.append(random.randint(1, 100))
    return orders

# Execução de benchmark
def benchmark():

    # Número de pedidos no teste
    num_orders_cases = [5, 7, 10]

    # Excutando 5 iterações
    num_iterations = 5
   
    for num_orders in num_orders_cases:
        
        orders = generate_random_orders(num_orders)

        total_time_method1 = 0
        total_time_method2 = 0
        
        # Calculando a média de vários iterações
        for _ in range(num_iterations):
            # Método com garantia de otimalidade
            start_time = timeit.default_timer()
            Orders(2).combine_orders(orders, 100)
            end_time = timeit.default_timer()
            total_time_method1 += (end_time - start_time)

            # Método first fit
            start_time = timeit.default_timer()
            Orders(2).combine_orders_first_fit(orders, 100)
            end_time = timeit.default_timer()
            total_time_method2 += (end_time - start_time)

        # Calculando tempo médio
        avg_time_method1 = total_time_method1 / num_iterations
        avg_time_method2 = total_time_method2 / num_iterations

        print(f"=============num_orders={num_orders}=================")
        print(f"Método Ótimo: {avg_time_method1:.5f} segundos")
        print(f"Método First-fit: {avg_time_method2:.5f} segundos")
        print()


# Executar benchmark
if __name__ == '__main__':
    benchmark()