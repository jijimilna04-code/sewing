from kivy.app import App
from kivy.uix.label import Label
import arabic_reshaper
from bidi.algorithm import get_display

class SewingApp(App):
    def build(self):
        text = "مرحباً بك في تطبيق الخياطة"
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)
        return Label(text=bidi_text)

if __name__ == '__main__':
    SewingApp().run()
