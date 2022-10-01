from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import *
from kivy.lang import Builder
import random

def reset():
 import kivy.core.window as window
 from kivy.base import EventLoop
 if not EventLoop.event_listeners:
    from kivy.cache import Cache
    window.Window = window.core_select_lib('window', window.window_impl, True)
    Cache.print_usage()
    for cat in Cache._categories:
        Cache._objects[cat] = {}



Builder.load_string('''
#:import utils kivy.utils
<LifeCounter>:
    BoxLayout:
        orientation: "vertical"

        Button:
            text: 'Random Number between 0 and 100: '+str(root.count)
            font_size:"25sp"
            color: utils.get_color_from_hex('#03A9F4')
            background_color: utils.get_color_from_hex('#58AE6F')
            on_release: root.incr()


''')

#%background_color: 1, 0, 0, 1

class LifeCounter(BoxLayout):
    count = NumericProperty(0)
    tex = StringProperty()
    def __init__(self, **kwargs):
        super(LifeCounter, self).__init__(**kwargs)

    def incr(self):
        self.count = random.randint(0,100)
        self.tex = 'Random number: '
        

class DemoApp(App):
    def build(self):
        return LifeCounter()

if __name__ == '__main__':
    reset()
    DemoApp().run() 