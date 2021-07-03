from kivymd.app import MDApp
from kivy.lang import Builder

"""
from kivy.properties import StringProperty

#from kivy.network.urlrequest import UrlRequest
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, IconLeftWidget, OneLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
"""

class Greeggy1(MDApp):

    def build(self):
        self.title = "Greeggy"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "700"
        return Builder.load_file("main.kv")
        
if __name__=="__main__":
    Greeggy1().run()