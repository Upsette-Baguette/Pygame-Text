import pygame

pygame.font.init()
myFont = pygame.font.SysFont("monospace", 17)
inpFont = pygame.font.SysFont("monospace", 22)

word = ""

screen = pygame.display.set_mode([800,100])
screen.fill((255,255,255))

label = myFont.render("Please input your vertical velocity. Press enter to confirm your value.", 1, (0,0,0))
screen.blit(label, (0, 0))

pointCount = 0

while True:
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			pygame.quit(); sys.exit();
		
		elif event.type == pygame.KEYDOWN:
			key = pygame.key.name(event.key)
			if key.isdigit() == True or key == "." and pointCount == 0:
				word += key
				if key == "." and pointCount == 0:
					pointCount += 1
					print pointCount
					print word[-1:]
		
		if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
				if word[-1:] == ".":
					pointCount -= 1
					print pointCount
				word = word[:-1]
				screen.fill((255,255,255))
				
		for char in word:
			userInput = inpFont.render(word, 1, (0,0,0))
			screen.blit(userInput, (0, 22))


