from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SuperGroupApp(App):
    def build(self):
        self.title = "Super Secret Group"
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='🔒 Super Secret Group', font_size=25))
        layout.add_widget(Label(text='Только для approved пользователей'))
        
        # Проверка доступа
        access_btn = Button(text='Проверить доступ', size_hint=(1, 0.2))
        access_btn.bind(on_press=self.check_access)
        layout.add_widget(access_btn)
        
        return layout
    
    def check_access(self, instance):
        print("Проверяем доступ через сервер...")
        # Здесь будет проверка через Telegram бота

if __name__ == '__main__':
    SuperGroupApp().run()
