from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
Screen:
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
"""
class MainApp(MDApp):

    def build(self):
        self.title = "Greeggy"
        self.theme_cls.theme_style = "Light" # Light
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "600"
        return Builder.load_string(KV)

    def profile_selection(self,profile):
        self.root.ids["mdlab"].text = "Profilo {} selezionato".format(profile)

MainApp().run()