from converters.base_conveter import BaseConverter

class TemperatureConveter(BaseConverter):
    def __init__(self):
        super().__init__()
        self.conversion_rates = {
            'C': {
                'F': self.celcius_to_fahrenheit,
                'K': self.celcius_to_kelvin,
                'C': self.to_self
            },
            'F': {
                'C': self.fahrenheit_to_celcius,
                'K': self.fahrenheit_to_kelvin,
                'F': self.to_self
            },
            'K': {
                'C': self.kelvin_to_celcius,
                'F': self.kelvin_to_fahrenheit,
                'K': self.to_self
            }
        }
    def celcius_to_fahrenheit(self, c):
        return (c * 9/5)+ 32
    
    def celcius_to_kelvin(self, c):
        return c - 273.15
    
    def fahrenheit_to_celcius(self, f):
        return (f - 32) * 5/9
    
    def fahrenheit_to_kelvin(self, f):
        return (f + 459.67) * 5/9
    
    def kelvin_to_celcius(self, k):
        return k + 273.15
    
    def kelvin_to_fahrenheit(self, k):
        return (k * 9/5) - 459.67