import pygame as pyg
from pygame.constants import K_ESCAPE


#under construction...

class UIStyle:
    def __init__(self):
        pass
    def Dark():
        pass
    def Light():
        pass
    def OS():
        pass

class UIEventHandler:
    def __init__(self):
        pass
    def OnHover(grace,targetid):
        if targetid.rect.collidepoint(pyg.mouse.get_pos()):
            return(True)
    def OnClick(targetid):
        clicked = False
        if pyg.mouse_get_pressed()[0] and targetid.rect.collidepoint(pyg.mouse.get_pos()) and not clicked:
            clicked = pyg.mouse.get_pressed()[0]
            return(True)
    def OnDrag(targetid):
        while pyg.mouse_get_pressed() and targetid.rect.colldiepoint(pyg.mouse.get_pos()):
            return(True)
    def OnWrite(targetid):
        pass
    def OnEscape():
        paused = False
        pressed = False
        if pyg.KEYDOWN(K_ESCAPE) == True:
            pressed == pyg.KEYDOWN(K_ESCAPE)
            if pyg.KEYDOWN(K_ESCAPE) is True and paused is False:
                paused == True
            if pyg.KEYDOWN(K_ESCAPE) is True and paused is True:
                paused == False
            while paused is True:
                return(True)


class UIElementHandler:
    def __init__(self):
        pass
    def Scroll():
        pass
    def Button(name,id,command):
        pass
    def RadioButton(name,buttongroupid,groupname,groupid,commandgroupid):
        pass
    def TextBox(text,font,id,format,encoding):
        pass
    def ListBox(textlist,font,id,format,encoding):
        pass
    def ScrollBar(id):
        pass
    def Slider(id,text,vaulerange,command):
        pass
    def ToolTip(tooltiptext,tooltipname,grace,id):
        pass
    def WriteBox(display,id):
        pass


class UIHandler:
    def __init__(self):
        ui_scale = 1
        ui_trans = 0
        ui_type = 0
        controlls = {}
        vol = {}
    def Window(sizey,sizex,gridx,gridy,offserx,offsety,style,id):
        pass
    def SubWindow(sizey,sizex,gridx,gridy,offsetx,offsety,style,id,parentid):
        pass
    def ScrollWindow(sizey,sizex,gridx,gridy,offserx,offsety,style,id,scrollx,scrolly):
        pass