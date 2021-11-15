class ConfigHandler:
    userconfig = {}
    resolution = {"640":"360","960":"540","1280":"720","1600":"900","1920":"1080"}
    config = "config/config.cfg"
    def __init__(self,key,vaule):
        self.key = key
        self.vaule = vaule
    def DefaultConfig():
        from os.path import exists
        if exists(ConfigHandler.config) == True:
            pass
        else:
            default_config = {"height":"640","width":"360","windowed":"False","framerate":"30","master_sound":"100","ambiance_sound":"100","music":"100","player_sound":"100","ai_sound":"100","left":"K_LEFT","right":"K_RIGHT","jump":"K_SPACEBAR","down":"K_DOWN","use":"KEY_F","shoot":"MOUSE1","grenade":"MOUSE2","scroll":"MOUSEWHEEL"}
            with open(ConfigHandler.config,"x",encoding="UTF-8") as f:
                for i in default_config.items():
                    f.writelines(i)
    def UserConfig(self,key):
        with open(ConfigHandler.config,"r",encoding="UTF-8") as f:
            for i in f:
                self.userconfig.update(f.readlines(i))
                return(self.userconfig.get(key))   
    def UserConfigUpadte(self,key,vaule):
        with open(ConfigHandler.config,"w",encoding="UTF-8") as f:
            self.userconfig.update(key,vaule)
            for i in self.userconfig:
                f.writelines(i)

ConfigHandler.DefaultConfig()
