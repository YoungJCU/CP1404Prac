from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Simple Kivy app that creates labels dynamically from a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Model: list of names
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        """Build the GUI and dynamically create labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Label widgets dynamically based on names."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main_box.add_widget(label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
