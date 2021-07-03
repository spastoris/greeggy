import pandas as pd

df = pd.read_csv('Personas.csv',delimiter=';')
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
    personas[str(cont)]["Icon"] = list(set(tmp_df["Image"]))[0]
    personas[str(cont)]["Activities"] = {}
    for elt in list(set(tmp_df["Activities"])):
        app_list = list(set(tmp_df[tmp_df["Activities"]==elt]["Appliances involved"]))
        for app in app_list:
            personas[str(cont)]["Activities"][app]=tmp_df[(tmp_df["Activities"]==elt)&(tmp_df["Appliances involved"]==app)]["Sentiment"].values[0]
    

print(personas)