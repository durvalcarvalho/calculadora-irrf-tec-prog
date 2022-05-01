## Características

### Simplicidade

### Elegância

### Modularidade

### Boas interfaces

### Extensibilidade

### Ausência de duplicidades

### Portabilidade

### Idiomático

Uma base de código idiomática é um código que parece natural e fluente aos usuários que conhecem as capacidades, características e convençôes da linguagem. Por exemplo, um código idiomático jamais irá reimplementar rotinas já existêntes na linguagem, e sim, utilizar as APIs já existentes para realizar tais tarefas.

Para a base de código deste trabalho, foi utilizado a linguagem de programação Python. Deste modo, para avaliar se a base de código é ou não idiomática é preciso verificar se o software em questão está de acordo com o documento chamado "Zen do Python". O "Zen do Python" é um documento criado pelo criado da linguagem Python, o holandês Guido Van Rossum, onde é descrito os 19 valores que formaram a linguagem e que por consequência define o idioma da linguagem. Alguns destes valores são:

* Bonito é melhor que feio
* Explícito é melhor que implícito
* Simples é melhor que complexo
* Complexo é melhor que complicado
* Plano é melhor que aninhado
* Esparso é melhor que denso
* Ligibilidade conta
* Casos especiais não são especiais o bastantes para quebrar regras
* Praticidade é melhor que pureza
* Erros nunca devem passar silenciosamente.
* Erros somente podem passar silenciosamente se forem explicitamente silenciados.
* Diante da ambiguidade, recuse a tentação de adivinhar
* Deve haver somente um modo óbvio para fazer algo
* Se a implementação é difícil de explicar, é uma má ideia
* Se a implementação é fácil, pode ser uma boa ideia
* Namespaces são uma grande ideia, utilize-os

Além do documento "Zen do Python", a linguagem Python também possui um guia de estilo definido na [PEP 8](https://www.python.org/dev/peps/pep-0008/). O guia de estilo PEP 8 define os padrões de estilo de código Python, e é um documento que deve ser seguido para que o código seja escrito de forma idiomática. Algumas das definições feitas no guia de estilo PEP 8 são:

* Tabs ou espaços: Espaços são preferíveis, use tabulações somente se for para permanecer consistente com o códigos já existentes que usam tabulações.

* Identação: Python é uma linguagem de programação indentada, isto é, o espaçamento no começo de cada linha é avaliado pelo interpretador. O guia define que a identação deve ser de 4 espaços, a menos que se esteja trabalhando com um código-fonte que já foi indentado com outro espaçamento.

* Limitação no tamanho das linhas: O guia de estilo do Python sugere que blocos de código tenham ao máximo 79 caracteres, e que blocos de docstrings ou comentários tenham ao máximo 72 caracteres. Caso exista linhas maiores que o limite de caracteres sugerido, utilize o contra-barra ('\') para quebrar linhas.

* Codificação de caracteres: Sempre utilize UTF-8, a menos que a base de código existente já utilize outra codificação.

* Importações de módulos: Cada linha deve conter somente as importações de um somente módulo. Nunca importe vários módulos utilizando somente um import.

* Nome de variáveis e funções: Preferencialmente utilize snake_case para nomes de variáveis e funções. A menos que a base de código existente utilize outro padrão.

* Nome de calsses: Preferencialmente utilize CamelCase para nomes de classes. A menos que a base de código existente utilize outro padrão.

É possível fazer um paralelo entre os maus cheiros de código (code smells) com os códigos não idiomáticos. Como por exemplo:

* Long Method e Limitação no tamanho das linhas: Uma vez que o guia de estilo da linguagem sugere que as linhas tenham ao máximo 79 caracteres, e que geralmente entre 20 a 25 caracteres são utilizados pela palavra reservada `def` e pelos nomes dos parâmetros, o tamanho do nome da função fica reduziada a cerca ao no máximo 50 caracteres.

* Poor Names e Nome de variáveis, funções e classes: A linguagem python define um padrão claro de nomenclatura para suas variáveis, funções e classes, deste modo quando uma função está nomeada como uma classe ou vice-versa, é um sinal de mau cheiro de código.

* Inconsistency e Espaçamento, Identação e Codificação de caracteres: A linguagem pytho é clara quando define a quantidade de espaços que devem ser utilizados para identação, e a codificação de caracteres é sempre UTF-8. Deste modo, se em uma mesma base de código há trechos que são inconsistentes entre si quando analisamos na lente de espaçamento, identação e codificação de caracteres, é um sinal de mau cheiro de código.



### Boa documentação