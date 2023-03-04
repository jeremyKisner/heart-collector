import pygame


class Heart(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.type = "heart"
        self.image = self.__load_main_image()
        self.get_image_dimensions()
        self.hp = 10


    def __load_main_image(self):
        image = pygame.image.load("./src/main/assets/Heart.png").convert_alpha()
        image = pygame.transform.scale(image, (25, 25))
        return image


    def get_image_dimensions(self):
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def draw(self, screen, x_pos, y_pos):
        screen.blit(self.image, (x_pos, y_pos))
        self.rect = pygame.Rect(x_pos, y_pos, self.width, self.height)
