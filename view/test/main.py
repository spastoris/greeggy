import certifi
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
        self.title = "WikipediaReader"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "400"
        return Builder.load_file("main.kv")

    def normal_search_button(self):
        query = self.root.ids["mdtext"].text
        self.get_data(title=query)

    def random_search_button(self):
        endpoint = "https://it.wikipedia.org/w/api.php?action=query&list=random&rnlimit=1&rnnamespace=0&format=json"
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint,
                                     on_success=self.get_data,
                                     ca_file=certifi.where())

    def get_data(self, *args, title=None):
        if title == None:
            response = args[1]
            random_article = response["query"]["random"][0]
            title = random_article["title"]
        endpoint = f"https://it.wikipedia.org/w/api.php?prop=extracts&explaintext&exintro&format=json&action=query&titles={title.replace(' ', '%20')}"
        self.data_request = UrlRequest(endpoint,
                                       on_success=self.set_textarea,
                                       ca_file=certifi.where())

    def set_textarea(self, request, response):
        page_info = response["query"]["pages"]
        page_id = next(iter(page_info))
        page_title = page_info[page_id]["title"]
        try:
            content = page_info[page_id]["extract"]
        except KeyError:
            content = f"Ci spiace, ma la ricerca '{page_title}' non ha prodotto risultati!\n\nRiprova! "
        self.root.ids["mdlab"].text = f"{page_title}\n\n{content}"

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
        self.dict_appliances={}
        self.dict_appliances["air_conditioner"] = "Condizionatore"
        self.dict_appliances["dishwasher"] = "Lavastoviglie"
        self.dict_appliances["hair_dryer"] = "Asciugacapelli"
        self.dict_appliances["fridge"] = "Frigorifero"
        self.dict_appliances["fan"] = "Stufetta"
        self.dict_appliances["washing_machine"] = "Lavatrice"
        self.dict_appliances["microwave"] = "Micronde"
        self.dict_appliances["oven"] = "Forno"
        self.dict_appliances["tv"] = "TV"
        self.dict_appliances["pc"] = "PC"
        self.dict_appliances["coffee_machine"] = "Macchinetta del caffé"
        self.dict_appliances["Console"] = "console"
        self.dict_appliances["Stereo"] = "stereo"
        self.dict_appliances["cooker_hood"] = "Cappa aspirante"
        self.dict_appliances["hair_straightener"] = "Stiracapelli"
        self.dict_appliances["kneader"] = "Impastatrice"
        self.dict_appliances["treadmill"] = "Tapis roulant"
        self.dict_appliances["exercise_bike"] = "Cyclette"
        self.dict_appliances["kitchen_robot"] = "Robot da cucina"
        self.dict_appliances["lamp"] = "Lampada"
        self.dict_appliances["printer"] = "Stampante"
        self.dict_appliances["tablet"] = "Tablet"
        self.dict_appliances["laptop"] = "Laptop"
        self.dict_appliances["electric_heater"] = "Stufetta"
        self.dict_appliances["headphones"] = "Cuffie"
        self.dict_appliances["mixer"] = "Mixer"
        self.dict_appliances["hoover"] = "Aspirapolvere"

        for i in self.dict_appliances.keys():
            self.root.ids.scroll.add_widget(
                ListItemWithCheckbox(text=self.dict_appliances[i], icon="./images/{}.jpg".format(i))
            )

    def get_active_check(self):
        app_activation = {}
        app_activation["active"] = []
        app_activation["inactive"] = []
        for ListItemWithCheckbox in self.root.ids.scroll.children:
            if ListItemWithCheckbox.ids.check.active:
                app_activation["active"].append(ListItemWithCheckbox.text)
            else:
                app_activation["inactive"].append(ListItemWithCheckbox.text)

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
            self.root.ids["md_simu"].text = "Complimenti, {} é contento/a di aver risparmiato senza troppo rinunciare alle proprie abitudini".format(name)
        else:
            self.root.ids["md_simu"].text = "Ci spiace ma {} é depresso/a per le troppe rinuncie".format(name)

Greeggy().run()

