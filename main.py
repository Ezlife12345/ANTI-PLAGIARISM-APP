import os
import difflib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


class AntiPlagiarismChecker(BoxLayout):
    def check_plagiarism(self):
        # Get the content of the copied and original text
        copied_text = self.ids.copied_text_box.text
        original_text = self.ids.original_text_box.text

        # Split the text into lines and compare them
        copied_lines = copied_text.splitlines()
        original_lines = original_text.splitlines()

        for line in copied_lines:
            if line in original_lines:
                index = original_lines.index(line)
                self.ids.original_text_box.select_text(index, index + len(line))


class Root(BoxLayout):
    pass


class AntiPlagiarismCheckerApp(MDApp):
    def build(self):
        # Load the KV file
        kv = Builder.load_file("main.kv")

        # Set window size
        Window.size = (480, 800)

        # Create the app layout
        layout = Root()

        return kv


if __name__ == "__main__":
    AntiPlagiarismCheckerApp().run()
