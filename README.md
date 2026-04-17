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

# Sendo Colocado com Anaconda
Este tutorial vai mostrar como usar modelagem preditiva no editor Anaconda Online. Estamos eliminando a necessidade de instalações locais. O Anaconda Online utiliza Jupyter Notebooks integrados e gerenciamento de pacotes poderoso que facilita muito a execução de programas complexos, incluindo regressão linear.

Nota: Para usar o editor, certifique-se de ter criado uma conta gratuita.

Comece abrindo seu navegador e visitando o Anaconda Online.

Em seguida, faça login na sua conta para acessar a página inicial. Depois, selecione "Iniciar o Caderno" na seção "Code Online":

# Nossas Ferramentas de Escolha
Bibliotecas! Tem que amar eles. Neste tutorial, vamos usar as seguintes bibliotecas Python para análise de dados, visualização de dados e aprendizado de máquina:

🔢 O NumPy oferece uma base sólida para operações numéricas e análise de dados.
🐼 O Pandas permite que você analise, limpe, explore e manipule dados de diferentes fontes.
📈 O Matplotlib transforma seus dados em visuais atraentes, como gráficos 2D e gráficos de barras.
🤖 Scikit-learn, comumente conhecido como Sklearn, oferece uma interface amigável para todos os tipos de aprendizado de máquina.
Se você já se perguntou como gráficos de "previsão" são criados em Python, as chances são de que uma dessas 4 ferramentas tenha sido envolvida. Eles facilitam para iniciantes desbloquearem o poder do Python na ciência de dados.

Após lançar o Notebook no Anaconda, abra um novo projeto:

# Começando
Neste tutorial, usaremos um conjunto de dados que compara o tamanho e os preços das casas de propriedades recentemente vendidas no bairro Dumbo, no Brooklyn, para prever o custo das casas com base no tamanho.

Nota: Esses dados foram coletados do Zillow.

Para começar, vamos importar as bibliotecas. Lembre-se de que, como você está usando um emulador online, não há necessidade de instalações locais. Esta é uma configuração simples para regressão linear usando a biblioteca scikit-learn.

Para uma rápida atualização, importamos as seguintes bibliotecas:

numpy para operações numéricas (aliasadas como ).np
pandas para leitura e análise de dados (apelidos como ).pd
matplotlib.pyplot para plotar grafos dos dados (aliasados como ).plt
train_test_split de para treinar e testar o modelo.sklearn.model_selection
A classe de para implementar regressão linear.LinearRegressionsklearn.linear_model

Este arquivo CSV contém 59 pares de pontos de dados. Após o upload, vamos adicionar o seguinte código:

# Load data from CSV file
data = pd.read_csv('home_dataset.csv')
 
# Extract features and target variable
house_sizes = data ['HouseSize'].values
house_prices = data['HousePrice'].values

Estamos usando para ler o arquivo CSV. Em seguida, estamos extraindo os valores correspondentes às características na ficha técnica. Nesse caso, os dados da coluna chamada "HouseSize" estão sendo adicionados à variável.pd.read_csv()house_size

Vamos agora começar a plotar os dados via objeto do Matplotlib.plt

Primeiro, costumamos criar um gráfico de dispersão entre preços de casas e tamanho da casa. Em seguida, atribuímos um título e rótulos para os eixos x e y. Depois, usamos para exibir o gráfico.plt.scatter()plt.show()

# Teste de Trem
Agora que extraímos nossos dados e traçamos em um gráfico, é hora da parte da regressão linear.

Um teste de treinamento divide os dados gerados em conjuntos de treinamento e teste usando a função do Sklearn.train_test_split()

A divisão de teste de trem é um procedimento de validação de modelo comumente usado em aprendizado de máquina preditivo para simular como um modelo funcionará com dados novos/desconhecidos. É comumente usado em grandes conjuntos de dados ou quando você precisa de uma estimativa rápida.

Vamos agora acrescentar o seguinte:

O código acima divide os dados 80/20:

80% dos dados serão usados para treinar o algoritmo em e .x_trainy_train
Os outros 20% serão usados para testar o algoritmo em e .x_testy_test
Nessa próxima etapa, estamos criando e treinando o modelo para fazer previsões com o seguinte código:

Após preparar nossos dados para o Numpy com , podemos criar o modelo de regressão linear com e treiná-lo usando nossos and data..reshape()LinearRegression()x_trainy_train

# Previsão
O modelo que acabamos de treinar agora será capaz de fazer previsões no conjunto de teste e . Os resultados são armazenados na variável.x-testy-testpredictions

Agora vamos plotar nossos resultados a partir de nossa modelagem preditiva:

Com nosso objeto, usamos um gráfico de dispersão para visualizar os preços reais e previstos. Selecionar o botão "executar" mostrará os resultados com pontos azuis e uma linha de regressão vermelha:plt

# Conclusão
É isso, você agora treinou oficialmente e visualizou um algoritmo de modelagem preditiva!

Para levar suas habilidades ao próximo nível, considere buscar dados e utilizar regressão linear para visualização. O Kaggle é um ótimo lugar para encontrar conjuntos de dados que já foram comprovados, mas você também pode importar qualquer dado. Você pode usar a regressão linear para prever tantas coisas:

Vendas de videogames baseadas em avaliações.
Engajamento nas redes sociais baseado no crescimento de seguidores.
Notas baseadas no tempo de estudo, e até tempo de recuperação baseado em dados médicos.
As possibilidades são infinitas! Seja criativo e lembre-se de formatar seus dados para facilitar o acesso.

## Mais Recursos
Para aprendizado e exploração adicionais, aqui estão alguns recursos para aprofundar seu entendimento:

👀 Código-fonte deste tutorial.
📊 Conjuntos de Dados Kaggle: Explore conjuntos de dados diversos para diversos projetos de aprendizado de máquina.
🤖 Documentação Scikit-Learn: Mergulhe em informações detalhadas sobre aprendizado de máquina.
📖 Documentação Pandas: Saiba mais sobre manipulação e análise de dados.
📈 Documentação Matplotlib: Explore a documentação Matplotlib para criar visualizações cativantes.
Ciência de Dados
Intermediário
Python
