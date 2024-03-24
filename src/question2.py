class Orders:
    def __init__(self, max_itens_in_bins):
        self.max_itens_in_bin = max_itens_in_bins

    def combine_orders(self, requests, n_max):
        
        arrangements = []

        # Criando todas os arranjos possiveis para ordem de envio dos pedidos
        self.generate_arrangements(requests, [], arrangements)
        
        # O número mínimo de viagens inicial é a quantidade de pedidos
        minTravels = len(requests)

        # Verificando resto da divisão entre o número de items 
        # e quantidade máxima de elementos em cada bin
        remainder = len(requests) % self.max_itens_in_bin
        
        # Para cada arranjo, calcular o número de viagem
        for arrangement in arrangements:
            
            travels = 0

            # Caso dois pedidos consecutivos tenham
            # valor maior que n_max, duas viagens são 
            # necessárias para levar cada um, senão apenas uma.            
            for i in range(0, len(arrangement) - 1, self.max_itens_in_bin):
                size = sum(arrangement[i:i + self.max_itens_in_bin])
                travels += 2 if size > n_max else 1

            # Adicionando o os itens restantes
            travels += remainder

            # Se o número de viagens para o arranjo for
            # menor do que qualquer outro número de viagens
            # para outro arranjo já visto
            minTravels = min(minTravels, travels)
            
        return minTravels
        
    # Método recursivo que gera todas os possíveis arranjos de pedidos
    def generate_arrangements(self, items: list[int], current: list[int], arrangements: list[list[int]]):
        
        # Caso base, há apenas um elemento em items
        # Adicione na lista atual como o último
        # elemento do arranjo.
        if len(items) == 1:
            currentCopy = current.copy()
            currentCopy.append(items[0])
            arrangements.append(currentCopy)
            return

        # Itere pelos itens, o remova da lista
        # e chame generate_arrangements de forma
        # recursiva para gerar todas as combinações 
        # possíveis
        for i in range(len(items)):
            itensCopy = items.copy()
            item = itensCopy.pop(i)
            curentCopy = current.copy()
            curentCopy.append(item)
            self.generate_arrangements(itensCopy, curentCopy, arrangements)


    # Solução alternativa considerando o algoritmo first fit
    # Esta solução é mais rápida mas não garante otimalidade em todos os casos.
    def combine_orders_first_fit(self, requests, n_max):

        # Ordenando requests
        requests.sort(reverse=True)
        
        # Inicializando bins
        bins = []
        
        # Iterando por todos os requests
        for request in requests:
            
            # Considerando que o request não se encaixa 
            # em um bin
            fit = False

            # Para cad bin            
            for bin in bins:
                has_space_in_bin = sum(bin) + request <= n_max
                has_capacity_in_bin = len(bin) < self.max_itens_in_bin

                # Caso tenha espaço no bin
                # incluir request e finalizar busca.
                # Mudar flag fit para True
                if has_space_in_bin and has_capacity_in_bin:
                    bin.append(request)
                    fit = True
                    break
            
            # Se não foi possível encaixar o request
            # em nenhum bin, incluir novo
            if not fit:
                bins.append([request])

        return len(bins)

if __name__ == '__main__':
  
    #orders = [70, 30, 10]
    k_max_cases = [2, 2, 2, 2, 4]
    n_max_cases = [100, 100, 100, 100, 12]
    orders_cases = [
        [70, 30, 10], 
        [70, 30, 80, 20, 100, 90, 10],
        [30, 35, 45, 55, 44, 5], 
        [80, 90, 75, 88, 26, 91], 
        [5, 4, 3, 2, 2, 2, 2, 2]
    ]
    expected_orders_cases = [2, 4, 3, 6, 2]

    for k, n, orders, expected in zip(k_max_cases, n_max_cases, orders_cases, expected_orders_cases):

        how_many_1 = Orders(k).combine_orders(orders, n)
        how_many_2 = Orders(k).combine_orders_first_fit(orders, n)
        
        print("===============================")
        print(how_many_1, ' == ', expected)
        assert how_many_1 == expected
        print(how_many_2, ' == ', expected)
        assert how_many_2 == expected
        print()