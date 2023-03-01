import pygame
from player import Player


def game_loop():
    screen = pygame.display.set_mode((800, 400))
    screen.fill((50, 50, 50))
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    screen.blit(player.surf, (0, 0))
    while True:
        frame = 0
        screen.blit(player.get_image(0, 60, 70, 1), (player.pos_x, player.pos_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
            if pygame.key.get_pressed()[pygame.K_w]:
                print("w was pressed")
                player.pos_y -= 1
                frame = 1
            if pygame.key.get_pressed()[pygame.K_s]:
                print("s was pressed")
                player.pos_y += 1
                frame = 1
            if pygame.key.get_pressed()[pygame.K_a]:
                print("a was pressed")
                player.pos_x -= 1
                frame = 1
            if pygame.key.get_pressed()[pygame.K_d]:
                print("d was pressed")
                player.pos_x += 1
                frame = 1
            screen.blit(player.get_image(frame, 60, 70, 1), (player.pos_x, player.pos_y))
        pygame.display.update()


def is_game_initialized():
    print("initializing game")
    pygame.init()
    is_initialized = pygame.get_init()
    if not is_initialized:
        raise ValueError("game failed to start!")
    else:
        print("game initialization complete")
    return True


def main():
    if is_game_initialized():
        print("starting game")
        game_loop()


if __name__ == "__main__":
    main()