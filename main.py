from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider

class MyWidget(GridLayout):
    def selected(self, filename):
        try:
            self.ids.image.source = filename[0]

        except:
            pass

class FileChoserWindow(App):
    def build(self):

        return MyWidget()






if __name__ == '__main__':

    window = FileChoserWindow()
    window.run()