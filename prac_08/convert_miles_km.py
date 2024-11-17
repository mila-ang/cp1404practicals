from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    output = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            self.output = str(miles * MILES_TO_KM)
        except ValueError:
            self.output = "0.0"
        self.root.ids.output_label.text = self.output

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
