#Sistema para visualizar o valor de um imóvel em determinada região, utilizando aprendizado de máquina, python e estatística.

#O aprendizado de máquina vai ser utilizado para que o computador absorva dados e aprenda padrões para fazer previsões e decisões. O python vai ser utilizado para aprender fundamentos de modelagem preditiva em aprendizado de máquina e regressão linear.

#Bibliotecas utilizadas:

NumPy
Pandas
Matplotlib
Scikit-learn

#Regressão linear:

É o traçar de uma linha reta através de um conjunto de dados para mapear e prever. Na ciência de dados utilizamos para tarefas de previsão, analise de tendências e para entender o impacto das variáveis em um resultado.





#O NumPy oferece uma base sólida para operações numéricas e análise de dados.
#O Pandas permite que você analise, limpe, explore e manipule dados de diferentes fontes.
#O Matplotlib transforma seus dados em visuais atraentes, como gráficos 2D e gráficos de barras.
#Scikit-learn, comumente conhecido como Sklearn, oferece uma interface amigável para todos os tipos de aprendizado de máquina.
Se você já se perguntou como gráficos de "previsão" são criados em Python, as chances são de que uma dessas 4 ferramentas tenha sido envolvida. Eles facilitam para iniciantes desbloquearem o poder do Python na ciência de dados.

#Dados coletados do Zillow.


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

#Ideias

1. Vendas de videogames baseadas em avaliações.
2. Engajamento nas redes sociais baseado no crescimento de seguidores.
3. Notas baseadas no tempo de estudo.

#Mais Recursos
#Para aprendizado e se aprofundar:

1. Código-fonte deste tutorial.
2. Conjuntos de Dados Kaggle: Explore conjuntos de dados diversos para diversos projetos de aprendizado de máquina.
3. Documentação Scikit-Learn: Mergulhe em informações detalhadas sobre aprendizado de máquina.
4. Documentação Pandas: Saiba mais sobre manipulação e análise de dados.
📈 Documentação Matplotlib: Explore a documentação Matplotlib para criar visualizações cativantes.
