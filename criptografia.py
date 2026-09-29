from regras import ultimo_digito

# ============================================================
# CRIPTOGRAFIAS
#
# O método usado em cada partida NÃO é mais sorteado: ele é
# decidido pelas regras de escolha em regras.py (REGRAS_METODO),
# a partir do serial, das baterias e do indicador da bomba.
# ============================================================

TABELA_METODO_3 = {
    0: 7,
    1: 4,
    2: 9,
    3: 1,
    4: 8,
    5: 0,
    6: 3,
    7: 6,
    8: 2,
    9: 5
}


def criptografia_1(codigo, bomba):
    # Avança X posições, onde X é o último dígito do serial.
    x = ultimo_digito(bomba["serial"])
    return [(numero + x) % 10 for numero in codigo]


def criptografia_2(codigo, bomba):
    return codigo[::-1]


def criptografia_3(codigo, bomba):
    return [TABELA_METODO_3[numero] for numero in codigo]


def criptografia_4(codigo, bomba):
    # Multiplica por 2, soma 1 e usa módulo 11.
    return [(numero * 2 + 1) % 11 for numero in codigo]


def criptografia_5(codigo, bomba):
    # Avança 3 posições e depois inverte a ordem.
    return [(numero + 3) % 10 for numero in codigo][::-1]


METODOS = {
    1: criptografia_1,
    2: criptografia_2,
    3: criptografia_3,
    4: criptografia_4,
    5: criptografia_5
}


def criptografar(codigo, metodo, bomba):
    return METODOS[metodo](codigo, bomba)


def tabela_metodo_4():
    """Devolve {número na bomba: número original} para o método 4."""
    return {
        (numero * 2 + 1) % 11: numero
        for numero in range(10)
    }
