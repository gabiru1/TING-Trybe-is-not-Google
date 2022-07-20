from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    list_of_paths = list()
    instance_len = instance.__len__()

    if instance_len:
        for index in range(instance_len):
            list_of_paths.append(instance.search(index)["nome_do_arquivo"])

    if path_file not in list_of_paths:
        news_content = txt_importer(path_file)

        data = dict()
        data["nome_do_arquivo"] = path_file
        data["qtd_linhas"] = len(news_content)
        data["linhas_do_arquivo"] = news_content

        instance.enqueue(data)

        print(data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    instance_len = instance.__len__()

    if not instance_len:
        print("Não há elementos", file=sys.stdout)

    if instance_len:
        instance_remove_queue = instance.dequeue()
        path_file = instance_remove_queue["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        data = instance.search(position)

        print(data, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
