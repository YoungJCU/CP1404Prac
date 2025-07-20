from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

__author__ = "Young"

MILES_TO_KM = 1.60934

class ConvertMilesKmApp(App):
    """App for converting miles to kilometers with live update."""
    output_text = StringProperty("0.0 km")

    def build(self):
        """Load the Kivy GUI."""
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, text):
        """Convert miles to km; handle invalid input."""
        try:
            miles = float(text)
        except ValueError:
            miles = 0
        km = miles * MILES_TO_KM
        self.output_text = f"{km:.3f} km"

    def handle_increment(self, text, delta):
        """Increase/decrease miles, treating invalid as 0."""
        try:
            miles = float(text)
        except ValueError:
            miles = 0
        miles += delta
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert(miles)

if __name__ == '__main__':
    ConvertMilesKmApp().run()