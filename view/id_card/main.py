from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 

KV ="""
GridLayout:
    rows: 5
    cols: 2

    MDLabel:
        id: mdlab
        text: "Benvenuto su greggy! Ora puoi selezionare un profilo che ti corrisponde."
        #size_hint_y: None
    MDRaisedButton:
        id: mdbu_pr1
        text: "PROFILO 1"
        #size_hint_x: 1.0
    MDRaisedButton:
        id: mdbu_pr2
        text: "PROFILO 2"
        #size_hint_x: 1.0
    MDRaisedButton:
        id: mdbu_pr3
        text: "PROFILO 3"
        #size_hint_x: 1.0
    MDRaisedButton:
        id: mdbu_pr4
        text: "PROFILO 4"
        #size_hint_x: 1.0
"""

class TestCard(MDApp):
    def build(self):
        return Builder.load_string(KV)

TestCard().run()
