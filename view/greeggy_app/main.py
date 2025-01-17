from kivy.lang import Builder
from kivy.properties import StringProperty

#from kivy.network.urlrequest import UrlRequest
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, IconLeftWidget, OneLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons

import pandas as pd

def import_personas(fileName,gender):
    df = pd.read_csv(fileName,delimiter=';')
    df['persona'] = df.apply(lambda persona: persona.Name+"_"+persona.Surname,axis=1)
    personas_list = list(set(df["persona"]))
    personas = {}
    cont=0
    for persona in personas_list:
        tmp_df = df[df["persona"]==persona]
        cont+=1
        personas[str(cont)] = {}
        personas[str(cont)]["Name"] = list(set(tmp_df["Name"]))[0]
        personas[str(cont)]["Surname"] = list(set(tmp_df["Surname"]))[0]
        personas[str(cont)]["Age"] = list(set(tmp_df["Age"]))[0]
        personas[str(cont)]["Status"] = list(set(tmp_df["Status"]))[0]
        personas[str(cont)]["Icon"] = list(set(tmp_df["Image"]))[0]+"_"+gender+".png"
        personas[str(cont)]["Activities"] = {}
        personas[str(cont)]["Appliances"] = {}
        for elt in list(set(tmp_df["Activities"])):
            personas[str(cont)]["Activities"][elt] = {}
            app_list = list(set(tmp_df[tmp_df["Activities"]==elt]["Appliances involved"]))
            for app in app_list:
                personas[str(cont)]["Appliances"][app]=tmp_df[(tmp_df["Activities"]==elt)&(tmp_df["Appliances involved"]==app)]["Sentiment"].values[0]
    
    return personas

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''

class Greeggy(MDApp):

    info_dialog = None
    contact_dialog = None

    def build(self):
        self.gender = "f"
        self.title = "Greeggy"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "400"
        return Builder.load_file("main.kv")

    def show_app_info_dialog(self):
        app_info = "Greeggy App\n\nMade to help in solving climate issues"
        if not self.info_dialog:
            self.info_dialog = MDDialog(
                title = "Informazioni App",
                text = app_info,
                auto_dismiss = True
            )
        self.info_dialog.open()

    def show_contact_info_dialog(self):
        andrea = "andrea.puricelli@mip.polimi.it"
        stefano = "stefano.pastoris@mip.polimi.it"
        ogi = "ognjen.obersnel@mip.polimi.it"
        app_info = "Contatti:\n\n{}\n{}\n{}".format(andrea,stefano,ogi)
        if not self.contact_dialog:
            self.contact_dialog = MDDialog(
                title = "I Nostri Contatti",
                text = app_info,
                auto_dismiss = True
            )
        self.contact_dialog.open()

    def show_text(self):
        strout = "Greeggy é un semplice gioco che ti permette di sperimentare come ridurre i consumi energetici,"
        strout += " in particolare durante i picchi di domanda di energia elettrica.\n"
        strout += "Step 1 - Selezionare un profilo di consumatore.\n"
        strout += "Step 2 - Analizzare la sua carta di identità per comprendere le sue abitudini.\n"
        strout += "Step 3 - Selezionare quali elettrodomestici bloccare per ridurre i consumi.\n\n"
        strout += "L'obiettivo del gioco consiste nel massimizzare il risparmio energetico senza degradare eccessivamente il benessere del consumatore che hai scelto.\n"
        strout += "Sei pronto per la sfida?"
        return strout

    def profile_selection(self,profile):
        self.personas = import_personas("./personas/Personas.csv",self.gender)

        str_id="Nome: {}\n".format(self.personas[profile]["Name"])
        str_id+="Cognome: {}\n".format(self.personas[profile]["Surname"])
        str_id+="Età: {}\n".format(self.personas[profile]["Age"])
        str_id+="Stato: {}".format(self.personas[profile]["Status"])
        self.root.ids["md_idcard"].text = str_id

        str_act="Attività:\n"
        for elt in self.personas[profile]["Activities"].keys():
            str_act+= "- {}\n".format(elt)
        self.root.ids["md_act"].text = str_act

        self.root.ids["md_persona_img"].source = "./personas/"+self.personas[profile]["Icon"]
        
        self.profile = profile

    def gender_selection(self,gender):
        self.gender = gender

    """
    def on_start(self):
        for i in range(5):
            #icon = IconLeftWidget(icon="./images/fan.jpg")
            item = OneLineListItem(text='Item ' + str(i), icon="./images/fan.jpg")
            #item.add_widget(icon)
            self.root.ids.container.add_widget(item)
    """

    def on_start(self):
        #icons = list(md_icons.keys())
        self.appliances=[
            ("air_conditioner","condizionatore"),
            ("dishwasher","lavastoviglie"),
            ("hair_dryer","asciugacapelli"),
            ("fridge","frigorifero"),
            ("fan","stufetta"),
            ("washing_machine","lavatrice"),
            ("microwave","micronde"),
            ("oven","forno"),
            ("tv","tv"),
            ("pc","pc"),
            ("coffee_machine","macchinetta del caffé"),
            ("console","console"),
            ("stereo","stereo"),
            ("cooker_hood","cappa aspirante"),
            ("hair_straightener","stiracapelli"),
            ("kneader","impastatrice"),
            ("treadmill","tapis roulant"),
            ("exercise_bike","cyclette"),
            ("kitchen_robot","robot da cucina"),
            ("lamp","lampada"),
            ("printer","stampante"),
            ("tablet","tablet"),
            ("laptop","laptop"),
            ("electric_heater","stufetta"),
            ("headphones","cuffie"),
            ("mixer","mixer"),
            ("hoover","aspirapolvere")]

        self.list_en = [i[0] for i in self.appliances]
        self.list_it = [i[1] for i in self.appliances]

        for i in self.appliances:
            self.root.ids.scroll.add_widget(
                ListItemWithCheckbox(text=i[1], icon="./images/{}.jpg".format(i[0]))
            )

    def get_active_check(self):
        app_activation = {}
        app_activation["active"] = []
        app_activation["inactive"] = []
        for ListItemWithCheckbox in self.root.ids.scroll.children:
            item_it = ListItemWithCheckbox.text
            item_en = self.list_en[self.list_it.index(item_it)]
            if ListItemWithCheckbox.ids.check.active:
                app_activation["inactive"].append(item_en)
            else:
                app_activation["active"].append(item_en)

        return app_activation

    def simulation(self):
        app_act_dict = self.get_active_check()
        sentiment = 100
        persona_profile = self.personas[self.profile]
        for app_sel in persona_profile["Appliances"].keys():
            if app_sel in app_act_dict["inactive"]:
                sentiment-=int(persona_profile["Appliances"][app_sel])

        name = persona_profile["Name"]
        if sentiment >= 50:
            self.root.ids["md_simu"].text = "Complimenti, {} é contento/a di aver risparmiato senza troppo rinunciare alle proprie abitudini, {}".format(name,str(sentiment))
        else:
            self.root.ids["md_simu"].text = "Ci spiace ma {} é depresso/a per le troppe rinuncie, {}".format(name,str(sentiment))

Greeggy().run()

