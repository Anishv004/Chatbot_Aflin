from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase

Window.size = (350, 550)


class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    
    font_size = 17


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    
    font_size = 17


class ResponseImage(Image):
    source = StringProperty()


class ChatBot(MDApp):

    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats.kv"))
        return screen_manager

    def bot_name(self):
        # if screen_manager.get_screen('main').bot_name.text != "":
        #     screen_manager.get_screen('chats').bot_name.text = screen_manager.get_screen('main').bot_name.text
        screen_manager.current = "chats"

    def response(self, *args):
        response = ""
        if value == "Hello" or value == "hello":
            response = f"Hello. I Am Your Personal Assistant {screen_manager.get_screen('chats').bot_name.text}."
        elif value == "How are you?" or value == "how are you?":
            response = "I'm doing well. Thanks!"
        elif value == "Images":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="chatbots.jpg"))
        elif value == "Images1":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source="1.png"))
        else:
            response = "Sorry could you say that again?"
        screen_manager.get_screen('chats').chat_list.add_widget(Response(text=response, size_hint_x=.75))

    def send(self):
        global size, halign, value
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) < 6:
                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen_manager.get_screen('chats').chat_list.add_widget(
                Command(text=value, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response, 2)
            screen_manager.get_screen('chats').text_input.text = ""


if __name__ == '__main__':
    
    ChatBot().run()
