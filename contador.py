# Linguagem de Programação II
# Atividade Contínua 02 - Dicionários
#
# e-mails: aluno1@aluno.faculdadeimpacta.com.br
#          aluno2@aluno.faculdadeimpacta.com.br
#          aluno3@aluno.faculdadeimpacta.com.br

from typing import List, Tuple, Dict


def le_arquivo(file_name: str) -> str:
    '''
    Função que recebe uma string com o nome do arquivo e
    retorna uma string com o texto da saída.
    Exemplo de chamada da função:
        texto = le_arquivo('exemplo.txt')
    '''
    f = open(file_name, 'r')
    texto = f.read()
    f.close()
    return texto.upper()


def eh_pontuacao(caract: str) -> bool:
    '''
    Função que recebe um caractere e retorna:
        True se ele for um símbolo de pontuação ou
        False caso contrário.
    Considere os seguintes símbolos:
    ['.', ',', ';', ':', '?', '!', '[',']','(',')','','']
    '''
    pass


def eh_versiculo(linha: str) -> bool:
    '''
    Função que recebe uma linha do texto e verifica se ela é a
    primeira linha de um versículo (comparar o primeiro caractere com '»')
    '''
    pass


def eh_texto(linha: str) -> bool:
    '''
    Função que recebe uma linha do texto e verifica se ela é uma
    linha do texto principal, prefixadas com um número inteiro
    Dica - verificar se o primeiro caractere é um dígito com x.isdigit()
    '''
    pass


def conta_linhas(texto: str) -> Tuple[int, ...]:
    '''
    Função que recebe uma string com um texto e retorna o número
    de linhas contidas na string em uma tupla, na seguinte ordem:
        (
            linhas totais,
            linhas em branco,
            linhas de texto (linhas numeradas apenas),
            linhas de título dos versículos (começam com '»')
            linhas não coontabilizadas acima
        )
    Dicas: Divida a string em uma lista de strings, separando-a
    no caractere de quebra de linha e use as funções que
    verificam o tipo de cada linha.
    '''
    pass


def conta_tudo(texto: str) -> Dict[str, int]:
    '''
    Função que recebe uma string e retorna um dicionário
    contendo a contagem de cada caractere encontrado nela.
    '''
    pass


def remove_pontuacao(texto: str) -> str:
    '''
    Função que recebe uma string e retorna uma cópia
    da string com a pontuação removida.
    Dica: Percorra a string e use a função que verifica se um
    caractere é um símbolo de pontuação ou não.
    '''
    pass


def conta_palavras(texto: str) -> Dict[str, int]:
    '''
    Função que recebe uma string e retorna um dicionário
    com a contagem de cada palavra encontrada no texto da string.
    Dica: Use a função de remover pontuação criada acima para
    obter uma string que tenha apenas palavras, em seguida separe
    a string em uma lista e então faça a contagem/inclusão no dicionário.
    '''
    pass


def encontra_max(dicio: dict) -> Tuple[str, int]:
    '''
    Função que recebe um dicionário, encontra a palavra
    de maior ocorrência e retorna uma tupla com a palavra
    encontrada e o número de ocorrências
    '''
    pass


def encontra_max_n(dicio: dict, n: int) -> List[Tuple[str, int]]:
    '''
    Função que recebe um dicionário, encontra as palavras mais frequentes
    até a N-ésima palavra, retornando uma lista de tuplas em pares
    ('palavra', num_ocorrencias), exemplo n = 4:
    [('banana', 7), ('pera', 5), ('maçã', 4), ('laranja', 2)]
    '''
    pass


def main():
    '''
    Função principal que executa o contador de palavras
    ###################################################
    ######## ESTA FUNÇÃO NÃO SERÁ AVALIADA ############
    ###################################################
    Seu uso é opicional, embora recomendado. O código
    abaixo é um exemplo de como chamar as funções criadas
    para contar as palavras dos arquivos de texto passados,
    e vocês podem modificá-lo se assim desejarem.
    '''
    # Ler o arquivo de texto:
    name_op = 1
    if name_op == 1:
        text = le_arquivo('Bíblia_Sagrada.txt')
    elif name_op == 2:
        text = le_arquivo('Bíblia_parcial.txt')
    elif name_op == 3:
        text = le_arquivo('arquivo1.txt')

    # Contar as linhas:
    linhas = conta_linhas(text)
    print(linhas)

    # Gerar o dicionário de caracteres:
    dic_caracteres = conta_tudo(text)

    # Gerar o dicionário de palavras:
    dic_palavras = conta_palavras(text)

    # Encontra a lista das 10 caracteres mais frequentes
    lista_caract = encontra_max_n(dic_caracteres, 10)
    print(lista_caract)

    # Encontra a lista das 10 palavras mais frequentes
    lista_palavras = encontra_max_n(dic_palavras, 10)
    print(lista_palavras)


# Impede que o código da função main seja executado na importação
if __name__ == '__main__':
    main()
