## Características

### Simplicidade

A **Simplicidade** é a característica mais importante de um código bem escrito. Não só o código como também ter um design simples em qualquer projeto seja mobile, web ou desktop é muito importante para facilitar o entendimento do que está sendo criado para outra pesssoa.

Um código simples não quer dizer que é o menor, mas é o menor possível considerando a tecnologia, linguagem e bibliotecas utilizadas na construção do projeto.

Certa vez, Pascal disse:

> Sinto muito pela extensão da minha carta, mas não tive tempo de escrever uma curta.

Ou seja, fazer um código pequeno exige que o desenvolvedor esteja engajado nesse propósito, porque tanto o exagero de simplicidade quanto a ausência de simplicidade podem ser prejudiciais para a compreensão do projeto.

Para se alcançar um código simples é necessário evitar:

* Classes longas;
* Métodos longos;
* Parâmetros longos;
* Duplicação de código. 

Evitar esses maus-cheiros são essenciais para uma boa escrita de código, assim como _Martin Fowler_ define os maus-cheiros.

A refatoração realizada pode ser encontrada em: [Simplicidade](https://github.com/durvalcarvalho/calculadora-irrf-tec-prog/commit/8a85e683a6b14fa57cb6cd1f03f72ea59bd2573c)

### Modularidade

Desde a criação de um projeto é necessário dividir em partes chamadas módulos ou componentes da aplicação. O ideal é ir quebrando o projeto em partes cada vez menores até um ponto que seja saudável para o projeto.

Sempre é bom lembrar que mesmo que se separe o projeto em partes, todas elas são menos complexas que o problema original, mas juntas resolvem o problema inicial. Buscar uma qualidade dentro dessa quebra por módulos do projeto é bastante importante.

As chaves para uma boa modularidade são:

* Alta coesão, ou seja, ter funcionalidades que sejam bem relacionadas entre elas;
* Baixo acoplamento, que significa a interdependência entre os módulos.

Sempre que um módulo for devidamente identificado ele pode ser trabalhado e testado separadamente. Uma das vantagens da modularidade é a possibilidade de criação de testes unitários para qualidade do projeto.

Além disso, um projeto modularizado pode permitir a divisão de tarefas entre desenvolvedores, mas sempre tomando cuidado com a criação de etapas diferentes dentro da aplicação como um todo.

O importante é que a modularização seja equilibrada e baseada na solução do problema e não em elementos periféricos e externos à aplicação.

Um código bem modularizado, evita:

* A criação de códigos duplicados sem necessidade.
* A obsessão primitiva.
* O uso de instruções como um switch.
* Generalidade especulativa.

A refatoração realizada pode ser encontrada em: [Modularidade](https://github.com/durvalcarvalho/calculadora-irrf-tec-prog/commit/f14fd41fef85aeec39fda9996e51f62d4399b11d)

### Extensibilidade

Um dos principais princípios da extensibilidade é ter um código bem projetado que permite a criação de novas funcionalidades em arquivos e pastas apropriados. Um dos perigos é a criação de diversos ramos que gerem uma estrutura extremamente complexa, e que complica qualquer alteração ou manutenção no futuro.

A extensibilidade pode ser feita através da criação da hierarquia de classes, classes abstratas, com o fornecimento de funções de retorno de atributos de uma classe e com uma estrutura de pastas e arquivos que seja lógica e maleável para a aplicação.

Um ponto de atenção é a importância de não tentar ser extensível com todo o código para não criar algo mais complexo do que de fato é.

Ao estender o código é importante pensar em algo que seja escalável, ou seja, que funcione para as funcionalidades de agora e para as que serão criadas futuramente.

Quando for necessário acrescentar alguma funcionalidade em um código extensível, deve ser:

* Fácil de se alterar;
* Pontual;
* Não deve precisar que o desenvolvedor altere em diversos lugares causando uma mudança divergente.
* Não deve ser necessário buscar muitos atributos de outras classes que poderiam não ter sido criadas para a plena criação da funcionalidade.

A refatoração realizada pode ser encontrada em: [Extensibilidade](https://github.com/durvalcarvalho/calculadora-irrf-tec-prog/commit/f14fd41fef85aeec39fda9996e51f62d4399b11d)

### Ausência de duplicidades

Antes de entrar na descrição formal da **Ausência de duplicidades**, vale o destaque para um pequeno lema que descreve a ideia central da característica:

> *Faça apenas uma vez e faça bem. Evite duplicações.*

Um código bem projetado não possui duplicações de código, isto é, ele nunca repete a si mesmo em diferentes partes. A duplicação de código é a maior inimiga de um projeto de software simples e elegante. Um código desnecessariamente redundante traz consigo um crítico problema: dado dois trechos de código semelhantes, diferenciados apenas por detalhes, que apresentam um mesmo bug, é comum que desenvolvedores ajustem o bug apenas em um dos trechos de código e esqueçam do outro. Tal problemática se mostra como um obstáculo sólido à saúde de um código.

Boa parte da duplicação de código é proveniente de programações oriundas da técnica de *copiar e colar*, isto é, a partir de editores de texto, copiar trechos de código e colar em outras partes do sistema. A duplicação também pode surgir de projetos de software desnecessariamente complexos e que, por falta de conhecimento ou domínio do conteúdo por parte dos programadores responsáveis, acabam replicando o código diversas e diversas vezes.

Evitar a duplicação de código é uma atividade que sempre deve estar presente no desenvolvimento de software. Para tal, existem algumas recomendações que podem ajudar a conquistar um código objetivo e sem replicações:

* Caso seja notado trechos muito parecidos e que estão em diferentes partes do código, é recomendável que seja criada uma função de generalização do código. A partir da definição apropriada dos parâmetros, é possível condessar a lógica em apenas um trecho de código, além da responsabilidade única, agora a correção de erros também se concentra em apenas um local. Além do mais, a legibilidade do código é melhorada, já que agora é possível criar um nome significativo e que consiga descrever a etapa específica do código.
* Um sinal de duplicação de código são classes excessivamente similares. Tal ocasião é um indicativo de que alguma funcionalidade deveria estar em uma classe pai, ou até mesmo que uma camada de interface seja necessária para descrever o comportamento em comum.

A refatoração realizada pode ser encontrada em: [Ausência de duplicidades](https://github.com/durvalcarvalho/calculadora-irrf-tec-prog/commit/c461e5d578cf0459a1f3d87434b252477ee00b21)

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
* Casos especiais não são especiais o bastante para quebrar regras
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

A refatoração realizada pode ser encontrada em: [Idiomático](https://github.com/durvalcarvalho/calculadora-irrf-tec-prog/commit/556ec0b14a6f758f1641643b467e2a034992feb5)

### Boa documentação

É comum a crença que um código bem escrito não precisa de documentação, pois somente com o código é possível compreender o que ele faz. Porém, em bases de códigos muito grandes não é plausível a leitura da base completa, de todos os subsistemas, módulos, classes e funções. Deste modo é importante que exista um mínimo de documentação que possibilite a rápida compreensão do que cada componente de código faz.

Na linguagem python este tipo de documentação é denominada docstrings. As docstrings são strings especiais que são utilizadas no início dos módulos, classes, funções e métodos, com a finalidade de apresentar um rápido resumo do que o código faz. Nos módulos é apresentado uma descrição do que aquele módulo agrupa, nas classes é apresentado uma descrição da abstração que a classe faz, e suas principais funcionalidade. E nos métodos e funções é apresentado um resumo da função, assim como o parâmetros de entrada e o retorno da função.

Algumas convenções usadas nas docstrings são:

* A primeira linha deve sempre ser uma breve descrição, geralmente de somente uma frase, com o resumo da docstring.

* Se houver a necessidade de uma explicação mais detalhada, a segunda linha deve sempre ser em branco, e a explicação deve começar a partir da terceira linha.

* Se houver a necessidade de documentar os parâmetros, é sugerido que a documentação seja da seguinte forma:

```
def function_with_types_in_docstring(param1, param2):
    """
    Example function with types documented in the docstring. (Curto resumo)

    (Descrição longa)
    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    (Documentação dos argumentos)
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    (Documentação do retorno)
    Returns:
        bool: The return value. True for success, False otherwise.

    (Outras informações)
    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
```

Essa característica vai de encontro com o codesmell de excesso de documentários. Porém, como esses comentários não são documentários de rotinas de código, e sim documentação de projeto, é desejável que uma base de código seja bem documentada, ainda mais quando os padrões de documentação são respeitados.

A refatoração realizada pode ser encontrada em: [Boa Documentação](https://github.com/durvalcarvalho/calculadora-irrf-tec-prog/commit/5bad69420a0476fa78fbcd77fac631dd507d12fe)
