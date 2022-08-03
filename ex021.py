#programa que abra mp3

import pygame

pygame.init()

pygame.mixer.music.load("podcast.mp3")
pygame.mixer.music.play()
pygame.event.wait()
