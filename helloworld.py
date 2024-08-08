from manim import Scene, Text, Write
from manim import *

class hello(Scene):
    def construct(self):   
        text = Text("Hello guys!")
        self.play(Write(text))
        self.wait(3)
        self.remove(text)
        text = Text("This is my first animation !")
        self.play(Write(text))
        self.wait(3)