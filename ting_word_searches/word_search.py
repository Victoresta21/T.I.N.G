def exists_word(word, instance):
    files_with_the_words = []
    word_ocorrencies = []

    for file in range(len(instance.data)):
        for index, line in enumerate(
            instance.search(file)["linhas_do_arquivo"]
        ):
            if word.lower() in line.lower():
                word_ocorrencies.append({"linha": index + 1})

        if len(word_ocorrencies) != 0:
            files_with_the_words.append({
                "palavra": word,
                "arquivo": instance.search(file)["nome_do_arquivo"],
                "ocorrencias": word_ocorrencies,
            })

    return files_with_the_words


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
