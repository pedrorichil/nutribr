
import pandas as pd
from typing import Optional, Union

VDR = {
    "Energia (kcal)": 2000,
    "Proteina (g)": 50,
    "Lipideos (g)": 70,
    "Carboidrato (g)": 300
}

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

    def percentual_vdr(self):
        return {
            "Energia (%)": round((self.energia_kcal / VDR["Energia (kcal)"]) * 100, 2),
            "Proteina (%)": round((self.proteina_g / VDR["Proteina (g)"]) * 100, 2),
            "Lipideos (%)": round((self.lipideos_g / VDR["Lipideos (g)"]) * 100, 2),
            "Carboidrato (%)": round((self.carboidrato_g / VDR["Carboidrato (g)"]) * 100, 2),
        }

class TabelaNutricional:
    def __init__(self, caminho: Optional[Union[str, 'Path']] = None):
        from pathlib import Path
        if caminho is None:
            caminho = Path(__file__).parent / "data" / "taco.csv"
        if isinstance(caminho, str):
            caminho = Path(caminho)

        if caminho.suffix == ".csv":
            self.df = pd.read_csv(caminho)
        elif caminho.suffix == ".json":
            self.df = pd.read_json(caminho)
        elif caminho.suffix in [".xls", ".xlsx"]:
            self.df = pd.read_excel(caminho)
        else:
            raise ValueError("Formato de arquivo não suportado")

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

    def listar_alimentos(self, categoria: Optional[str] = None) -> list:
        if categoria:
            return self.df[self.df['Categoria'].str.lower() == categoria.lower()]['Alimento'].tolist()
        return self.df['Alimento'].tolist()

    def filtrar(self, categoria: Optional[str] = None, max_calorias: Optional[float] = None,
                min_proteina: Optional[float] = None) -> pd.DataFrame:
        df = self.df.copy()
        if categoria:
            df = df[df['Categoria'].str.lower() == categoria.lower()]
        if max_calorias is not None:
            df = df[df['Energia (kcal)'] <= max_calorias]
        if min_proteina is not None:
            df = df[df['Proteina (g)'] >= min_proteina]
        return df
