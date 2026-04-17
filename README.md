# prever-precos-de-casas-com-regressao-linear

# Introdução
Você já quis saber quanto custa alugar ou possuir um apartamento ou casa na sua região? Como aprendizado de máquina e estatística funcionam com uma linguagem de programação poderosa como Python?

Aprendizado de máquina é um campo importante que permite que computadores absorvam dados e aprendam padrões para fazer previsões e decisões. Vamos usar Python para aprender sobre um dos fundamentos da modelagem preditiva em aprendizado de máquina e, mais especificamente, regressão linear. Para nos ajudar, vamos usar algumas bibliotecas de ciência de dados:

NumPy
Pandas
Matplotlib
Scikit-learn
# Regressão linear
Em estatística, a regressão linear é usada para modelar relações entre variáveis x independentes (por exemplo, tamanhos de casas) e uma variável y dependente (por exemplo, preços de imóveis) ajustando uma equação linear aos dados observados. Simplificando, estamos traçando uma linha reta através de um conjunto de dados para mapear e prever. Em ciência de dados, a regressão linear é amplamente utilizada para tarefas como prever vendas, analisar tendências econômicas e entender o impacto das variáveis em um resultado.

Neste tutorial, vamos criar um modelo de regressão linear para prever os preços das casas com base no tamanho das casas. Usando um gráfico de dispersão dos dados de teste, o modelo forma uma relação entre as duas variáveis e então faz previsões.

Bibliotecas! Tem que amar eles. Neste tutorial, vamos usar as seguintes bibliotecas Python para análise de dados, visualização de dados e aprendizado de máquina:

🔢 O NumPy oferece uma base sólida para operações numéricas e análise de dados.
🐼 O Pandas permite que você analise, limpe, explore e manipule dados de diferentes fontes.
📈 O Matplotlib transforma seus dados em visuais atraentes, como gráficos 2D e gráficos de barras.
🤖 Scikit-learn, comumente conhecido como Sklearn, oferece uma interface amigável para todos os tipos de aprendizado de máquina.
Se você já se perguntou como gráficos de "previsão" são criados em Python, as chances são de que uma dessas 4 ferramentas tenha sido envolvida. Eles facilitam para iniciantes desbloquearem o poder do Python na ciência de dados.

# Começando
Neste tutorial, usaremos um conjunto de dados que compara o tamanho e os preços das casas de propriedades recentemente vendidas no bairro Dumbo, no Brooklyn, para prever o custo das casas com base no tamanho.

Nota: Esses dados foram coletados do Zillow.
