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
    IDCardScreen:
    AppliancesScreen:
    SimulationScreen:

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
        #on_press: app.verify_profile_choice() #FIXME
        on_press: root.manager.current = 'id_card'
<IDCardScreen>:
    name: 'id_card'
    MDLabel:
        text: 'ID Card'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Next'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'appliances'
        
<AppliancesScreen>:
    name: 'appliances'
    MDLabel:
        text: 'Appliances choice'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Next'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'simulation'

<SimulationScreen>:
    name: 'simulation'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Start again'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'choose_profile'
"""

class ChooseProfileScreen(Screen):
    pass

class IDCardScreen(Screen):
    pass

class AppliancesScreen(Screen):
    pass

class SimulationScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(ChooseProfileScreen(name='choose_profile'))
sm.add_widget(IDCardScreen(name='id_card'))
sm.add_widget(AppliancesScreen(name='appliances'))
sm.add_widget(SimulationScreen(name='simulation'))

class MainApp(MDApp):

    def build(self):
        self.title = "Greeggy"
        self.theme_cls.theme_style = "Light" # Light
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "400"
        self.profile = None
        screen = Builder.load_string(screen_helper)
        return screen

    def profile_selection(self,profile):
        self.root.get_screen('choose_profile').ids["mdlab"].text = "Profilo {} selezionato".format(profile)
        self.profile = profile

    def verify_profile_choice(self):
        #FIXME
        if self.profile is not None:
            #self.root.manager.current = 'id_card'
            sm.switch_to(sm.get_screen("id_card"))
        else:
            self.root.get_screen('choose_profile').ids["mdlab"].text = "Devi selezionare un profilo"

    def define_list_appliances(self):
        # Creating a Simple List
        scroll = ScrollView()
        screen = Screen()


        list_view = MDList()
        for i in range(20):

            # items = ThreeLineListItem(text=str(i) + ' item',
            #                          secondary_text='This is ' + str(i) + 'th item',
            #                          tertiary_text='hello')

            icons = IconLeftWidget(icon="android")
            items = OneLineIconListItem(text=str(i) + ' item')
            items.add_widget(icons)
            list_view.add_widget(items)

        scroll.add_widget(list_view)
        # End List

        screen.add_widget(scroll)
        return screen



MainApp().run()