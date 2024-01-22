import pygame

pygame.init()  # aplicando o setup
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Pegando a posição inicial como o centro
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Lista para armazenar posições e duração dos disparos
tiros = []

while running:
    # pygame.QUIT é para ver se apertamos o X da janela para fecha-la
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # preenche a tela com a cor preta
    screen.fill("black")

    # Desenha um círculo na tela com a cor branca, na posição do player e com raio de 20 px
    pygame.draw.circle(screen, "white", (int(player_pos.x), int(player_pos.y)), 20)

    # Verifica se uma tecla foi apertada
    def movimentacao():
        keys = pygame.key.get_pressed()
        velocidade = 300

        if keys[pygame.K_w]:
            player_pos.y -= velocidade * dt
        if keys[pygame.K_s]:
            player_pos.y += velocidade * dt
        if keys[pygame.K_a]:
            player_pos.x -= velocidade * dt
        if keys[pygame.K_d]:
            player_pos.x += velocidade * dt

    # Atualiza a posição do jogador
    movimentacao()

    # Desenha as bolas de disparo
    def disparo():
        keys = pygame.key.get_pressed()
        velocidade_tiro = 500

        if keys[pygame.K_UP]:
            tiros.append({"pos": pygame.Vector2(player_pos.x, player_pos.y), "vel": pygame.Vector2(0, -velocidade_tiro), "duration": 0})
        if keys[pygame.K_DOWN]:
            tiros.append({"pos": pygame.Vector2(player_pos.x, player_pos.y), "vel": pygame.Vector2(0, velocidade_tiro), "duration": 0})
        if keys[pygame.K_LEFT]:
            tiros.append({"pos": pygame.Vector2(player_pos.x, player_pos.y), "vel": pygame.Vector2(-velocidade_tiro, 0), "duration": 0})
        if keys[pygame.K_RIGHT]:
            tiros.append({"pos": pygame.Vector2(player_pos.x, player_pos.y), "vel": pygame.Vector2(velocidade_tiro, 0), "duration": 0})

        # Combinações diagonais
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            tiros.append({"pos": pygame.Vector2(player_pos.x, player_pos.y), "vel": pygame.Vector2(-velocidade_tiro, -velocidade_tiro), "duration": 0})
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            tiros.append({"pos": pygame.Vector2(player_pos.x, player_pos.y), "vel": pygame.Vector2(velocidade_tiro, -velocidade_tiro), "duration": 0})
        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            tiros.append({"pos": pygame.Vector2(player_pos.x, player_pos.y), "vel": pygame.Vector2(-velocidade_tiro, velocidade_tiro), "duration": 0})
        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            tiros.append({"pos": pygame.Vector2(player_pos.x, player_pos.y), "vel": pygame.Vector2(velocidade_tiro, velocidade_tiro), "duration": 0})

    # Atualiza os disparos
    disparo()

    # Desenha e atualiza a duração dos disparos
    for tiro in tiros:
        pygame.draw.circle(screen, "red", (int(tiro["pos"].x), int(tiro["pos"].y)), 5)
        tiro["pos"] += tiro["vel"] * dt
        tiro["duration"] += dt

    # Remove os disparos que atingiram a borda da tela ou duraram mais de 2 segundos
    tiros = [tiro for tiro in tiros if 0 < tiro["pos"].x < screen.get_width() and 0 < tiro["pos"].y < screen.get_height() and tiro["duration"] < 2]

    # flip() não entendi direito mas acredito que atualiza a página
    pygame.display.flip()

    # limita FPS a 60
    # dt é o tempo delta em segundos desde o último quadro, usado para taxa de quadros
    # física independente.
    dt = clock.tick(60) / 1000

pygame.quit()
