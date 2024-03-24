# Python Technical Challenge

Minhas considerações para a solução do desafio técnico.


## Question 1

Para a solução da primeira questão dois algoritmos foram propostos. O primeiro considerando a ordenação
dos contratos de forma decrescente, permitindo fácil acesso aos contratos com maiores valores.
Essa solução tem complexidade O(klogk), sendo k o número de contratos. 

Outra solução considera o uso de um heap para manter os n contratos de maior valor. Essa 
solução tem complexidade O(k) + O(nlogn), pois não é necessário ordernar os contratos de antemão,
mas é necessário manter uma estrutura (heap) com os n contratos de maior valor.

Para executar a solução, use o comando:

```
python src/question1.py
```

Um benchmark foi desenvolvido para demostrar o comportamento de ambas as soluções para diferentes valores de k. Para executá-lo, utilize:

```
python src/question1-benchmark.py
```

Os resultados da execução do benchmark são:
```
=============n=10=================
Método da Ordenação: 0.028 segundos
Método do Heap: 0.021 segundos     

=============n=100=================
Método da Ordenação: 0.027 segundos
Método do Heap: 0.021 segundos     

=============n=1000=================
Método da Ordenação: 0.027 segundos
Método do Heap: 0.029 segundos     

=============n=10000=================
Método da Ordenação: 0.028 segundos
Método do Heap: 0.078 segundos
```

Os dados demonstram que há uma ligeira vantagem para o algoritmo baseado em heap para valores de n menores. 
O algoritmo baseado em heap é em torno de 25% mais rápido para valores de n até 100. Porém,
ao aumentar os valores, vemos que nesse caso o algoritmo baseado em ordenação é até 35% mais rápido. 
Ambos os algoritmos podem trabalhar juntos para atender a cenários diferentes de forma mais eficiente.

## Question 2

O problema do agrupamento de pedidos em diversos caminhões é conhecido como Bin Packing. Este é um problema
conhecido e amplamente estudado, sendo um problema complexo (da classe de complexidade NP-HARD), 
e tendo diversas possíveis soluções, algumas com garantia de otimilidade outras não, que oferecem apenas aproximações.

Para executar a solução, use o comando:

```
python src/question2.py
```

Duas soluções foram propostas para esse problema. A primeira solução possui garantia de otimilidade em todos casos,
mesmo nos quais se relaxa a restrição de termos apenas dois items em cada remessa. Essa solução consiste na simulação
de todos os casos possíveis e nela ocorre uma explosão exponencial do número de casos à medida em que o número
de pedidos a ser considerado aumenta. 

A segunda solução utiliza uma aproximação, que é mais eficiente (complexidade O(n²)), porém sem as fortes garantias de otimalidade
em todos os cenários, sobretudo naqueles em que sejam permitidos mais do que 2 items em um mesmo caminhão. 
Observe que um dos testes irá falhar ao se executar o script. Se utilizarmos o algoritmo first-fit para o caso 
[5, 4, 3, 2, 2, 2, 2, 2], vemos que a solução 1 retorna o valor 2, enquanto a solução first-fit retorna o valor 3.

Esse exemplo sintético serve para ilustrar uma situação em que o first-fit irá prover uma solução não ótima. Se
temos os pedidos [5, 4, 3, 2, 2, 2, 2, 2] e podemos colocar até 4 elementos por caminhão (com um valor máximo de 12 por caminhão),
O algoritmo first-fit irá criar os grupos [[5, 4, 3], [2, 2, 2, 2], [2]]. Essa solução não é ótima, pois exige 3 viagens. A solução ótima é
[[5, 3, 2, 2], [4, 2, 2, 2]], que exige apenas duas e é encotrada pelo primeiro algoritmo.

Entretanto, a alta complexidade da solução ótima impossibilita sua utilização na maioria dos casos. Um pequeno aumento no tamanho do número de pedidos a ser
considerado irá aumentar em muito o tempo de execução desta solução. Podemos ver esse efeito nos resultados do benchmark.

```
=============num_orders=5=================
Método Ótimo: 0.00019 segundos
Método First-fit: 0.00000 segundos

=============num_orders=7=================
Método Ótimo: 0.01142 segundos
Método First-fit: 0.00001 segundos

=============num_orders=10=================
Método Ótimo: 11.83278 segundos
Método First-fit: 0.00001 segundos
```

Perceba o aumento expressivo de 0.00019 segundos para 11.83 segundos que ocorre quando dobramos o valor de pedidos de 5 para 10.
Este é um aumento de 62263 vezes no tempo de execução. Desta maneira, a solução first-fit, embora não ótima em todos os casos, 
pode ser uma das soluções viáveis para obter um desempenho aceitável à medida em que o número de pedidos a ser considerável aumenta.