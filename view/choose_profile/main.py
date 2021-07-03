# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:24:44 2021

@author: stefano
"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """

ScreenManager:
    ChooseProfileScreen:

<ChooseProfileScreen>:
    name: 'choose_profile'
    GridLayout:
        rows: 5

        MDLabel:
            id: mdlab
            text: "Benvenuto su greggy! Ora puoi selezionare un profilo che ti corrisponde."
            size_hint_y: None

        MDRaisedButton:
            id: mdbu_pr1
            text: "PROFILO 1"
            size_hint_x: 1.0
            on_press: app.profile_selection("1")
        MDRaisedButton:
            id: mdbu_pr2
            text: "PROFILO 2"
            size_hint_x: 1.0
            on_press: app.profile_selection("2")
        MDRaisedButton:
            id: mdbu_pr3
            text: "PROFILO 3"
            size_hint_x: 1.0
            on_press: app.profile_selection("3")
        MDRaisedButton:
            id: mdbu_pr4
            text: "PROFILO 4"
            size_hint_x: 1.0
            on_press: app.profile_selection("4")
    MDRectangleFlatButton:
        text: 'Next'
        pos_hint: {'center_x':0.5,'center_y':0.1}
"""

class ChooseProfileScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(ChooseProfileScreen(name='choose_profile'))

class MainApp(MDApp):

    def build(self):
        self.title = "Greeggy"
        self.theme_cls.theme_style = "Light" 
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "400"
        self.profile = None
        screen = Builder.load_string(screen_helper)
        return screen

    def profile_selection(self,profile):
        self.root.get_screen('choose_profile').ids["mdlab"].text = "Profilo {} selezionato".format(profile)
        self.profile = profile

MainApp().run()