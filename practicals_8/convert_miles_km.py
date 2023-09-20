from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty

KM_PER_MILE = 1.609344


class ConvertMilesToKmApp(App):

    km_output = StringProperty()

    def build(self):

        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert_miles_to_km(self, miles_input):

        miles = self.convert_text_to_number(miles_input)
        self.km_output = str(miles * KM_PER_MILE)

    def handle_increment(self, increment):

        miles = self.convert_text_to_number(self.root.ids.miles_input.text)
        miles += increment
        self.root.ids.miles_input.text = str(miles)

    @staticmethod
    def convert_text_to_number(text):

        try:
            number = float(text)
        except ValueError:
            number = 0.0
        return number


ConvertMilesToKmApp().run()
