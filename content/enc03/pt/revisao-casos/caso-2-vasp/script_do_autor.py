import csv
import os

def calculate_adsorption_energy(csv_file):
    energies = {}
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            energies[row['sistema']] = float(row['energia_eV'])
    
    # E_ads = E(CO/slab) - E(slab) - E(CO gás)
    e_co_slab = energies.get('CO_slab')
    e_slab = energies.get('slab')
    e_co_gas = energies.get('CO_gas')
    
    if None in (e_co_slab, e_slab, e_co_gas):
        print("Erro: Valores necessários não encontrados no arquivo CSV.")
        return

    e_ads = e_co_slab - e_slab - e_co_gas
    
    print("-" * 40)
    print("Cálculo da Energia de Adsorção")
    print("-" * 40)
    print(f"E(CO/slab) : {e_co_slab:>10.3f} eV")
    print(f"E(slab)    : {e_slab:>10.3f} eV")
    print(f"E(CO gás)  : {e_co_gas:>10.3f} eV")
    print("-" * 40)
    print(f"E_ads      : {e_ads:>10.3f} eV")
    print("-" * 40)

if __name__ == "__main__":
    # O arquivo resumo.csv está no mesmo diretório que o script
    csv_path = os.path.join(os.path.dirname(__file__), 'resumo.csv')
    
    if os.path.exists(csv_path):
        calculate_adsorption_energy(csv_path)
    else:
        print(f"Arquivo não encontrado: {csv_path}")
