import pygame
from pygame.locals import *

class CameraController:
    def __init__(self, x, y, z):
        self.xPos, self.yPos, self.zPos = x, y, z
        self.xRot, self.yRot = 0, 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    self.move_forward(0.1)
                elif event.key == K_s:
                    self.move_backward(0.1)
                elif event.key == K_a:
                    self.strafe_left(0.1)
                elif event.key == K_d:
                    self.strafe_right(0.1)
            elif event.type == MOUSEMOTION:
                dx, dy = event.rel
                self.rotate(dy * 0.1, dx * 0.1)

    def move_forward(self, distance):
        self.xPos += distance * math.sin(math.radians(self.yRot))
        self.zPos -= distance * math.cos(math.radians(self.yRot))

    def move_backward(self, distance):
        self.xPos -= distance * math.sin(math.radians(self.yRot))
        self.zPos += distance * math.cos(math.radians(self.yRot))

    def strafe_left(self, distance):
        self.xPos -= distance * math.sin(math.radians(self.yRot - 90))
        self.zPos += distance * math.cos(math.radians(self.yRot - 90))

    def strafe_right(self, distance):
        self.xPos -= distance * math.sin(math.radians(self.yRot + 90))
        self.zPos += distance * math.cos(math.radians(self.yRot + 90))

    def rotate(self, pitch, yaw):
        self.xRot += pitch
        self.yRot += yaw

# Initialisation de Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

camera = CameraController(0, 0, 0)

while True:
    camera.handle_events()

    # Mise à jour de la position et de la rotation de la caméra
    glLoadIdentity()
    glRotatef(camera.xRot, 1, 0, 0)
    glRotatef(camera.yRot, 0, 1, 0)
    glTranslatef(-camera.xPos, -camera.yPos, -camera.zPos)

    # Dessinez ici votre scène Minecraft

    pygame.display.flip()
    pygame.time.wait(10)
