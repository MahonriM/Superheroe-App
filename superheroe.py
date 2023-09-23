import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
Builder.load_string(
    '''
<MyGrid>:
    name:name
    power:power
    p:p
    GridLayout:
        cols:1
        size:root.width,root.height
        GridLayout:
            cols:2
            Label:
                text:"Introduce your super heroe name"
            TextInput:
                id:name
                multiline:False
            Label:
                text:"Introduce your suporpower"
            TextInput:
                id:power
                multiline:False
            Button:
                text:"Give me Super powers"
                on_press:root.superpower()
            Label:
                id:p
                text:""
''')
class MyGrid(Widget):
    name=ObjectProperty(None)
    power=ObjectProperty(None)
    def superpower(self):
        name=self.name.text
        power=self.power.text
        self.p.text=(f"You are {name} and you power is {power} ")
class MyApp(App):
    def build(self):
        return MyGrid()
if __name__=="__main__":
    MyApp().run()