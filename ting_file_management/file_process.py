import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return

    text_reader = txt_importer(path_file)

    process_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text_reader),
        "linhas_do_arquivo": text_reader
    }

    instance.enqueue(process_file)
    print(process_file, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
