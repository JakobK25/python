import pygame
from pygame import mixer

mixer.init()

mixer.music.load('click.mp3')

mixer.music.set_volume(1)

mixer.music.play()