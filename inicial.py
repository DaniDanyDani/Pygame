import pygame

pygame.init() # aplicando o setup
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Pegando a posiçao inicial como o centro
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # pygame.QUIT é para ver se apertamos o X da janela para fecha-la
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # preenche a tela com a cor roxa
    screen.fill("purple")

    # Desenha um circulo na tela com a cor vermelha, na posiçao do player e com raio de 10 px
    pygame.draw.circle(screen, "red", player_pos, 10)

    # Verifica se uma tecla foi apertada
    def movimentacao():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            # Tecla w
            player_pos.y -= 300 * dt
            # Atualiza a posição em y
        if keys[pygame.K_s]:
            # Tecla s
            player_pos.y += 300 * dt
            # Atualiza a posição em y
        if keys[pygame.K_a]:
            # tecla a
            player_pos.x -= 300 * dt
            # Atualiza a posição em x
        if keys[pygame.K_d]:
            # tecla d
            player_pos.x += 300 * dt
            # Atualiza a posição em x
        return player_pos

    movimentacao()
    # flip() não entendi direito mas acredito que atualiza a página
    pygame.display.flip()

    # limita FPS a 60
    # dt é o tempo delta em segundos desde o último quadro, usado para taxa de quadros
    # física independente.
    dt = clock.tick(60) / 1000

pygame.quit()