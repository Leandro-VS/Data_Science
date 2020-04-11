def plot_decision_regions(X, y, classifier, resolution=0.02):
    #Setup do gerador de marcadores e cores (color map)
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    
    #plot da superficie de decisão
    #definindo o min e max das duas features
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    
    #Usando o min e max das features para criar um par de vetores de grid para a função meshgrid
    #np.meshgrid cria uma grade retangular apartir de duas matrizes para uma representação cartesiana
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    
    """
    _Como treinamos nosso perceptron com dados de duas diemensões, precisamos "achatar" os vetores grid,
    para criar uma matrix que tenha o mesmo numero de colunas que o sub-dataset de treino,
    então usamos o metodo predict para prever as lebels Z correpondentes aos pontos do grid.
    
    _.ravel() retorna um vetor "achatado"(1D)
    _.T acessa o atributo 'T' do objeto, que Transpõe o vetor (vetor transposto)
    _.shape() retorna uma tupla com as dimensões do vetor
    
    """
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    
    #Após redimensionar Z dentro do grid para as mesmas dimensões de xx1 e xx2, podemos então
    #plotar o seu contorno, onde diferentes regiões de decisão terão cores diferentes
    plt.figure(figsize=(14,9))
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    #Plot das classes das amostras
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], 
                    y=X[y == cl, 1],
                    alpha=0.8, 
                    c=colors[idx],
                    marker=markers[idx], 
                    label=cl, 
                    edgecolor='black')
