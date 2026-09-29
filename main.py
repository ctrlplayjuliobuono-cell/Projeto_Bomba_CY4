import pygame

from config import (
    FPS,
    TELA,
    PRETO,
    MAX_ERROS,
    TEMPO_TOTAL,
    clock,
    botao_iniciar,
    botao_reiniciar
)

from partida import gerar_partida
from manual import criar_manual

from desenho import (
    desenhar_menu,
    desenhar_modulo_fios,
    desenhar_modulo_codigo,
    desenhar_modulo_simbolos,
    desenhar_modulo_painel,
    retangulos_fios,
    retangulos_simbolos,
    retangulos_painel,
    desenhar_vitoria,
    desenhar_explosao
)

# ============================================================
# INICIALIZAÇÃO
# ============================================================

pygame.init()

# O manual é fixo: é gerado uma única vez, ao abrir o jogo.
criar_manual()

partida = gerar_partida()

estado = "menu"
modulo_atual = 1
erros = 0

tempo_restante = TEMPO_TOTAL
inicio_tempo = pygame.time.get_ticks()

codigo_digitado = ""
sequencia_digitada = []
sequencia_painel_digitada = []

# ============================================================
# FUNÇÕES DE CONTROLE
# ============================================================

def registrar_erro():
    global erros
    global estado

    erros += 1

    if erros >= MAX_ERROS:
        estado = "explodiu"


def proximo_modulo():
    global modulo_atual
    global estado
    global inicio_tempo

    modulo_atual += 1

    if modulo_atual > 4:
        estado = "venceu"
  


def nova_partida():
    global partida
    global modulo_atual
    global erros
    global tempo_restante
    global inicio_tempo
    global codigo_digitado
    global sequencia_digitada
    global sequencia_painel_digitada
    global estado

    partida = gerar_partida()

    modulo_atual = 1
    erros = 0

    tempo_restante = TEMPO_TOTAL
    inicio_tempo = pygame.time.get_ticks()

    codigo_digitado = ""
    sequencia_digitada = []
    sequencia_painel_digitada = []

    estado = "jogando"

# ============================================================
# LOOP PRINCIPAL
# ============================================================

rodando = True

while rodando:

    clock.tick(FPS)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        # ====================================================
        # MENU
        # ====================================================

        if estado == "menu":

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if botao_iniciar.collidepoint(evento.pos):
                    nova_partida()

        # ====================================================
        # JOGO
        # ====================================================

        elif estado == "jogando":

            # =================================================
            # MÓDULO 1 - FIOS
            # =================================================

            if modulo_atual == 1:

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    mouse_x, mouse_y = evento.pos

                    for i, rect in enumerate(
                        retangulos_fios(len(partida["fios"]))
                    ):

                        if rect.collidepoint(mouse_x, mouse_y):

                            if i == partida["fio_correto"]:
                                proximo_modulo()
                            else:
                                registrar_erro()

            # =================================================
            # MÓDULO 2 - CÓDIGO
            # =================================================

            elif modulo_atual == 2:

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_BACKSPACE:

                        codigo_digitado = codigo_digitado[:-1]

                    elif evento.unicode.isdigit():

                        if len(codigo_digitado) < 4:

                            codigo_digitado += evento.unicode

                            if len(codigo_digitado) == 4:

                                codigo_correto = "".join(
                                    map(
                                        str,
                                        partida["codigo_original"]
                                    )
                                )

                                if codigo_digitado == codigo_correto:
                                    proximo_modulo()
                                else:
                                    registrar_erro()
                                    codigo_digitado = ""

            # =================================================
            # MÓDULO 3 - SÍMBOLOS
            # =================================================

            elif modulo_atual == 3:

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    mouse_x, mouse_y = evento.pos

                    for simbolo, rect in zip(
                        partida["simbolos"],
                        retangulos_simbolos()
                    ):

                        if rect.collidepoint(mouse_x, mouse_y):

                            sequencia_digitada.append(simbolo)

                            indice = len(sequencia_digitada) - 1

                            if (
                                sequencia_digitada[indice]
                                != partida["sequencia_simbolos"][indice]
                            ):
                                registrar_erro()
                                sequencia_digitada = []

                            elif len(sequencia_digitada) == 4:
                                proximo_modulo()

            # =================================================
            # MÓDULO 4 - PAINEL
            # =================================================

            elif modulo_atual == 4:

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    mouse_x, mouse_y = evento.pos

                    for i, rect in enumerate(retangulos_painel()):

                        if rect.collidepoint(mouse_x, mouse_y):

                            if i in sequencia_painel_digitada:
                                break

                            sequencia_painel_digitada.append(i)

                            indice = len(sequencia_painel_digitada) - 1

                            if (
                                sequencia_painel_digitada[indice]
                                != partida["sequencia_painel"][indice]
                            ):
                                registrar_erro()
                                sequencia_painel_digitada = []

                            elif len(sequencia_painel_digitada) == 3:
                                proximo_modulo()

        # ====================================================
        # FIM DE JOGO
        # ====================================================

        elif estado in ["venceu", "explodiu"]:

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if botao_reiniciar.collidepoint(evento.pos):
                    nova_partida()

    # ========================================================
    # TEMPORIZADOR
    # ========================================================

    if estado == "jogando":

        tempo_decorrido = (
            pygame.time.get_ticks()
            - inicio_tempo
        ) / 1000

        tempo_restante = TEMPO_TOTAL - tempo_decorrido

        if tempo_restante <= 0:
            tempo_restante = 0
            estado = "explodiu"

    # ========================================================
    # DESENHO
    # ========================================================

    if estado == "menu":

        desenhar_menu(botao_iniciar)

    elif estado == "jogando":

        TELA.fill(PRETO)

        if modulo_atual == 1:

            desenhar_modulo_fios(
                partida,
                tempo_restante,
                modulo_atual,
                erros,
                MAX_ERROS
            )

        elif modulo_atual == 2:

            desenhar_modulo_codigo(
                partida,
                tempo_restante,
                modulo_atual,
                erros,
                MAX_ERROS,
                codigo_digitado
            )

        elif modulo_atual == 3:

            desenhar_modulo_simbolos(
                partida,
                tempo_restante,
                modulo_atual,
                erros,
                MAX_ERROS,
                sequencia_digitada
            )

        elif modulo_atual == 4:

            desenhar_modulo_painel(
                partida,
                tempo_restante,
                modulo_atual,
                erros,
                MAX_ERROS,
                sequencia_painel_digitada
            )

    elif estado == "venceu":

        desenhar_vitoria(botao_reiniciar)

    elif estado == "explodiu":

        desenhar_explosao(botao_reiniciar, erros)

    pygame.display.flip()

pygame.quit()
