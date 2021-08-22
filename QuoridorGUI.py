import pygame
import os

WIDTH, HEIGHT = (900, 900)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quoridor")
WHITE = (255, 255, 255)
FPS = 60

#BOARD_IMAGE = pygame.image.load(os.path.join("Assets", "board_image.png")
#PLAYER_1_IMAGE +
#

def draw_window():
	WIN.fill(WHITE)
	WIN.blit(#ADD PLAYER IMAGES HERE, fences on side of screen)
	pygame.display.update()

def main():
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		draw_window()
	pygame.quit()

if __name__ == "__main__":
	main()