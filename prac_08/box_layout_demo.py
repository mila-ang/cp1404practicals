from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greeting when 'Greet' button is pressed."""
        name = self.root.ids.input_name.text
        if name.strip():
            self.root.ids.output_label.text = f"Hello {name}"
        else:
            self.root.ids.output_label.text = "Hello"

    def handle_clear(self):
        """Handle the clearing of text fields when 'Clear' button is pressed."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
