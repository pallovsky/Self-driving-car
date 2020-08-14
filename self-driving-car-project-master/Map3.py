import pygame


class Map:
    def __init__(self, scale):
        self.out_path = [
            (1, 1),
            (1, 8),
            (2, 10),
            (2, 12),
            (1, 14),
            (1, 20),
            (4, 20),
            (7, 19),
            (13, 19),
            (15, 20),
            (21, 20),
            (21, 13),
            (18, 11),
            (14, 11),
            (13, 14),
            (8, 13),
            (10, 8),
            (21, 8),
            (21, 1),
            (1, 1)
        ]

        self.in_path = [
            (4, 3),
            (4, 17),
            (18, 17),
            (18, 14),
            (16, 16),
            (5, 16),
            (6, 5),
            (18, 5),
            (18, 4),
            (12, 4),
            (10, 3),
            (4, 3)
        ]
        self.scale(scale)
        self.translate(20, 20)

    def scale(self, scale):
        self.out_path = [(x * scale, y * scale) for x, y in self.out_path]
        self.in_path = [(x * scale, y * scale) for x, y in self.in_path]

    def translate(self, a, b):
        self.out_path = [(x + a, y + b) for x, y in self.out_path]
        self.in_path = [(x + a, y + b) for x, y in self.in_path]

    def draw(self, screen, color):
        pygame.draw.lines(screen, color, False, self.out_path)
        pygame.draw.lines(screen, color, False, self.in_path)

