import pygame

from config import (
    TELA,
    PRETO,
    BRANCO,
    CINZA,
    CINZA_CLARO,
    VERMELHO,
    VERDE,
    AMARELO,
    FONTE_TITULO,
    FONTE_GRANDE,
    FONTE_MEDIA,
    FONTE_PEQUENA,
    FONTE_NUMERO
)
from simbolos import desenhar_simbolo

# ============================================================
# FUNÇÕES AUXILIARES DE DESENHO
# ============================================================

def desenhar_texto(texto, fonte, cor, x, y, centralizado=False):
    superficie = fonte.render(texto, True, cor)

    if centralizado:
        retangulo = superficie.get_rect(center=(x, y))
    else:
        retangulo = superficie.get_rect(topleft=(x, y))

    TELA.blit(superficie, retangulo)

    return retangulo


def desenhar_botao(rect, texto, cor, cor_texto=BRANCO):
    pygame.draw.rect(
        TELA,
        cor,
        rect,
        border_radius=10
    )

    pygame.draw.rect(
        TELA,
        BRANCO,
        rect,
        2,
        border_radius=10
    )

    desenhar_texto(
        texto,
        FONTE_MEDIA,
        cor_texto,
        rect.centerx,
        rect.centery,
        True
    )

# ============================================================
# GEOMETRIA DOS ELEMENTOS CLICÁVEIS
# (usada tanto para desenhar quanto para detectar cliques)
# ============================================================

def retangulos_fios(quantidade):
    espacamento = 130
    largura_total = (quantidade - 1) * espacamento + 80
    inicio_x = 550 - largura_total // 2

    return [
        pygame.Rect(inicio_x + i * espacamento, 350, 80, 150)
        for i in range(quantidade)
    ]


def retangulos_simbolos():
    return [
        pygame.Rect(170 + i * 145, 320, 100, 120)
        for i in range(6)
    ]


def retangulos_painel():
    retangulos = []

    for i in range(6):
        coluna = i % 3
        linha = i // 3

        retangulos.append(
            pygame.Rect(
                280 + coluna * (150 + 30),
                310 + linha * (85 + 25),
                150,
                85
            )
        )

    return retangulos

# ============================================================
# BOMBA
# ============================================================

def desenhar_bomba(partida, tempo_restante, modulo_atual, erros, max_erros):

    pygame.draw.rect(
        TELA,
        (40, 40, 45),
        (100, 70, 900, 560),
        border_radius=20
    )

    pygame.draw.rect(
        TELA,
        CINZA_CLARO,
        (100, 70, 900, 560),
        3,
        border_radius=20
    )

    pygame.draw.rect(
        TELA,
        (20, 20, 23),
        (130, 100, 840, 80),
        border_radius=10
    )

    desenhar_texto(
        "DISPOSITIVO EXPLOSIVO",
        FONTE_TITULO,
        VERMELHO,
        550,
        140,
        True
    )

    minutos = int(tempo_restante) // 60
    segundos = int(tempo_restante) % 60
    tempo = f"{minutos:02d}:{segundos:02d}"

    pygame.draw.rect(
        TELA,
        PRETO,
        (780, 115, 150, 50),
        border_radius=5
    )

    desenhar_texto(
        tempo,
        FONTE_MEDIA,
        VERMELHO,
        855,
        140,
        True
    )

    desenhar_texto(
        f"MÓDULO {modulo_atual}/4",
        FONTE_MEDIA,
        BRANCO,
        140,
        200
    )

    desenhar_texto(
        f"ERROS: {erros}/{max_erros}",
        FONTE_MEDIA,
        VERMELHO if erros > 0 else BRANCO,
        750,
        200
    )

    # Informações gerais (sempre visíveis, usadas pelo manual)
    bomba = partida["bomba"]

    pygame.draw.rect(
        TELA,
        (20, 20, 23),
        (130, 588, 840, 34),
        border_radius=8
    )

    cor_indicador = AMARELO if bomba["indicador_aceso"] else CINZA_CLARO
    texto_indicador = "ACESO" if bomba["indicador_aceso"] else "APAGADO"

    pygame.draw.circle(TELA, cor_indicador, (735, 605), 8)

    desenhar_texto(
        f"SERIAL: {bomba['serial']}",
        FONTE_PEQUENA,
        BRANCO,
        330,
        605,
        True
    )

    desenhar_texto(
        f"BATERIAS: {bomba['baterias']}",
        FONTE_PEQUENA,
        BRANCO,
        550,
        605,
        True
    )

    desenhar_texto(
        f"INDICADOR: {texto_indicador}",
        FONTE_PEQUENA,
        cor_indicador,
        850,
        605,
        True
    )

# ============================================================
# MÓDULO 1
# ============================================================

def desenhar_modulo_fios(partida, tempo_restante, modulo_atual, erros, max_erros):
    desenhar_bomba(partida, tempo_restante, modulo_atual, erros, max_erros)

    desenhar_texto(
        "CORTE O FIO CORRETO",
        FONTE_GRANDE,
        BRANCO,
        550,
        250,
        True
    )

    for i, (fio, rect) in enumerate(
        zip(partida["fios"], retangulos_fios(len(partida["fios"])))
    ):
        pygame.draw.rect(
            TELA,
            fio[1],
            (rect.x + 30, 350, 20, 150),
            border_radius=8
        )

        desenhar_texto(
            str(i + 1),
            FONTE_MEDIA,
            BRANCO,
            rect.x + 40,
            530,
            True
        )

# ============================================================
# MÓDULO 2
# ============================================================

def desenhar_modulo_codigo(
    partida,
    tempo_restante,
    modulo_atual,
    erros,
    max_erros,
    codigo_digitado
):
    desenhar_bomba(partida, tempo_restante, modulo_atual, erros, max_erros)

    desenhar_texto(
        "DECODIFIQUE O CÓDIGO",
        FONTE_GRANDE,
        BRANCO,
        550,
        250,
        True
    )

    codigo = "".join(
        map(str, partida["codigo_criptografado"])
    )

    pygame.draw.rect(
        TELA,
        PRETO,
        (350, 300, 400, 100),
        border_radius=10
    )

    desenhar_texto(
        codigo,
        FONTE_NUMERO,
        VERDE,
        550,
        350,
        True
    )

    pygame.draw.rect(
        TELA,
        CINZA,
        (350, 430, 400, 70),
        border_radius=10
    )

    desenhar_texto(
        codigo_digitado,
        FONTE_NUMERO,
        BRANCO,
        550,
        465,
        True
    )

    desenhar_texto(
        "Digite os 4 números",
        FONTE_PEQUENA,
        CINZA_CLARO,
        550,
        530,
        True
    )

# ============================================================
# MÓDULO 3
# ============================================================

def desenhar_modulo_simbolos(
    partida,
    tempo_restante,
    modulo_atual,
    erros,
    max_erros,
    sequencia_digitada
):
    desenhar_bomba(partida, tempo_restante, modulo_atual, erros, max_erros)

    desenhar_texto(
        "SEQUÊNCIA DE SÍMBOLOS",
        FONTE_GRANDE,
        BRANCO,
        550,
        250,
        True
    )

    for i, (simbolo, rect) in enumerate(
        zip(partida["simbolos"], retangulos_simbolos())
    ):
        pygame.draw.rect(
            TELA,
            CINZA,
            rect,
            border_radius=12
        )

        pygame.draw.rect(
            TELA,
            BRANCO,
            rect,
            2,
            border_radius=12
        )

        desenhar_simbolo(
            simbolo,
            rect.centerx,
            rect.centery,
            30
        )

        desenhar_texto(
            str(i + 1),
            FONTE_PEQUENA,
            CINZA_CLARO,
            rect.centerx,
            rect.bottom + 20,
            True
        )

    x = 550
    y = 510

    for i, simbolo in enumerate(sequencia_digitada):
        desenhar_simbolo(
            simbolo,
            x - 120 + i * 80,
            y,
            22,
            VERDE
        )

    desenhar_texto(
        "Digite a sequência indicada pelo especialista",
        FONTE_PEQUENA,
        CINZA_CLARO,
        550,
        575,
        True
    )

# ============================================================
# MÓDULO 4
# ============================================================

def desenhar_modulo_painel(
    partida,
    tempo_restante,
    modulo_atual,
    erros,
    max_erros,
    sequencia_painel_digitada
):
    desenhar_bomba(partida, tempo_restante, modulo_atual, erros, max_erros)

    desenhar_texto(
        "PAINEL DE ENERGIA",
        FONTE_GRANDE,
        BRANCO,
        550,
        250,
        True
    )

    for i, (interruptor, rect) in enumerate(
        zip(partida["painel"], retangulos_painel())
    ):
        x = rect.x
        y = rect.y

        pygame.draw.rect(
            TELA,
            CINZA,
            rect,
            border_radius=10
        )

        pygame.draw.rect(
            TELA,
            interruptor["cor_rgb"],
            rect,
            4,
            border_radius=10
        )

        desenhar_texto(
            str(i + 1),
            FONTE_MEDIA,
            BRANCO,
            x + 25,
            y + 20,
            True
        )

        desenhar_texto(
            str(interruptor["numero"]),
            FONTE_NUMERO,
            interruptor["cor_rgb"],
            x + 75,
            y + 42,
            True
        )

        desenhar_texto(
            interruptor["cor"],
            FONTE_PEQUENA,
            BRANCO,
            x + 75,
            y + 68,
            True
        )

    texto = "SEQUÊNCIA: "

    for numero in sequencia_painel_digitada:
        texto += str(numero + 1) + " "

    desenhar_texto(
        texto,
        FONTE_MEDIA,
        VERDE,
        550,
        535,
        True
    )

    desenhar_texto(
        "Pressione os três interruptores na ordem correta.",
        FONTE_PEQUENA,
        CINZA_CLARO,
        550,
        575,
        True
    )

# ============================================================
# TELAS FINAIS
# ============================================================

def desenhar_menu(botao_iniciar):
    TELA.fill(PRETO)

    desenhar_texto(
        "OPERAÇÃO DESARME",
        FONTE_TITULO,
        VERMELHO,
        550,
        150,
        True
    )

    desenhar_texto(
        "Jogo cooperativo para dois jogadores",
        FONTE_MEDIA,
        BRANCO,
        550,
        220,
        True
    )

    desenhar_texto(
        "JOGADOR 1: Especialista",
        FONTE_MEDIA,
        (240, 200, 40),
        550,
        290,
        True
    )

    desenhar_texto(
        "JOGADOR 2: Técnico",
        FONTE_MEDIA,
        (40, 100, 220),
        550,
        330,
        True
    )

    desenhar_botao(
        botao_iniciar,
        "INICIAR",
        VERDE
    )

    desenhar_texto(
        "O manual é fixo: consulte o arquivo manual_bomba.txt.",
        FONTE_PEQUENA,
        CINZA_CLARO,
        550,
        610,
        True
    )


def desenhar_vitoria(botao_reiniciar):
    TELA.fill((10, 60, 25))

    desenhar_texto(
        "BOMBA DESARMADA!",
        FONTE_TITULO,
        VERDE,
        550,
        200,
        True
    )

    desenhar_texto(
        "Parabéns! Os dois jogadores trabalharam juntos.",
        FONTE_MEDIA,
        BRANCO,
        550,
        280,
        True
    )

    desenhar_botao(
        botao_reiniciar,
        "NOVA PARTIDA",
        (40, 100, 220)
    )


def desenhar_explosao(botao_reiniciar, erros):
    TELA.fill((100, 10, 10))

    desenhar_texto(
        "BOOOOOOM!",
        FONTE_TITULO,
        (240, 200, 40),
        550,
        220,
        True
    )

    desenhar_texto(
        "A bomba explodiu!",
        FONTE_GRANDE,
        BRANCO,
        550,
        300,
        True
    )

    desenhar_texto(
        f"Erros cometidos: {erros}",
        FONTE_MEDIA,
        BRANCO,
        550,
        360,
        True
    )

    desenhar_botao(
        botao_reiniciar,
        "TENTAR NOVAMENTE",
        VERDE
    )
