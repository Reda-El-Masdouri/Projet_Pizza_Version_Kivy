from kivy.app import App
from kivy.properties import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.widget import Widget
from kivy.lang import Builder
from models import Pizza


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    # NumericProperty / BooleanProperty
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza("4 fromages", "chèvre, emmental, brie, comté", 9.5, True),
            Pizza("Chorizo", "tomates, chorizo, parmesan", 11.2, False),
            Pizza("Calzone", "fromage, jambon, champignons", 10, False)
        ]

    def on_parent(self, widget, parent):
        l = [pizza.get_dictionary() for pizza in self.pizzas]
        self.recycleView.data = l
    
    

with open("pizzascr.kv", encoding='utf8') as f:
    Builder.load_string(f.read())

class PizzaApp(App):
    def build(self):
        return MainWidget()


PizzaApp().run()