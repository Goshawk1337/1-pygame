import pygame
import texture

class tile:
    def __innit__(Tile,texture,posx,posy,posz,solid):
        Tile.texture = texture
        Tile.posx = posx
        Tile.posy = posy
        Tile.posz = posz
        Tile.solid = solid
        if tile.solid == 1:
            pygame.sprite.spritecollide()
        elif tile.solid == -1:
            pygame.sprite.spritecollideany()
        else:
            pass


        