import csv

# Constante de conversão de Hartree para kcal/mol
HARTREE_TO_KCAL_MOL = 627.509

def calcular_energia_reacao(arquivo_csv):
    energias = {}
    
    # Lê os dados do arquivo CSV
    with open(arquivo_csv, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            molecula = row['molecula'].strip()
            energia = float(row['energia'])
            energias[molecula] = energia
            
    # Verifica se todas as moléculas necessárias estão presentes
    for mol in ['H2', 'F2', 'HF']:
        if mol not in energias:
            raise ValueError(f"Energia da molécula {mol} não encontrada no arquivo.")
            
    # Reação: H2 + F2 -> 2 HF
    # ΔE = 2 * E(HF) - [E(H2) + E(F2)]
    e_reagentes = energias['H2'] + energias['F2']
    e_produtos = 2 * energias['HF']
    
    delta_e_hartree = e_produtos - e_reagentes
    delta_e_kcal_mol = delta_e_hartree * HARTREE_TO_KCAL_MOL
    
    print("=== Cálculo de Energia de Reação ===")
    print("Reação: H2 + F2 -> 2 HF")
    print(f"E(H2): {energias['H2']:>12.6f} Hartree")
    print(f"E(F2): {energias['F2']:>12.6f} Hartree")
    print(f"E(HF): {energias['HF']:>12.6f} Hartree")
    print("-" * 36)
    print(f"ΔE (Hartree):  {delta_e_hartree:>12.6f}")
    print(f"ΔE (kcal/mol): {delta_e_kcal_mol:>12.6f}")

if __name__ == "__main__":
    calcular_energia_reacao('resumo.csv')
