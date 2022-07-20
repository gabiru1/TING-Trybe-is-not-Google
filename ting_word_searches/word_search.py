def exists_word(word, instance):
    """Aqui irá sua implementação"""
    listings = list()
    stacks = instance.__len__()

    for position in range(stacks):
        events = list()
        file = instance.search(position)

        for index, value in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in value.lower():
                events.append({"linha": index + 1})

        if len(events):
            listings.append({"palavra": word, "arquivo": file["nome_do_arquivo"], "ocorrencias": events})

    return listings


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
