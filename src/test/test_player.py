import unittest
import src.main.player as t
import pygame

class TestPlayer(unittest.TestCase):

    pygame.init()
    screen = pygame.display.set_mode((800, 400))

    def test_player_initialize(self):
        p = t.Player()
        self.assertIsNotNone(p.get_current_health())


    def test_none_set_current_health(self):
        p = t.Player()
        temp_current_health = p.get_current_health()
        p.set_current_health(None)
        self.assertEqual(temp_current_health, p.get_current_health())


    def test_add_set_current_health(self):
        p = t.Player()
        temp_current_health = p.get_current_health()
        p.set_current_health(1)
        self.assertEqual(temp_current_health + 1, p.get_current_health())


    def test_minus_set_current_health(self):
        p = t.Player()
        temp_current_health = p.get_current_health()
        p.set_current_health(-1)
        self.assertEqual(temp_current_health - 1, p.get_current_health())
        p.set_current_health(-100000)
        self.assertEqual(0, p.get_current_health())
