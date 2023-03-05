import pygame


class Heart(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.type = "heart"
        self.image = self.__load_main_image()
        self.__get_image_dimensions()
        self.hp = 10
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)


    def __load_main_image(self):
        image = pygame.image.load("./src/main/assets/Heart.png").convert_alpha()
        image = pygame.transform.scale(image, (25, 25))
        return image


    def __get_image_dimensions(self):
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
