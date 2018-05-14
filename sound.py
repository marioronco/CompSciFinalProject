song = pygame.mixer.Sound('sound.wav')
clock = pygame.time.Clock()
song.play()
while True:
    clock.tick(60)

song.play() 

https://stackoverflow.com/questions/45269664/why-does-this-code-to-play-a-sound-using-python-and-pygame-on-mac-not-load-the-f