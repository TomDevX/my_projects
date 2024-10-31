pip install pygame
import pygame
import random
from pygame import mixer

class Bird:
    def __init__(self):
        pygame.init()  # Init pygame
        self.xScreen, self.yScreen = 500, 600  # Screen create
        linkBackGround = "city.jpeg"  # Đường dẫn ảnh background
        self.linkImgBird = "flappy.png"  # Đường dẫn ảnh bird
        self.screen = pygame.display.set_mode(
            (self.xScreen, self.yScreen))  # Khởi tao kích thước màn hình
        pygame.display.set_caption("Code Learn - Flappybird")
        self.background = pygame.image.load(linkBackGround)
        self.gamerunning = True
        icon = pygame.image.load(self.linkImgBird)
        pygame.display.set_icon(icon)
        # --------------------------------------------------------
        self.xSizeBird = 80  # Chiều cao ảnh Bird
        self.ySizeBird = 60  # Chiều rộng ảnh Bird
        self.xBird = self.xScreen/3  # Vị trí bạn đầu của bird
        self.yBird = self.yScreen/2
        self.VBirdUp = 70  # Tốc độ nhảy bird
        self.VBirdDown = 7  # Tốc độ rớt bird
        # ------------------------------
        self.xColunm = self.yScreen+250  # khởi tạo cột đầu tiên
        self.yColunm = 0
        self.xSizeColunm = 100  # Chiều rộng cột
        self.ySizeColunm = self.yScreen
        self.Vcolunm = 6  # Tốc độ cột di chuyển
        self.colunmChange = 0

        self.scores = 0
        self.checkLost = False

 def music(self, url):  # Âm thanh
        bulletSound = mixer.Sound(url)
        bulletSound.play()
