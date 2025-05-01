# nutribr

📦 Biblioteca de dados nutricionais de alimentos brasileiros baseada na TACO (IBGE)

## Visão Geral

`nutribr` é uma biblioteca Python que fornece acesso estruturado aos dados nutricionais dos alimentos presentes na Tabela Brasileira de Composição de Alimentos (TACO), mantida pelo IBGE e outras instituições. Ideal para projetos de nutrição, saúde e alimentação.

## Instalação

```bash
pip install nutribr
```

## Uso Básico

```python
from nutribr import TabelaNutricional

tabela = TabelaNutricional()
arroz = tabela.buscar("arroz")

for item in arroz:
    print(item)
```

## Funcionalidades

- Busca por alimentos por nome
- Listagem de todos os alimentos disponíveis
- Acesso aos dados de energia, proteínas, lipídios e carboidratos

## Estrutura dos Dados

- `Alimento`: nome, categoria, energia (kcal), proteína (g), lipídios (g), carboidrato (g)

## Fonte dos Dados

Os dados são derivados da [Tabela Brasileira de Composição de Alimentos (TACO)](https://www.unicamp.br/nepa/taco/).

## Licença

MIT