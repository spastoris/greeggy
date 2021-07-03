from kivymd.uix.boxlayout import MDBoxLayout
from kivy.app import runTouchApp

"""
layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
# Make sure the height is such that there is something to scroll.
layout.bind(minimum_height=layout.setter('height'))
for i in range(100):
    btn = Button(text=str(i), size_hint_y=None, height=40)
    layout.add_widget(btn)
root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)
"""
#MDBoxLayout:
#    adaptive_height: True
#    md_bg_color: app.theme_cls.primary_color
root = MDBoxLayout(adaptive_height=True,md_bg_color=theme_cls.primary_color)
#root.add_widget(layout)

runTouchApp(root)