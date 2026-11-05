import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def main():
    # Carregar os dados
    df = pd.read_csv('dados_regressao.csv')
    
    # Separar features (X) e target (y)
    # Vamos usar todas as variáveis disponíveis como preditores para a energia
    X = df.drop(columns=['energia'])
    y = df['energia']
    
    # Dividir em conjuntos de treino e teste (80% treino, 20% teste)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Criar e treinar o modelo de regressão linear
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    
    # Fazer as predições no conjunto de teste
    y_pred = modelo.predict(X_test)
    
    # Calcular e exibir o R²
    r2 = r2_score(y_test, y_pred)
    print(f"R² nos dados de teste: {r2:.4f}")

if __name__ == '__main__':
    main()
