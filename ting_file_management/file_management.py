import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""

    try:
        if '.txt' not in path_file:
            print("Formato inválido", file=sys.stderr)

        file = open(path_file, 'r')
        content = [line.replace("\n", "") for line in file.readlines()]

        return content
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
