import pygame

pygame.init()

# ============================================================
# CONFIGURAÇÕES GERAIS
# ============================================================

LARGURA = 1100
ALTURA = 700
FPS = 60

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("OPERAÇÃO DESARME")

clock = pygame.time.Clock()

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

# ============================================================
# JOGO
# ============================================================

MAX_ERROS = 3
TEMPO_TOTAL = 300

botao_iniciar = pygame.Rect(400, 500, 300, 70)
botao_reiniciar = pygame.Rect(400, 540, 300, 70)
