import string

def limpar_texto(texto):
    translator = str.maketrans("","",string.punctuation)
    return texto.translate(translator).lower()

def tokeinzar(texto):
    texto_limpo = limpar_texto(texto)
    return texto_limpo.split()

"""."""

def frequencia_palavras(tokens):
    freq={}

    for palavra in tokens:
        freq[palavra] = freq.get(palavra,0)+1
    return freq

def top_n_palavras(tokens, n=5):
    freq = frequencia_palavras(tokens)
    palavras_ordenadas = sorted(freq.items())
    return palavras_ordenadas[:n]
