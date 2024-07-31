from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.title = 'Simple Kivy App'
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Hello, Kivy!', font_size='24sp')
        btn = Button(text='Change Text')
        btn.bind(on_press=self.change_text)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def change_text(self, instance):
        self.label.text = 'Text Changed!'

if __name__ == '__main__':
    MyApp().run()
