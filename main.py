import pygame
import random
import math

pygame.init()

LARGURA = 1100
ALTURA = 700

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("OPERAÇÃO DESARME")

FPS = 60

# ============================================================
# CORES
# ============================================================

PRETO = (15, 15, 18)
BRANCO = (240, 240, 240)
CINZA = (70, 70, 75)
CINZA_CLARO = (130, 130, 135)

VERMELHO = (220, 40, 40)
VERDE = (40, 200, 90)
AZUL = (40, 100, 220)
AMARELO = (240, 200, 40)
ROXO = (150, 60, 200)
LARANJA = (240, 120, 30)
CIANO = (30, 200, 210)

# ============================================================
# FONTES
# ============================================================

FONTE_TITULO = pygame.font.SysFont("arial", 42, bold=True)
FONTE_GRANDE = pygame.font.SysFont("arial", 34, bold=True)
FONTE_MEDIA = pygame.font.SysFont("arial", 26)
FONTE_PEQUENA = pygame.font.SysFont("arial", 20)
FONTE_NUMERO = pygame.font.SysFont("arial", 48, bold=True)

clock = pygame.time.Clock()


# ============================================================
# FUNÇÕES AUXILIARES
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
# CRIPTOGRAFIAS
# ============================================================

def criptografia_1(codigo):

    return [
        (numero + 3) % 10
        for numero in codigo
    ]


def criptografia_2(codigo):

    return codigo[::-1]


def criptografia_3(codigo):

    tabela = {
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

    return [
        tabela[numero]
        for numero in codigo
    ]


def criptografia_4(codigo):

    # Multiplica por 2, soma 1 e usa módulo 11.
    # Assim, cada dígito de 0 a 9 gera um resultado único
    # que continua dentro do intervalo de 0 a 9.
    return [
        (numero * 2 + 1) % 11
        for numero in codigo
    ]


def gerar_criptografia(codigo):

    metodo = random.randint(1, 4)

    if metodo == 1:
        return criptografia_1(codigo), metodo

    if metodo == 2:
        return criptografia_2(codigo), metodo

    if metodo == 3:
        return criptografia_3(codigo), metodo

    return criptografia_4(codigo), metodo


# ============================================================
# SÍMBOLOS
# ============================================================

SIMBOLOS = [
    "triangulo",
    "circulo",
    "losango",
    "estrela",
    "sol",
    "guarda_chuva"
]

NOMES_SIMBOLOS = {
    "triangulo": "TRIÂNGULO",
    "circulo": "CÍRCULO",
    "losango": "LOSANGO",
    "estrela": "ESTRELA",
    "sol": "SOL",
    "guarda_chuva": "GUARDA-CHUVA"
}

# Valor fixo de cada símbolo.
# Esses valores são usados para criar a lógica
# do Módulo 3.
VALORES_SIMBOLOS = {
    "triangulo": 1,
    "circulo": 2,
    "losango": 3,
    "estrela": 4,
    "sol": 5,
    "guarda_chuva": 6
}


# ============================================================
# DESENHO DOS SÍMBOLOS
# ============================================================

def desenhar_simbolo(simbolo, x, y, tamanho, cor=BRANCO):

    if simbolo == "triangulo":

        pontos = [
            (x, y - tamanho),
            (x - tamanho, y + tamanho),
            (x + tamanho, y + tamanho)
        ]

        pygame.draw.polygon(
            TELA,
            cor,
            pontos
        )

    elif simbolo == "circulo":

        pygame.draw.circle(
            TELA,
            cor,
            (x, y),
            tamanho
        )

    elif simbolo == "losango":

        pontos = [
            (x, y - tamanho),
            (x + tamanho, y),
            (x, y + tamanho),
            (x - tamanho, y)
        ]

        pygame.draw.polygon(
            TELA,
            cor,
            pontos
        )

    elif simbolo == "estrela":

        pontos = []

        for i in range(10):

            angulo = -math.pi / 2 + i * math.pi / 5

            if i % 2 == 0:
                raio = tamanho
            else:
                raio = tamanho * 0.45

            ponto_x = x + math.cos(angulo) * raio
            ponto_y = y + math.sin(angulo) * raio

            pontos.append(
                (ponto_x, ponto_y)
            )

        pygame.draw.polygon(
            TELA,
            cor,
            pontos
        )

    elif simbolo == "sol":

        pygame.draw.circle(
            TELA,
            cor,
            (x, y),
            int(tamanho * 0.55)
        )

        for i in range(8):

            angulo = i * math.pi / 4

            x1 = x + math.cos(angulo) * tamanho * 0.8
            y1 = y + math.sin(angulo) * tamanho * 0.8

            x2 = x + math.cos(angulo) * tamanho * 1.2
            y2 = y + math.sin(angulo) * tamanho * 1.2

            pygame.draw.line(
                TELA,
                cor,
                (x1, y1),
                (x2, y2),
                4
            )

    elif simbolo == "guarda_chuva":

        pygame.draw.arc(
            TELA,
            cor,
            (
                x - tamanho,
                y - tamanho * 0.6,
                tamanho * 2,
                tamanho * 1.2
            ),
            math.pi,
            2 * math.pi,
            5
        )

        pygame.draw.line(
            TELA,
            cor,
            (x, y),
            (x, y + tamanho),
            5
        )

        pygame.draw.arc(
            TELA,
            cor,
            (
                x - tamanho * 0.25,
                y + tamanho * 0.7,
                tamanho * 0.5,
                tamanho * 0.5
            ),
            0,
            math.pi,
            5
        )


# ============================================================
# GERAÇÃO DA PARTIDA
# ============================================================

def gerar_partida():

    # ========================================================
    # MÓDULO 1 - FIOS
    # ========================================================

    cores_fios = [
        ("VERMELHO", VERMELHO),
        ("AZUL", AZUL),
        ("VERDE", VERDE),
        ("AMARELO", AMARELO),
        ("ROXO", ROXO),
        ("LARANJA", LARANJA)
    ]

    fios = random.sample(
        cores_fios,
        6
    )

    posicao_vermelho = None

    for i, fio in enumerate(fios):

        if fio[0] == "VERMELHO":

            posicao_vermelho = i
            break

    posicao_humana = posicao_vermelho + 1

    if posicao_humana % 2 == 1:

        if posicao_vermelho == 5:
            fio_correto = 0
        else:
            fio_correto = posicao_vermelho + 1

        regra_fios = (
            "Localize o primeiro fio VERMELHO.\n"
            "Se ele estiver em posição ÍMPAR, "
            "corte o fio imediatamente DEPOIS.\n"
            "Se o vermelho estiver na última posição, "
            "corte o PRIMEIRO fio."
        )

    else:

        if posicao_vermelho == 0:
            fio_correto = 5
        else:
            fio_correto = posicao_vermelho - 1

        regra_fios = (
            "Localize o primeiro fio VERMELHO.\n"
            "Se ele estiver em posição PAR, "
            "corte o fio imediatamente ANTES.\n"
            "Se o vermelho estiver na primeira posição, "
            "corte o ÚLTIMO fio."
        )

    # ========================================================
    # MÓDULO 2 - CÓDIGO
    # ========================================================

    codigo_original = [
        random.randint(0, 9)
        for _ in range(4)
    ]

    codigo_criptografado, metodo_cripto = gerar_criptografia(
        codigo_original
    )

    # ========================================================
    # MÓDULO 3 - SÍMBOLOS
    # ========================================================

    simbolos_disponiveis = random.sample(
        SIMBOLOS,
        6
    )

    # --------------------------------------------------------
    # NOVA REGRA DO MÓDULO 3
    # --------------------------------------------------------
    #
    # Os símbolos possuem valores fixos:
    #
    # TRIÂNGULO      = 1
    # CÍRCULO        = 2
    # LOSANGO        = 3
    # ESTRELA        = 4
    # SOL            = 5
    # GUARDA-CHUVA   = 6
    #
    # A sequência correta será formada pelos símbolos
    # que possuem os valores:
    #
    # 2 → 5 → 1 → 4
    #
    # Como os seis símbolos estão presentes, a sequência
    # sempre poderá ser encontrada.
    #
    # --------------------------------------------------------

    valores_sequencia = [2, 5, 1, 4]

    sequencia_simbolos = []

    for valor in valores_sequencia:

        for simbolo in simbolos_disponiveis:

            if VALORES_SIMBOLOS[simbolo] == valor:

                sequencia_simbolos.append(
                    simbolo
                )

                break

    # ========================================================
    # MÓDULO 4 - PAINEL DE ENERGIA
    # ========================================================

    cores_painel = [
        ("VERMELHO", VERMELHO),
        ("AZUL", AZUL),
        ("VERDE", VERDE),
        ("AMARELO", AMARELO),
        ("ROXO", ROXO),
        ("LARANJA", LARANJA)
    ]

    painel = []

    numeros = random.sample(
        range(1, 10),
        6
    )

    cores_sorteadas = random.sample(
        cores_painel,
        6
    )

    for i in range(6):

        painel.append({
            "numero": numeros[i],
            "cor": cores_sorteadas[i][0],
            "cor_rgb": cores_sorteadas[i][1]
        })

    indice_maior = max(
        range(6),
        key=lambda i: painel[i]["numero"]
    )

    indice_menor = min(
        range(6),
        key=lambda i: painel[i]["numero"]
    )

    indice_azul = next(
        i
        for i in range(6)
        if painel[i]["cor"] == "AZUL"
    )

    sequencia_painel = [
        indice_maior,
        indice_menor,
        indice_azul
    ]

    return {

        # Módulo 1
        "fios": fios,
        "fio_correto": fio_correto,
        "regra_fios": regra_fios,

        # Módulo 2
        "codigo_original": codigo_original,
        "codigo_criptografado": codigo_criptografado,
        "metodo_cripto": metodo_cripto,

        # Módulo 3
        "simbolos": simbolos_disponiveis,
        "sequencia_simbolos": sequencia_simbolos,

        # Módulo 4
        "painel": painel,
        "sequencia_painel": sequencia_painel
    }


# ============================================================
# CRIAÇÃO DO MANUAL
# ============================================================

def criar_manual(partida):

    with open(
        "manual_bomba.txt",
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            "=============================================\n"
        )

        arquivo.write(
            "        MANUAL DO ESPECIALISTA\n"
        )

        arquivo.write(
            "          OPERAÇÃO DESARME\n"
        )

        arquivo.write(
            "=============================================\n\n"
        )

        arquivo.write(
            "IMPORTANTE:\n"
            "O especialista deve ler este manual.\n"
            "O técnico NÃO deve ter acesso ao manual.\n\n"
        )

        # ====================================================
        # MÓDULO 1
        # ====================================================

        arquivo.write(
            "=============================================\n"
        )

        arquivo.write(
            "MÓDULO 1 - FIOS\n"
        )

        arquivo.write(
            "=============================================\n\n"
        )

        arquivo.write(
            partida["regra_fios"]
        )

        arquivo.write("\n\n")

        arquivo.write(
            "Sequência atual dos fios:\n\n"
        )

        for i, fio in enumerate(partida["fios"]):

            arquivo.write(
                f"{i + 1} - {fio[0]}\n"
            )

        arquivo.write("\n")

        arquivo.write(
            "Utilize a regra acima para descobrir "
            "qual fio deve ser cortado.\n\n"
        )

        # ====================================================
        # MÓDULO 2
        # ====================================================

        arquivo.write(
            "=============================================\n"
        )

        arquivo.write(
            "MÓDULO 2 - CRIPTOGRAFIA\n"
        )

        arquivo.write(
            "=============================================\n\n"
        )

        arquivo.write(
            "Código apresentado na bomba:\n\n"
        )

        arquivo.write(
            "".join(
                map(
                    str,
                    partida["codigo_criptografado"]
                )
            )
        )

        arquivo.write("\n\n")

        if partida["metodo_cripto"] == 1:

            arquivo.write(
                "MÉTODO 1 - DESLOCAMENTO\n\n"
            )

            arquivo.write(
                "Cada número foi avançado 3 posições.\n"
                "Para descobrir o número original, "
                "volte 3 posições.\n\n"
            )

        elif partida["metodo_cripto"] == 2:

            arquivo.write(
                "MÉTODO 2 - INVERSÃO\n\n"
            )

            arquivo.write(
                "O código original foi completamente "
                "invertido.\n"
                "Inverta novamente para descobrir o código.\n\n"
            )

        elif partida["metodo_cripto"] == 3:

            arquivo.write(
                "MÉTODO 3 - SUBSTITUIÇÃO\n\n"
            )

            arquivo.write(
                "Utilize a tabela abaixo para descobrir "
                "os números originais.\n\n"
            )

            arquivo.write(
                "NÚMERO CRIPTOGRAFADO:\n"
                "7 4 9 1 8 0 3 6 2 5\n\n"
            )

            arquivo.write(
                "NÚMERO ORIGINAL:\n"
                "0 1 2 3 4 5 6 7 8 9\n\n"
            )

            arquivo.write(
                "Exemplo: se o número criptografado for 7, "
                "o número original era 0.\n\n"
            )

        elif partida["metodo_cripto"] == 4:

            arquivo.write(
                "MÉTODO 4 - DOBRAR E LIMITAR A 0–9\n\n"
            )

            arquivo.write(
                "Para descobrir cada número original:\n\n"
            )

            arquivo.write(
                "1. Pegue um número original.\n"
                "2. Multiplique esse número por 2.\n"
                "3. Some 1 ao resultado.\n"
                "4. Se o resultado chegar a 11, volte para 0.\n\n"
            )

            arquivo.write(
                "Exemplos:\n\n"
            )

            arquivo.write(
                "3 → 3 × 2 + 1 = 7\n"
            )

            arquivo.write(
                "5 → 5 × 2 + 1 = 11 → 0\n\n"
            )

            arquivo.write(
                "Portanto:\n"
                "3 vira 7.\n"
                "5 vira 0.\n\n"
            )

            arquivo.write(
                "Para decodificar, teste os números de 0 a 9 "
                "até encontrar qual deles produz cada número "
                "apresentado na bomba. Cada número criptografado "
                "possui uma única correspondência.\n\n"
            )

        arquivo.write(
            "Utilize o método indicado para descobrir "
            "o código que deverá ser digitado.\n\n"
        )

        # ====================================================
        # MÓDULO 3
        # ====================================================

        arquivo.write(
            "=============================================\n"
        )

        arquivo.write(
            "MÓDULO 3 - SÍMBOLOS\n"
        )

        arquivo.write(
            "=============================================\n\n"
        )

        arquivo.write(
            "Cada símbolo possui um valor:\n\n"
        )

        arquivo.write(
            "TRIÂNGULO      = 1\n"
        )

        arquivo.write(
            "CÍRCULO        = 2\n"
        )

        arquivo.write(
            "LOSANGO        = 3\n"
        )

        arquivo.write(
            "ESTRELA        = 4\n"
        )

        arquivo.write(
            "SOL            = 5\n"
        )

        arquivo.write(
            "GUARDA-CHUVA   = 6\n\n"
        )

        arquivo.write(
            "Os seis símbolos estão presentes na bomba.\n\n"
        )

        arquivo.write(
            "REGRA DA SEQUÊNCIA:\n\n"
        )

        arquivo.write(
            "A sequência correta é formada pelos símbolos "
            "que possuem os seguintes valores, nesta ordem:\n\n"
        )

        arquivo.write(
            "2 → 5 → 1 → 4\n\n"
        )

        arquivo.write(
            "Descubra qual símbolo corresponde a cada valor "
            "e informe a sequência ao técnico.\n\n"
        )

        # ====================================================
        # MÓDULO 4
        # ====================================================

        arquivo.write(
            "=============================================\n"
        )

        arquivo.write(
            "MÓDULO 4 - PAINEL DE ENERGIA\n"
        )

        arquivo.write(
            "=============================================\n\n"
        )

        arquivo.write(
            "O painel possui 6 interruptores.\n"
        )

        arquivo.write(
            "Cada interruptor possui uma cor e um número.\n\n"
        )

        arquivo.write(
            "REGRAS:\n\n"
        )

        arquivo.write(
            "1 - O PRIMEIRO interruptor deve ser aquele "
            "que possui o MAIOR número.\n\n"
        )

        arquivo.write(
            "2 - O SEGUNDO interruptor deve ser aquele "
            "que possui o MENOR número.\n\n"
        )

        arquivo.write(
            "3 - O TERCEIRO interruptor deve ser o "
            "interruptor AZUL.\n\n"
        )

        arquivo.write(
            "Pressione os três interruptores nessa ordem.\n\n"
        )

        arquivo.write(
            "=============================================\n"
        )

        arquivo.write(
            "FIM DO MANUAL\n"
        )

        arquivo.write(
            "=============================================\n"
        )


# ============================================================
# ESTADO DO JOGO
# ============================================================

partida = gerar_partida()

criar_manual(partida)

estado = "menu"

modulo_atual = 1

erros = 0

MAX_ERROS = 3

tempo_total = 300

tempo_restante = tempo_total

inicio_tempo = pygame.time.get_ticks()

codigo_digitado = ""

sequencia_digitada = []

sequencia_painel_digitada = []


# ============================================================
# BOTÕES
# ============================================================

botao_iniciar = pygame.Rect(
    400,
    500,
    300,
    70
)

botao_reiniciar = pygame.Rect(
    400,
    540,
    300,
    70
)


# ============================================================
# DESENHAR BOMBA
# ============================================================

def desenhar_bomba():

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
        f"ERROS: {erros}/{MAX_ERROS}",
        FONTE_MEDIA,
        VERMELHO if erros > 0 else BRANCO,
        750,
        200
    )


# ============================================================
# MÓDULO 1 - FIOS
# ============================================================

def desenhar_modulo_fios():

    desenhar_bomba()

    desenhar_texto(
        "CORTE O FIO CORRETO",
        FONTE_GRANDE,
        BRANCO,
        550,
        250,
        True
    )

    inicio_x = 180
    espacamento = 130

    for i, fio in enumerate(partida["fios"]):

        x = inicio_x + i * espacamento

        pygame.draw.rect(
            TELA,
            fio[1],
            (
                x + 30,
                350,
                20,
                150
            ),
            border_radius=8
        )

        desenhar_texto(
            str(i + 1),
            FONTE_MEDIA,
            BRANCO,
            x + 40,
            530,
            True
        )


# ============================================================
# MÓDULO 2 - CÓDIGO
# ============================================================

def desenhar_modulo_codigo():

    desenhar_bomba()

    desenhar_texto(
        "DECODIFIQUE O CÓDIGO",
        FONTE_GRANDE,
        BRANCO,
        550,
        250,
        True
    )

    codigo = "".join(
        map(
            str,
            partida["codigo_criptografado"]
        )
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
# MÓDULO 3 - SÍMBOLOS
# ============================================================

def desenhar_modulo_simbolos():

    desenhar_bomba()

    desenhar_texto(
        "SEQUÊNCIA DE SÍMBOLOS",
        FONTE_GRANDE,
        BRANCO,
        550,
        250,
        True
    )

    inicio_x = 170
    espacamento = 145

    for i, simbolo in enumerate(
        partida["simbolos"]
    ):

        x = inicio_x + i * espacamento

        rect = pygame.Rect(
            x,
            320,
            100,
            120
        )

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

    for i, simbolo in enumerate(
        sequencia_digitada
    ):

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
# MÓDULO 4 - PAINEL DE ENERGIA
# ============================================================

def desenhar_modulo_painel():

    desenhar_bomba()

    desenhar_texto(
        "PAINEL DE ENERGIA",
        FONTE_GRANDE,
        BRANCO,
        550,
        250,
        True
    )

    inicio_x = 280
    inicio_y = 310

    largura = 150
    altura = 85

    espaco_x = 30
    espaco_y = 25

    for i, interruptor in enumerate(
        partida["painel"]
    ):

        coluna = i % 3
        linha = i // 3

        x = (
            inicio_x
            + coluna * (largura + espaco_x)
        )

        y = (
            inicio_y
            + linha * (altura + espaco_y)
        )

        rect = pygame.Rect(
            x,
            y,
            largura,
            altura
        )

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
# REGISTRAR ERRO
# ============================================================

def registrar_erro():

    global erros
    global estado

    erros += 1

    if erros >= MAX_ERROS:

        estado = "explodiu"


# ============================================================
# PRÓXIMO MÓDULO
# ============================================================

def proximo_modulo():

    global modulo_atual
    global estado
    global inicio_tempo

    modulo_atual += 1

    if modulo_atual > 4:

        estado = "venceu"

    else:

        inicio_tempo = pygame.time.get_ticks()


# ============================================================
# MENU
# ============================================================

def desenhar_menu():

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
        AMARELO,
        550,
        290,
        True
    )

    desenhar_texto(
        "JOGADOR 2: Técnico",
        FONTE_MEDIA,
        AZUL,
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
        "O manual será criado automaticamente.",
        FONTE_PEQUENA,
        CINZA_CLARO,
        550,
        610,
        True
    )


# ============================================================
# VITÓRIA
# ============================================================

def desenhar_vitoria():

    TELA.fill(
        (10, 60, 25)
    )

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
        AZUL
    )


# ============================================================
# EXPLOSÃO
# ============================================================

def desenhar_explosao():

    TELA.fill(
        (100, 10, 10)
    )

    desenhar_texto(
        "BOOOOOOM!",
        FONTE_TITULO,
        AMARELO,
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


# ============================================================
# NOVA PARTIDA
# ============================================================

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

    criar_manual(partida)

    modulo_atual = 1

    erros = 0

    tempo_restante = tempo_total

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

                if botao_iniciar.collidepoint(
                    evento.pos
                ):

                    nova_partida()

        # ====================================================
        # JOGO
        # ====================================================

        elif estado == "jogando":

            # =================================================
            # MÓDULO 1
            # =================================================

            if modulo_atual == 1:

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    mouse_x, mouse_y = evento.pos

                    inicio_x = 180
                    espacamento = 130

                    for i in range(6):

                        x = (
                            inicio_x
                            + i * espacamento
                        )

                        rect = pygame.Rect(
                            x,
                            350,
                            80,
                            150
                        )

                        if rect.collidepoint(
                            mouse_x,
                            mouse_y
                        ):

                            if (
                                i
                                == partida["fio_correto"]
                            ):

                                proximo_modulo()

                            else:

                                registrar_erro()

            # =================================================
            # MÓDULO 2
            # =================================================

            elif modulo_atual == 2:

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_BACKSPACE:

                        codigo_digitado = (
                            codigo_digitado[:-1]
                        )

                    elif evento.unicode.isdigit():

                        if len(codigo_digitado) < 4:

                            codigo_digitado += (
                                evento.unicode
                            )

                            if len(
                                codigo_digitado
                            ) == 4:

                                codigo_correto = "".join(
                                    map(
                                        str,
                                        partida[
                                            "codigo_original"
                                        ]
                                    )
                                )

                                if (
                                    codigo_digitado
                                    == codigo_correto
                                ):

                                    proximo_modulo()

                                else:

                                    registrar_erro()

                                    codigo_digitado = ""

            # =================================================
            # MÓDULO 3
            # =================================================

            elif modulo_atual == 3:

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    mouse_x, mouse_y = evento.pos

                    inicio_x = 170
                    espacamento = 145

                    for i, simbolo in enumerate(
                        partida["simbolos"]
                    ):

                        x = (
                            inicio_x
                            + i * espacamento
                        )

                        rect = pygame.Rect(
                            x,
                            320,
                            100,
                            120
                        )

                        if rect.collidepoint(
                            mouse_x,
                            mouse_y
                        ):

                            sequencia_digitada.append(
                                simbolo
                            )

                            indice = (
                                len(
                                    sequencia_digitada
                                ) - 1
                            )

                            if (
                                sequencia_digitada[indice]
                                != partida[
                                    "sequencia_simbolos"
                                ][indice]
                            ):

                                registrar_erro()

                                sequencia_digitada = []

                            elif len(
                                sequencia_digitada
                            ) == 4:

                                proximo_modulo()

            # =================================================
            # MÓDULO 4
            # =================================================

            elif modulo_atual == 4:

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    mouse_x, mouse_y = evento.pos

                    inicio_x = 280
                    inicio_y = 310

                    largura = 150
                    altura = 85

                    espaco_x = 30
                    espaco_y = 25

                    for i in range(6):

                        coluna = i % 3
                        linha = i // 3

                        x = (
                            inicio_x
                            + coluna
                            * (
                                largura
                                + espaco_x
                            )
                        )

                        y = (
                            inicio_y
                            + linha
                            * (
                                altura
                                + espaco_y
                            )
                        )

                        rect = pygame.Rect(
                            x,
                            y,
                            largura,
                            altura
                        )

                        if rect.collidepoint(
                            mouse_x,
                            mouse_y
                        ):

                            if i in sequencia_painel_digitada:

                                break

                            sequencia_painel_digitada.append(i)

                            indice = (
                                len(
                                    sequencia_painel_digitada
                                ) - 1
                            )

                            if (
                                sequencia_painel_digitada[
                                    indice
                                ]
                                != partida[
                                    "sequencia_painel"
                                ][indice]
                            ):

                                registrar_erro()

                                sequencia_painel_digitada = []

                            elif len(
                                sequencia_painel_digitada
                            ) == 3:

                                proximo_modulo()

        # ====================================================
        # FIM DE JOGO
        # ====================================================

        elif estado in [
            "venceu",
            "explodiu"
        ]:

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if botao_reiniciar.collidepoint(
                    evento.pos
                ):

                    nova_partida()

    # ========================================================
    # TEMPORIZADOR
    # ========================================================

    if estado == "jogando":

        tempo_decorrido = (
            pygame.time.get_ticks()
            - inicio_tempo
        ) / 1000

        tempo_restante = (
            tempo_total
            - tempo_decorrido
        )

        if tempo_restante <= 0:

            tempo_restante = 0

            estado = "explodiu"

    # ========================================================
    # DESENHO
    # ========================================================

    if estado == "menu":

        desenhar_menu()

    elif estado == "jogando":

        TELA.fill(PRETO)

        if modulo_atual == 1:

            desenhar_modulo_fios()

        elif modulo_atual == 2:

            desenhar_modulo_codigo()

        elif modulo_atual == 3:

            desenhar_modulo_simbolos()

        elif modulo_atual == 4:

            desenhar_modulo_painel()

    elif estado == "venceu":

        desenhar_vitoria()

    elif estado == "explodiu":

        desenhar_explosao()

    pygame.display.flip()


pygame.quit()