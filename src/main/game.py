import pygame
from player import Player
from components.heart import Heart


def game_loop():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 400))
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    power_ups = pygame.sprite.Group()
    heart = Heart(250, 250)
    power_ups.add(heart)
    heart = Heart(100, 100)
    power_ups.add(heart)
    while True:
        screen.fill((50, 50, 50))
        pygame.draw.rect(screen, (255,0,0), (10, 10, player.current_health / player.get_health_ratio(), 25))
        pygame.draw.rect(screen, (255,255,255), (10, 10, player.health_bar, 25), 4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
        player.handle_keys()
        player.draw(screen)
        for s in power_ups:
            s.draw(screen)
            if pygame.sprite.collide_rect(player, s):
                power_ups.remove(s)
                player.set_current_health(s.hp)
        pygame.display.update()
        clock.tick(60)


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
