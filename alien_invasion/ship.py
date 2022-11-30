class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game=None):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取外界矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘飞船，都将其放在屏幕底部中央位置
        self.rect.midbottom = self.screen.rect_midbottom

        # 移动标志
        self.moving_right = False
        self.moving_left = True

    def update(self):
        if self.moving_right:
            self.rect += 1
        if self.moving_left:
            self.rect += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
