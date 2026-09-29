import textwrap

from criptografia import TABELA_METODO_3, tabela_metodo_4
from regras import (
    REGRAS_FIOS,
    REGRAS_METODO,
    REGRAS_SEQUENCIA_SIMBOLOS,
    MODIFICADORES_SIMBOLOS,
    REGRAS_PAINEL
)
from simbolos import SIMBOLOS, NOMES_SIMBOLOS, VALORES_SIMBOLOS

LARGURA_TEXTO = 68
LINHA = "=" * 45

# ============================================================
# MANUAL FIXO
# O texto é sempre o mesmo, pois é gerado a partir das mesmas
# regras (regras.py) que o jogo usa para validar as jogadas.
# ============================================================

def _paragrafo(texto, recuo=""):
    return textwrap.fill(
        texto,
        width=LARGURA_TEXTO,
        initial_indent=recuo,
        subsequent_indent=recuo
    )


def _regras_numeradas(regras):
    linhas = []

    for numero, regra in enumerate(regras, start=1):
        texto = regra[0]
        linhas.append(
            textwrap.fill(
                f"{numero}) {texto}",
                width=LARGURA_TEXTO,
                subsequent_indent="   "
            )
        )
        linhas.append("")

    return "\n".join(linhas)


def _titulo(texto):
    return f"{LINHA}\n{texto}\n{LINHA}\n\n"


def gerar_texto_manual():
    t = []

    # ========================================================
    # CABEÇALHO
    # ========================================================

    t.append(f"{LINHA}\n        MANUAL DO ESPECIALISTA\n          OPERAÇÃO DESARME\n{LINHA}\n\n")

    t.append(
        _paragrafo(
            "IMPORTANTE: o ESPECIALISTA lê este manual. O TÉCNICO "
            "NÃO deve ler o manual: ele só enxerga a bomba, descreve "
            "o que vê e executa as ordens do especialista."
        )
        + "\n\n"
    )

    t.append(
        _paragrafo(
            "Este manual é o mesmo em todas as partidas. O que muda "
            "de uma partida para outra é a bomba: as informações "
            "gerais, os fios, o código, os símbolos e o painel."
        )
        + "\n\n"
    )

    # ========================================================
    # INFORMAÇÕES GERAIS
    # ========================================================

    t.append(_titulo("INFORMAÇÕES GERAIS DA BOMBA"))

    t.append(
        _paragrafo(
            "Na parte de baixo da bomba, em TODOS os módulos, ficam "
            "três informações. Muitas regras dependem delas, então "
            "peça ao técnico que as leia logo no início:"
        )
        + "\n\n"
    )

    t.append(
        "  - SERIAL: 6 caracteres (letras e números), ex.: KB47M3.\n"
        "  - BATERIAS: quantidade de baterias (de 0 a 4).\n"
        "  - INDICADOR: aceso ou apagado.\n\n"
    )

    t.append("DEFINIÇÕES USADAS NAS REGRAS:\n\n")

    t.append(
        _paragrafo(
            "- ÚLTIMO DÍGITO DO SERIAL: o último NÚMERO que aparece "
            "no serial. Em KB47M3 é o 3 (ímpar). Em QA52Z8 seria o 8.",
            ""
        )
        + "\n"
    )

    t.append(
        _paragrafo(
            "- VOGAL: as letras A, E, I, O, U. Diga que o serial "
            "\"contém vogal\" se QUALQUER uma delas aparecer.",
            ""
        )
        + "\n"
    )

    t.append(
        _paragrafo(
            "- PAR/ÍMPAR: o 0 conta como PAR.",
            ""
        )
        + "\n\n"
    )

    t.append(
        _paragrafo(
            "COMO LER AS REGRAS: leia sempre de cima para baixo e "
            "aplique a PRIMEIRA regra cuja condição for verdadeira. "
            "Ignore todas as regras seguintes (exceto onde o manual "
            "disser que TODAS as regras devem ser verificadas)."
        )
        + "\n\n"
    )

    # ========================================================
    # MÓDULO 1
    # ========================================================

    t.append(_titulo("MÓDULO 1 - FIOS"))

    t.append(
        _paragrafo(
            "Os fios são numerados de 1 a N, da ESQUERDA para a "
            "DIREITA. A bomba pode ter 4, 5 ou 6 fios, e as cores "
            "PODEM SE REPETIR. Pergunte ao técnico quantos fios "
            "existem e a cor de cada um, na ordem, e então use a "
            "seção correspondente."
        )
        + "\n\n"
    )

    for quantidade, regras in REGRAS_FIOS.items():
        t.append(f"--- BOMBA COM {quantidade} FIOS ---\n\n")
        t.append(_regras_numeradas(regras))
        t.append("\n")

    # ========================================================
    # MÓDULO 2
    # ========================================================

    t.append(_titulo("MÓDULO 2 - CRIPTOGRAFIA"))

    t.append(
        _paragrafo(
            "A bomba mostra um código de 4 números que está "
            "criptografado. O técnico deve digitar o código ORIGINAL. "
            "Este módulo tem dois passos."
        )
        + "\n\n"
    )

    t.append("PASSO 1 - DESCOBRIR QUAL MÉTODO FOI USADO\n\n")
    t.append(_regras_numeradas(REGRAS_METODO))

    t.append("PASSO 2 - DECODIFICAR USANDO O MÉTODO\n\n")

    t.append("MÉTODO 1 - DESLOCAMENTO PELO SERIAL\n\n")
    t.append(
        _paragrafo(
            "Cada número foi AVANÇADO X posições, onde X é o último "
            "dígito do serial. Para decodificar, VOLTE X posições em "
            "cada número. Depois do 9 vem o 0, e antes do 0 vem o 9."
        )
        + "\n\n"
    )
    t.append(
        "Exemplo com X = 3: o número 1 na bomba era o 8 (1 - 3 = -2, "
        "que volta a 8).\n"
        "Exemplo com X = 3: o número 5 na bomba era o 2.\n\n"
    )

    t.append("MÉTODO 2 - INVERSÃO\n\n")
    t.append(
        _paragrafo(
            "O código original foi escrito de trás para frente. "
            "Inverta a ordem dos números para descobrir o código. "
            "Exemplo: 4 8 1 6 na bomba era 6 1 8 4."
        )
        + "\n\n"
    )

    t.append("MÉTODO 3 - SUBSTITUIÇÃO\n\n")
    t.append("Use a tabela para trocar cada número da bomba pelo original:\n\n")

    inverso_3 = {cripto: original for original, cripto in TABELA_METODO_3.items()}
    ordem = list(range(10))

    t.append("  NÚMERO NA BOMBA:  " + " ".join(str(n) for n in ordem) + "\n")
    t.append("  NÚMERO ORIGINAL:  " + " ".join(str(inverso_3[n]) for n in ordem) + "\n\n")

    t.append("MÉTODO 4 - DOBRAR, SOMAR 1 E LIMITAR\n\n")
    t.append(
        _paragrafo(
            "O código foi feito assim: cada número original foi "
            "multiplicado por 2, somado a 1 e, se o resultado "
            "chegasse a 11 ou mais, subtraía-se 11. "
            "Para não precisar fazer a conta ao contrário, use a "
            "tabela:"
        )
        + "\n\n"
    )

    inverso_4 = tabela_metodo_4()

    t.append("  NÚMERO NA BOMBA:  " + " ".join(str(n) for n in ordem) + "\n")
    t.append("  NÚMERO ORIGINAL:  " + " ".join(str(inverso_4[n]) for n in ordem) + "\n\n")

    t.append("MÉTODO 5 - DESLOCAMENTO + INVERSÃO\n\n")
    t.append(
        _paragrafo(
            "Dois passos, nesta ordem: (a) INVERTA a ordem dos "
            "números da bomba; (b) em cada número, VOLTE 3 posições "
            "(antes do 0 vem o 9; ex.: 1 vira 8). "
            "Exemplo: 2 9 0 4 -> inverte: 4 0 9 2 -> volta 3: 1 7 6 9."
        )
        + "\n\n"
    )

    # ========================================================
    # MÓDULO 3
    # ========================================================

    t.append(_titulo("MÓDULO 3 - SÍMBOLOS"))

    t.append("Cada símbolo possui um valor fixo:\n\n")

    for simbolo in SIMBOLOS:
        nome = NOMES_SIMBOLOS[simbolo]
        t.append(f"  {nome:<14} = {VALORES_SIMBOLOS[simbolo]}\n")

    t.append("\n")

    t.append(
        _paragrafo(
            "Os seis símbolos aparecem na tela em uma ordem "
            "aleatória. Eles são numerados de 1 a 6, da ESQUERDA "
            "para a DIREITA (o técnico vê o número de cada posição "
            "abaixo do símbolo). O técnico deve clicar em 4 símbolos, "
            "na ordem correta."
        )
        + "\n\n"
    )

    t.append("PASSO 1 - ESCOLHA A SEQUÊNCIA BASE DE VALORES\n\n")

    for numero, (texto, _, valores) in enumerate(REGRAS_SEQUENCIA_SIMBOLOS, start=1):
        sequencia = " -> ".join(str(v) for v in valores)
        t.append(f"{numero}) {texto}\n   sequência: {sequencia}\n\n")

    t.append("PASSO 2 - APLIQUE OS MODIFICADORES\n\n")
    t.append(
        _paragrafo(
            "Agora verifique TODOS os modificadores abaixo, um por "
            "um, na ordem. Cada modificador cuja condição for "
            "verdadeira altera a sequência que você tem naquele "
            "momento. Pergunte ao técnico a posição do SOL, do "
            "TRIÂNGULO, do CÍRCULO e da ESTRELA."
        )
        + "\n\n"
    )
    t.append(_regras_numeradas(MODIFICADORES_SIMBOLOS))

    t.append("PASSO 3 - TRADUZA OS VALORES EM SÍMBOLOS\n\n")
    t.append(
        _paragrafo(
            "Use a tabela de valores para descobrir qual símbolo "
            "corresponde a cada valor da sequência final e diga ao "
            "técnico a ordem em que ele deve clicar."
        )
        + "\n\n"
    )

    # ========================================================
    # MÓDULO 4
    # ========================================================

    t.append(_titulo("MÓDULO 4 - PAINEL DE ENERGIA"))

    t.append(
        _paragrafo(
            "O painel tem 6 interruptores, cada um com um NÚMERO "
            "(de 1 a 9, sem repetição) e uma COR (as 6 cores "
            "aparecem uma vez cada). Eles são numerados de 1 a 6, "
            "da esquerda para a direita, de cima para baixo. O "
            "técnico deve pressionar 3 interruptores, um por passo."
        )
        + "\n\n"
    )

    t.append(
        _paragrafo(
            "ATENÇÃO: em cada passo, considere apenas os "
            "interruptores que AINDA NÃO foram pressionados. Um "
            "interruptor nunca é escolhido duas vezes."
        )
        + "\n\n"
    )

    for passo, regras in enumerate(REGRAS_PAINEL, start=1):
        t.append(f"--- {passo}º INTERRUPTOR ---\n\n")
        t.append(_regras_numeradas(regras))

    t.append(f"{LINHA}\nFIM DO MANUAL\n{LINHA}\n")

    return "".join(t)


def criar_manual(caminho="manual_bomba.txt"):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(gerar_texto_manual())
