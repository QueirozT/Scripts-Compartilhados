from unicodedata import normalize


# Forma convencional de remover acentos
def normaliza(*palavras):
    saida = []

    for palavra in palavras:
        normalizado = normalize('NFKD', palavra)
        normalizada = normalizado.encode('ASCII', 'ignore').decode('ASCII')
        saida.append(normalizada)

    return saida


# Forma pythonica de remover acentos usando funções aninhadas
def normaliza2(*palavras):

    def ajudante(palavra):
        normalizado = normalize('NFKD', palavra)
        return normalizado.encode('ASCII', 'ignore').decode('ASCII')

    return [ajudante(palavra) for palavra in palavras]



if __name__ == '__main__':
    print(normaliza('Érico', 'Sabiá', 'João'))
    # ['Erico', 'Sabia', 'Joao']


    print(normaliza2('Érico', 'Sabiá', 'João'))
    # ['Erico', 'Sabia', 'Joao']
