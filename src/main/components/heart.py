import pygame


class Heart(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.main_image = self.__load_main_image()
        self.rect = self.main_image.get_rect()


    def __load_main_image(self):
        image = pygame.image.load("./src/main/assets/Heart.png").convert_alpha()
        image = pygame.transform.scale(image, (25, 25))
        return image


    def render(self, screen, x_pos, y_pos):
        self.rect.move_ip(x_pos, y_pos)
        screen.blit(self.main_image, (x_pos, y_pos))


    def consume(self):
        self.kill()
