import random

from config import (
    VERMELHO,
    AZUL,
    VERDE,
    AMARELO,
    ROXO,
    LARANJA
)
from criptografia import criptografar
from regras import (
    escolher_metodo,
    resolver_fios,
    resolver_sequencia_simbolos,
    resolver_painel
)
from simbolos import SIMBOLOS, VALORES_SIMBOLOS

# ============================================================
# CORES
# ============================================================

CORES = [
    ("VERMELHO", VERMELHO),
    ("AZUL", AZUL),
    ("VERDE", VERDE),
    ("AMARELO", AMARELO),
    ("ROXO", ROXO),
    ("LARANJA", LARANJA)
]

LETRAS_SERIAL = "ABCDEFGHJKLMNPQRSTUVWXYZ"

# ============================================================
# INFORMAÇÕES GERAIS DA BOMBA
# Ficam sempre visíveis na parte de baixo da bomba e são
# usadas pelas condicionais do manual.
# ============================================================

def gerar_bomba():
    serial = (
        random.choice(LETRAS_SERIAL)
        + random.choice(LETRAS_SERIAL)
        + str(random.randint(0, 9))
        + str(random.randint(0, 9))
        + random.choice(LETRAS_SERIAL)
        + str(random.randint(0, 9))
    )

    return {
        "serial": serial,
        "baterias": random.randint(0, 4),
        "indicador_aceso": random.choice([True, False])
    }

# ============================================================
# GERAÇÃO DA PARTIDA
# O manual é fixo: o que muda a cada partida é apenas o estado
# da bomba. As respostas certas vêm de regras.py.
# ============================================================

def gerar_partida():

    bomba = gerar_bomba()

    # ========================================================
    # MÓDULO 1 - FIOS (4, 5 ou 6 fios; as cores podem repetir)
    # ========================================================

    quantidade_fios = random.choice([4, 5, 6])
    fios = random.choices(CORES, k=quantidade_fios)

    nomes_fios = [fio[0] for fio in fios]
    fio_correto = resolver_fios(bomba, nomes_fios)

    # ========================================================
    # MÓDULO 2 - CÓDIGO
    # ========================================================

    codigo_original = [
        random.randint(0, 9)
        for _ in range(4)
    ]

    metodo_cripto = escolher_metodo(bomba)

    codigo_criptografado = criptografar(
        codigo_original,
        metodo_cripto,
        bomba
    )

    # ========================================================
    # MÓDULO 3 - SÍMBOLOS
    # ========================================================

    simbolos_disponiveis = random.sample(SIMBOLOS, 6)

    valores_sequencia = resolver_sequencia_simbolos(
        bomba,
        simbolos_disponiveis
    )

    sequencia_simbolos = []

    for valor in valores_sequencia:
        for simbolo in simbolos_disponiveis:
            if VALORES_SIMBOLOS[simbolo] == valor:
                sequencia_simbolos.append(simbolo)
                break

    # ========================================================
    # MÓDULO 4 - PAINEL DE ENERGIA
    # (as 6 cores aparecem uma vez cada)
    # ========================================================

    numeros = random.sample(range(1, 10), 6)
    cores_sorteadas = random.sample(CORES, 6)

    painel = []

    for i in range(6):
        painel.append({
            "numero": numeros[i],
            "cor": cores_sorteadas[i][0],
            "cor_rgb": cores_sorteadas[i][1]
        })

    sequencia_painel = resolver_painel(bomba, painel)

    return {
        "bomba": bomba,

        "fios": fios,
        "fio_correto": fio_correto,

        "codigo_original": codigo_original,
        "codigo_criptografado": codigo_criptografado,
        "metodo_cripto": metodo_cripto,

        "simbolos": simbolos_disponiveis,
        "sequencia_simbolos": sequencia_simbolos,

        "painel": painel,
        "sequencia_painel": sequencia_painel
    }
