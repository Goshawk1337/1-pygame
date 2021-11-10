from os import write
import pygame
import tilehandler

class level_load:
    def __init__(path_to_level):
        level_load.path = path_to_level
        with open(path_to_level) as f:
            pass




class level_save:
    def __init__(path_to_level,savedata):
        level_save.path_to_level = path_to_level
        level_save.savedata = savedata
        with open(path_to_level,"w") as f:
            savedata = f.write(savedata)