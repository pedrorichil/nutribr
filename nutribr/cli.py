
import argparse
from .core import TabelaNutricional

def main():
    parser = argparse.ArgumentParser(description="Interface de linha de comando da biblioteca nutribr.")
    subparsers = parser.add_subparsers(dest="comando")

    buscar = subparsers.add_parser("buscar")
    buscar.add_argument("nome", type=str, help="Nome do alimento")

    listar = subparsers.add_parser("listar")
    listar.add_argument("--categoria", type=str, help="Filtrar por categoria")

    vdr = subparsers.add_parser("vdr")
    vdr.add_argument("nome", type=str, help="Nome do alimento para cálculo de VDR")

    args = parser.parse_args()
    tabela = TabelaNutricional()

    if args.comando == "buscar":
        alimento = tabela.buscar_por_nome(args.nome)
        print(alimento if alimento else "Alimento não encontrado.")

    elif args.comando == "listar":
        alimentos = tabela.listar_alimentos(args.categoria)
        print(alimentos)

    elif args.comando == "vdr":
        alimento = tabela.buscar_por_nome(args.nome)
        if alimento:
            print(f"VDR de {alimento.nome}:")
            print(alimento.percentual_vdr())
        else:
            print("Alimento não encontrado.")
