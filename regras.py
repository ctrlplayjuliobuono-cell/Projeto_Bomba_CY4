# ============================================================
# REGRAS DO JOGO (FONTE ÚNICA DA VERDADE)
#
# Tudo o que aparece no manual é gerado a partir das listas
# abaixo, e as mesmas listas decidem qual é a resposta certa
# de cada módulo. Assim o manual e o jogo nunca divergem.
#
# Cada regra é uma tupla: (texto_do_manual, condição, resultado)
# As regras são lidas de cima para baixo: vale a PRIMEIRA
# cuja condição for verdadeira.
# ============================================================

VOGAIS = "AEIOU"

# ============================================================
# FUNÇÕES AUXILIARES SOBRE A BOMBA
#
# bomba = {
#     "serial": "KB47M3",
#     "baterias": 2,
#     "indicador_aceso": True
# }
# ============================================================

def ultimo_digito(serial):
    for caractere in reversed(serial):
        if caractere.isdigit():
            return int(caractere)
    return 0


def tem_vogal(serial):
    return any(c in VOGAIS for c in serial)


def indices_da_cor(fios, cor):
    return [i for i, nome in enumerate(fios) if nome == cor]


# ============================================================
# MÓDULO 1 - FIOS
# Condição e ação recebem (bomba, fios), onde fios é a lista
# de nomes das cores, da esquerda para a direita.
# A ação devolve o índice (começando em 0) do fio a cortar.
# ============================================================

REGRAS_FIOS = {
    4: [
        (
            "Se houver MAIS DE UM fio VERMELHO e o último dígito do "
            "serial for ÍMPAR: corte o ÚLTIMO fio VERMELHO.",
            lambda b, f: f.count("VERMELHO") > 1
            and ultimo_digito(b["serial"]) % 2 == 1,
            lambda b, f: indices_da_cor(f, "VERMELHO")[-1]
        ),
        (
            "Senão, se o ÚLTIMO fio for AMARELO e NÃO houver nenhum "
            "fio VERMELHO: corte o PRIMEIRO fio.",
            lambda b, f: f[-1] == "AMARELO" and f.count("VERMELHO") == 0,
            lambda b, f: 0
        ),
        (
            "Senão, se houver EXATAMENTE UM fio AZUL: corte o fio "
            "imediatamente DEPOIS dele (se o AZUL for o último, "
            "corte o PRIMEIRO fio).",
            lambda b, f: f.count("AZUL") == 1,
            lambda b, f: (indices_da_cor(f, "AZUL")[0] + 1) % len(f)
        ),
        (
            "Senão, se houver MAIS DE UM fio AMARELO: corte o "
            "ÚLTIMO fio.",
            lambda b, f: f.count("AMARELO") > 1,
            lambda b, f: len(f) - 1
        ),
        (
            "Senão: corte o SEGUNDO fio.",
            lambda b, f: True,
            lambda b, f: 1
        ),
    ],
    5: [
        (
            "Se o ÚLTIMO fio for ROXO e a bomba tiver 0 BATERIAS: "
            "corte o QUARTO fio.",
            lambda b, f: f[-1] == "ROXO" and b["baterias"] == 0,
            lambda b, f: 3
        ),
        (
            "Senão, se houver EXATAMENTE UM fio VERMELHO e MAIS DE "
            "UM fio AMARELO: corte o PRIMEIRO fio.",
            lambda b, f: f.count("VERMELHO") == 1 and f.count("AMARELO") > 1,
            lambda b, f: 0
        ),
        (
            "Senão, se NÃO houver nenhum fio LARANJA: corte o "
            "SEGUNDO fio.",
            lambda b, f: f.count("LARANJA") == 0,
            lambda b, f: 1
        ),
        (
            "Senão, se o INDICADOR estiver ACESO: corte o PRIMEIRO "
            "fio LARANJA.",
            lambda b, f: b["indicador_aceso"],
            lambda b, f: indices_da_cor(f, "LARANJA")[0]
        ),
        (
            "Senão: corte o ÚLTIMO fio.",
            lambda b, f: True,
            lambda b, f: len(f) - 1
        ),
    ],
    6: [
        (
            "Se NÃO houver nenhum fio AMARELO e o último dígito do "
            "serial for ÍMPAR: corte o TERCEIRO fio.",
            lambda b, f: f.count("AMARELO") == 0
            and ultimo_digito(b["serial"]) % 2 == 1,
            lambda b, f: 2
        ),
        (
            "Senão, se houver EXATAMENTE UM fio AMARELO e MAIS DE UM "
            "fio VERDE: corte o QUARTO fio.",
            lambda b, f: f.count("AMARELO") == 1 and f.count("VERDE") > 1,
            lambda b, f: 3
        ),
        (
            "Senão, se NÃO houver nenhum fio VERMELHO: corte o "
            "ÚLTIMO fio.",
            lambda b, f: f.count("VERMELHO") == 0,
            lambda b, f: len(f) - 1
        ),
        (
            "Senão, se a bomba tiver 2 ou mais BATERIAS e o serial "
            "contiver alguma VOGAL: corte o PRIMEIRO fio VERMELHO.",
            lambda b, f: b["baterias"] >= 2 and tem_vogal(b["serial"]),
            lambda b, f: indices_da_cor(f, "VERMELHO")[0]
        ),
        (
            "Senão: corte o fio cuja posição seja igual ao número de "
            "BATERIAS somado a 1 (0 baterias = 1º fio, 1 bateria = "
            "2º fio, e assim por diante).",
            lambda b, f: True,
            lambda b, f: b["baterias"]
        ),
    ],
}


def resolver_fios(bomba, fios):
    for _, condicao, acao in REGRAS_FIOS[len(fios)]:
        if condicao(bomba, fios):
            return acao(bomba, fios)


# ============================================================
# MÓDULO 2 - CRIPTOGRAFIA
# Escolha do método a partir do estado da bomba.
# ============================================================

REGRAS_METODO = [
    (
        "Se o INDICADOR estiver ACESO e a bomba tiver 3 ou mais "
        "BATERIAS: use o MÉTODO 5.",
        lambda b: b["indicador_aceso"] and b["baterias"] >= 3,
        5
    ),
    (
        "Senão, se o serial contiver alguma VOGAL e o INDICADOR "
        "estiver APAGADO: use o MÉTODO 3.",
        lambda b: tem_vogal(b["serial"]) and not b["indicador_aceso"],
        3
    ),
    (
        "Senão, se a bomba tiver 0 BATERIAS: use o MÉTODO 2.",
        lambda b: b["baterias"] == 0,
        2
    ),
    (
        "Senão, se o último dígito do serial for PAR: use o MÉTODO 4.",
        lambda b: ultimo_digito(b["serial"]) % 2 == 0,
        4
    ),
    (
        "Senão: use o MÉTODO 1.",
        lambda b: True,
        1
    ),
]


def escolher_metodo(bomba):
    for _, condicao, metodo in REGRAS_METODO:
        if condicao(bomba):
            return metodo


# ============================================================
# MÓDULO 3 - SÍMBOLOS
# Passo 1: escolher a sequência base de VALORES.
# Passo 2: aplicar TODOS os modificadores cuja condição for
#          verdadeira, na ordem em que aparecem.
# Os símbolos são identificados pelo nome interno
# ("sol", "triangulo", "circulo", "estrela", ...) e a lista
# "simbolos" está na ordem em que aparecem na tela.
# ============================================================

REGRAS_SEQUENCIA_SIMBOLOS = [
    (
        "Se a bomba tiver 3 ou mais BATERIAS:",
        lambda b: b["baterias"] >= 3,
        [4, 1, 6, 2]
    ),
    (
        "Senão, se o INDICADOR estiver ACESO:",
        lambda b: b["indicador_aceso"],
        [5, 3, 1, 6]
    ),
    (
        "Senão, se o serial contiver alguma VOGAL:",
        lambda b: tem_vogal(b["serial"]),
        [2, 5, 1, 4]
    ),
    (
        "Senão:",
        lambda b: True,
        [6, 3, 4, 1]
    ),
]


def _posicao(simbolos, nome):
    return simbolos.index(nome) + 1


MODIFICADORES_SIMBOLOS = [
    (
        "Se o SOL estiver em uma posição ÍMPAR (1, 3 ou 5): INVERTA "
        "a ordem da sequência.",
        lambda b, s: _posicao(s, "sol") % 2 == 1,
        lambda seq: seq[::-1]
    ),
    (
        "Se o TRIÂNGULO estiver ao lado do CÍRCULO (posições "
        "vizinhas): TROQUE DE LUGAR o primeiro e o último valor "
        "da sequência.",
        lambda b, s: abs(_posicao(s, "triangulo") - _posicao(s, "circulo")) == 1,
        lambda seq: [seq[-1]] + seq[1:-1] + [seq[0]]
    ),
    (
        "Se a ESTRELA estiver na primeira ou na última posição "
        "(1 ou 6): TROQUE DE LUGAR o segundo e o terceiro valor "
        "da sequência.",
        lambda b, s: _posicao(s, "estrela") in (1, 6),
        lambda seq: [seq[0], seq[2], seq[1], seq[3]]
    ),
]


def resolver_sequencia_simbolos(bomba, simbolos):
    """Devolve a lista de 4 VALORES na ordem correta."""
    for _, condicao, valores in REGRAS_SEQUENCIA_SIMBOLOS:
        if condicao(bomba):
            sequencia = list(valores)
            break

    for _, condicao, aplicar in MODIFICADORES_SIMBOLOS:
        if condicao(bomba, simbolos):
            sequencia = aplicar(sequencia)

    return sequencia


# ============================================================
# MÓDULO 4 - PAINEL DE ENERGIA
# São 3 passos. Em cada passo, só contam os interruptores que
# AINDA NÃO foram pressionados ("restantes").
# Condição e escolha recebem (bomba, painel, restantes).
# ============================================================

def _maior(painel, restantes):
    return max(restantes, key=lambda i: painel[i]["numero"])


def _menor(painel, restantes):
    return min(restantes, key=lambda i: painel[i]["numero"])


def _da_cor(painel, restantes, cor):
    for i in restantes:
        if painel[i]["cor"] == cor:
            return i
    return None


def _com_numero(painel, restantes, numero):
    for i in restantes:
        if painel[i]["numero"] == numero:
            return i
    return None


REGRAS_PAINEL = [
    # ---------------- 1º interruptor ----------------
    [
        (
            "Se o INDICADOR estiver ACESO: o interruptor de MAIOR número.",
            lambda b, p, r: b["indicador_aceso"],
            lambda b, p, r: _maior(p, r)
        ),
        (
            "Senão, se o número de BATERIAS for PAR (0 conta como par): "
            "o interruptor de MENOR número.",
            lambda b, p, r: b["baterias"] % 2 == 0,
            lambda b, p, r: _menor(p, r)
        ),
        (
            "Senão: o interruptor VERMELHO.",
            lambda b, p, r: True,
            lambda b, p, r: _da_cor(p, r, "VERMELHO")
        ),
    ],
    # ---------------- 2º interruptor ----------------
    [
        (
            "Se existir um interruptor cujo número seja IGUAL ao último "
            "dígito do serial: esse interruptor.",
            lambda b, p, r: _com_numero(p, r, ultimo_digito(b["serial"])) is not None,
            lambda b, p, r: _com_numero(p, r, ultimo_digito(b["serial"]))
        ),
        (
            "Senão, se a bomba tiver 2 ou mais BATERIAS e o interruptor "
            "AMARELO ainda não foi pressionado: o interruptor AMARELO.",
            lambda b, p, r: b["baterias"] >= 2 and _da_cor(p, r, "AMARELO") is not None,
            lambda b, p, r: _da_cor(p, r, "AMARELO")
        ),
        (
            "Senão: o interruptor de MENOR número.",
            lambda b, p, r: True,
            lambda b, p, r: _menor(p, r)
        ),
    ],
    # ---------------- 3º interruptor ----------------
    [
        (
            "Se a SOMA dos números dos 6 interruptores for MAIOR que 30 "
            "e o interruptor VERDE ainda não foi pressionado: o "
            "interruptor VERDE.",
            lambda b, p, r: sum(i["numero"] for i in p) > 30
            and _da_cor(p, r, "VERDE") is not None,
            lambda b, p, r: _da_cor(p, r, "VERDE")
        ),
        (
            "Senão, se o interruptor AZUL ainda não foi pressionado: "
            "o interruptor AZUL.",
            lambda b, p, r: _da_cor(p, r, "AZUL") is not None,
            lambda b, p, r: _da_cor(p, r, "AZUL")
        ),
        (
            "Senão: o interruptor de MAIOR número.",
            lambda b, p, r: True,
            lambda b, p, r: _maior(p, r)
        ),
    ],
]


def resolver_painel(bomba, painel):
    """Devolve os índices (a partir de 0) dos 3 interruptores, em ordem."""
    restantes = list(range(len(painel)))
    sequencia = []

    for regras_do_passo in REGRAS_PAINEL:
        for _, condicao, escolha in regras_do_passo:
            if condicao(bomba, painel, restantes):
                escolhido = escolha(bomba, painel, restantes)
                break

        sequencia.append(escolhido)
        restantes.remove(escolhido)

    return sequencia
