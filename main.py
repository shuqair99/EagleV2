from kivy.app import App
from kivy.uix.button import Button

class EagleApp(App):
    def build(self):
        return Button(text="EAGLE V2 READY")

if __name__ == "__main__":
    EagleApp().run()
