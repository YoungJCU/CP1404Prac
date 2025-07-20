from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

__author__ = "Your Name"

MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    """Kivy App to convert miles to kilometers."""
    output_text = StringProperty()

    def build(self):
        """Build the Kivy app."""
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_text = "0.0 km"
        return self.root

    def handle_convert(self, value):
        """Handle conversion from miles to km."""
        try:
            miles = float(value)
            km = miles * MILES_TO_KM
            self.output_text = f"{km:.3f} km"
        except ValueError:
            self.output_text = "Invalid input"

    def handle_increment(self, value, step):
        """Handle incrementing or decrementing the value by step."""
        try:
            miles = float(value)
            miles += step
            self.root.ids.input_miles.text = str(miles)
            self.handle_convert(miles)
        except ValueError:
            pass


if __name__ == '__main__':
    ConvertMilesKmApp().run()
