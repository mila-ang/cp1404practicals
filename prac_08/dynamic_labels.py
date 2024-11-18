from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App to dynamically create labels for a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Define the list of names (model)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        """Build the Kivy app from the kv file and add dynamic labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a Label for each name in the list and add it to the main layout."""
        for name in self.names:
            label = Label(text=name, font_size=24)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()
