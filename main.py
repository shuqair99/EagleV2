from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

# إعداد لون الخلفية (اختياري)
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class EagleV2(App):
    def build(self):
        # الواجهة الرئيسية
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # عنوان التطبيق
        self.label = Label(
            text="EAGLE V2 CHECKER", 
            font_size='32sp', 
            bold=True,
            color=(0, 1, 0, 1) # لون أخضر
        )
        
        # زرار تجريبي
        btn = Button(
            text="START CHECKING",
            size_hint=(1, 0.2),
            background_color=(0, 0.7, 0, 1)
        )
        btn.bind(on_press=self.on_click)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def on_click(self, instance):
        self.label.text = "Initializing Scanner..."
        self.label.color = (1, 1, 0, 1) # أصفر

if __name__ == "__main__":
    EagleV2().run()
