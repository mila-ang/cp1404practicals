from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesToKmApp(App):
    output = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            self.output = str(miles * 1.60934)
            self.root.ids.output_label.text = self.output
        except ValueError:
            self.root.ids.output_label.text = "0.0"

    def handle_up(self):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles += 1
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def handle_down(self):
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles -= 1
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()


MilesToKmApp().run()
