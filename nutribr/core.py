
import pandas as pd
from typing import Optional

class Alimento:
    def __init__(self, nome: str, categoria: str, energia_kcal: float, proteina_g: float, lipideos_g: float, carboidrato_g: float):
        self.nome = nome
        self.categoria = categoria
        self.energia_kcal = energia_kcal
        self.proteina_g = proteina_g
        self.lipideos_g = lipideos_g
        self.carboidrato_g = carboidrato_g

    def __repr__(self):
        return f"<Alimento {self.nome} ({self.energia_kcal} kcal)>"

class TabelaNutricional:
    def __init__(self, caminho_csv: Optional[str] = None):
        if caminho_csv is None:
            from pathlib import Path
            caminho_csv = Path(__file__).parent / "data" / "taco.csv"
        self.df = pd.read_csv(caminho_csv)

    def buscar_por_nome(self, nome: str) -> Optional[Alimento]:
        resultados = self.df[self.df['Alimento'].str.lower() == nome.lower()]
        if not resultados.empty:
            row = resultados.iloc[0]
            return Alimento(
                nome=row['Alimento'],
                categoria=row['Categoria'],
                energia_kcal=row['Energia (kcal)'],
                proteina_g=row['Proteina (g)'],
                lipideos_g=row['Lipideos (g)'],
                carboidrato_g=row['Carboidrato (g)']
            )
        return None

    def listar_alimentos(self) -> list:
        return self.df['Alimento'].tolist()
