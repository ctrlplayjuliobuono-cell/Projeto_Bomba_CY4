import math
import pygame

from config import TELA, BRANCO

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
        pygame.draw.polygon(TELA, cor, pontos)

    elif simbolo == "circulo":
        pygame.draw.circle(TELA, cor, (x, y), tamanho)

    elif simbolo == "losango":
        pontos = [
            (x, y - tamanho),
            (x + tamanho, y),
            (x, y + tamanho),
            (x - tamanho, y)
        ]
        pygame.draw.polygon(TELA, cor, pontos)

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
            pontos.append((ponto_x, ponto_y))

        pygame.draw.polygon(TELA, cor, pontos)

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

            pygame.draw.line(TELA, cor, (x1, y1), (x2, y2), 4)

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
