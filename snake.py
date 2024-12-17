import pygame
import keyboard
from collections import deque
import random

pygame.init()

# config da tela
#x = base; y =altura
base, altura = 800, 600
tela = pygame.display.set_mode((base, altura))
pygame.display.set_caption("snake")

# cores 
branco = (255,255,255)
black = (0,0,0)
red = (250,0,0)

# fonte
fonte = pygame.font.Font(None, 35)  # None usa a fonte padrão, 48 é o tamanho

# texto
pontos = 0
speed = 2
# Configurações da Snake
raio_segmento = 8  # Raio de cada segmento da cobra
espaco_entre_segmentos = 4  # Espaço entre os segmentos
snake = deque([(200, 150)])  # Lista de segmentos (cabeça começa no centro)
direcao = (speed, 0)  # Movimento inicial para a direita
comprimento = 5  # Quantidade máxima de segmentos


fruta = 'o'
cord_y_fruta = 260
cord_x_fruta = 400

imagem_fruta = pygame.font.Font(None, 45).render(fruta, True, red)

# Loop principal
relogio = pygame.time.Clock()
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    score = fonte.render(str(pontos), True, red)

    #pontuação
    chave_fruta = cord_x_fruta, cord_y_fruta
    chave_snake = snake[0]
    distance_y = chave_fruta[0] - chave_snake[0]
    distance_x = chave_fruta[1] - chave_snake[1]
    if distance_y < 0: distance_y = chave_snake[0] - chave_fruta[0]
    if distance_x < 0: distance_x = chave_snake[1] - chave_fruta[1]

    
    if distance_y <= 20 and distance_x <= 20:
        pontos += 1
        speed += 0.5
        comprimento += 4
        cord_x_fruta = random.randint(50,750)
        cord_y_fruta = random.randint(50,550)
       
        pygame.display.flip()

    if keyboard.is_pressed('d') and direcao != (speed - speed*2, 0):
        direcao = (speed, 0)
    if keyboard.is_pressed('a') and direcao != (speed, 0):
        direcao = (speed - speed*2, 0)
    if keyboard.is_pressed('s') and direcao != (0, speed - speed*2):
        direcao = (0, speed)
    if keyboard.is_pressed('w') and direcao != (0, speed):
        direcao = (0, speed - speed*2)
        
            #morte
    elif snake[0][0] >= 800 or snake[0][0] <= 0:
        print(pontos)
        rodando = False
    elif snake[0][1] >= 600 or snake[0][1] <= 0:
        print(pontos)
        rodando = False
    
    nova_cabeca = (snake[0][0] + direcao[0], snake[0][1] + direcao[1])
    snake.appendleft(nova_cabeca)  # Adiciona a nova posição da cabeça

    # Mantém o comprimento da cobra
    while len(snake) > comprimento:
        snake.pop()

    tela.fill(black)
    for i, segmento in enumerate(snake):
        # O último segmento é mais claro para dar um efeito visual fluido
        intensidade = 255 - (i * comprimento) if i * comprimento < 255 else 0
        cor_segmento = (intensidade, 255, intensidade)
        pygame.draw.circle(tela, cor_segmento, segmento, raio_segmento)

    tela.blit(imagem_fruta,(cord_x_fruta, cord_y_fruta))

    
    tela.blit(score,(20,25))

    # Atualizando a tela
    
    pygame.display.flip()
    relogio.tick(60)  # Controle de FPS

pygame.quit()
