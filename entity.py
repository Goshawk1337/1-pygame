import pygame as pyg

# under contruction
# any variable beyond 'id' will be optional w defaults given if not declared

class Entity(pyg.sprite.Sprite):
    def __init__(self):
        pyg.sprite.Sprite.__init__(self)
    def Destructible(health,id,explosive,damage):
        pass
    def Rotator(originy,originx,id,speed,crusher):
        pass
    def Mover(originy,originx,speed,pathid,id,respawn,delay,ontouch,crusher):
        pass
    def Faller(originy,originx,speed,delay,id,ontouch,crusher):
        pass
    def Pushable(originy,originx,frict,id,grav,crusher):
        pass
    def Path(id,target):
        pass
    def AIBlock(posx,posy):
        pass
    def Teleport(posx,posy,sizex,sizey,target):
        pass
    def HPPickup(posx,posy,amount,id,overheal,respawn,delay):
        pass
    def AmmoPickup(posx,posy,type,amount,id,respawn,dealy):
        pass
    def Key(posx,posy,id):
        pass
    def Flag(posx,posy,id,dropable,rdelay):
        pass
    def Button(originy,originx,target,id,sound,reuse):
        pass
    def Emitter(posx,posy,particle,id,fade,delay):
        pass
    def Shooter(posx,posy,weap,target,id,homing):
        pass