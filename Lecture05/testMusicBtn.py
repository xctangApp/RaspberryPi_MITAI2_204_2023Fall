import pygame
from gpiozero import Button

pygame.init()

#drum = pygame.mixer.Sound("/home/pi/gpio_music_box/drum_tom_hi_soft.wav")
#drum = pygame.mixer.Sound("/home/pi/Desktop/drum_tom_mid_hard.wav")
drum = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_tom_mid_hard.wav")


#cymbal = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cymbal_hard.wav")
#snare = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_snare_hard.wav")
#bell = pygame.mixer.Sound("/home/pi/gpio-music-box/samples/drum_cowbell_hard.wav")

btn_drum = Button(17)
btn_drum.when_pressed = drum.play
