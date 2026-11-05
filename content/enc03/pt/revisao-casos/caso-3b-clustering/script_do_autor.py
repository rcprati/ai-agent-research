import pandas as pd
from sklearn.cluster import KMeans
from collections import Counter

def main():
    # Carregar os dados
    df = pd.read_csv('dados_clustering.csv')
    
    # Criar o modelo K-means com 3 clusters
    kmeans = KMeans(n_clusters=3, random_state=42)
    
    # Treinar e predizer os clusters
    labels = kmeans.fit_predict(df)
    
    # Contar o tamanho de cada cluster
    tamanhos = Counter(labels)
    
    # Exibir os resultados
    print("Tamanho de cada cluster:")
    # Ordenar por id do cluster para facilitar a leitura
    for cluster_id in sorted(tamanhos.keys()):
        print(f"Cluster {cluster_id}: {tamanhos[cluster_id]} elementos")

if __name__ == '__main__':
    main()
