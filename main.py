from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text='🔒 MrAnatas9 Secret Group', font_size=30))
        layout.add_widget(Label(text='Только для проверенных пользователей'))
        
        self.user_input = TextInput(hint_text='Введите ваш ID', multiline=False)
        layout.add_widget(self.user_input)
        
        login_btn = Button(text='Войти в систему', size_hint=(1, 0.2), background_color=(0, 0.5, 1, 1))
        login_btn.bind(on_press=self.check_access)
        layout.add_widget(login_btn)
        
        self.add_widget(layout)
    
    def check_access(self, instance):
        user_id = self.user_input.text
        if user_id.lower() == "mranatas9" or user_id == "admin":
            self.manager.current = 'admin_panel'
        else:
            self.manager.current = 'user_chat'

class UserChatScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='💬 Группа MrAnatas9', font_size=25))
        layout.add_widget(Label(text='Вы вошли как пользователь\nИмена скрыты для конфиденциальности'))
        self.add_widget(layout)

class AdminPanelScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=5)
        
        layout.add_widget(Label(text='👑 ПАНЕЛЬ MRANATAS9', font_size=20, color=(1, 0, 0, 1)))
        
        functions = [
            ('📨 Просмотр всех сообщений', self.view_messages),
            ('👥 Просмотр ЛС пользователей', self.view_private),
            ('🚫 Блокировка пользователей', self.ban_users),
            ('⚙️ Настройки системы', self.settings),
            ('🔍 Мониторинг активности', self.monitor)
        ]
        
        for text, func in functions:
            btn = Button(text=text, size_hint=(1, 0.15))
            btn.bind(on_press=func)
            layout.add_widget(btn)
        
        self.add_widget(layout)
    
    def view_messages(self, instance): print("Режим просмотра сообщений...")
    def view_private(self, instance): print("Доступ к ЛС пользователей...")
    def ban_users(self, instance): print("Управление блокировками...")
    def settings(self, instance): print("Системные настройки...")
    def monitor(self, instance): print("Мониторинг активности...")

class MrAnatas9App(App):
    def build(self):
        self.title = "MrAnatas9 Secret System"
        
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(UserChatScreen(name='user_chat'))
        sm.add_widget(AdminPanelScreen(name='admin_panel'))
        
        return sm

if __name__ == '__main__':
    MrAnatas9App().run()
