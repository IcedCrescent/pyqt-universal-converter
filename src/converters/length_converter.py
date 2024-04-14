from converters.base_conveter import BaseConverter


class LengthConverter(BaseConverter):
    def __init__(self):
        super().__init__()

        self.conversion_rates = {
            'cm': {  # Centimeters
                'm': lambda cm: cm / 100,
                'km': lambda cm: cm / 100000,
                'yd': lambda cm: cm / 91.44,
                'ft': lambda cm: cm / 30.48,
                'mi': lambda cm: cm / 160934,
                'cm': self.to_self
            },
            'm': {  # Meters
                'cm': lambda m: m * 100,
                'km': lambda m: m / 1000,
                'yd': lambda m: m / 0.9144,
                'ft': lambda m: m / 0.3048,
                'mi': lambda m: m / 1609.34,
                'm': self.to_self
            },
            'km': {  # Kilometers
                'cm': lambda km: km * 100000,
                'm': lambda km: km * 1000,
                'yd': lambda km: km * 1093.61,
                'ft': lambda km: km * 3280.84,
                'mi': lambda km: km / 1.60934,
                'km': self.to_self
            },
            'yd': {  # Yards
                'cm': lambda yd: yd * 91.44,
                'm': lambda yd: yd * 0.9144,
                'km': lambda yd: yd / 1093.61,
                'ft': lambda yd: yd * 3,
                'mi': lambda yd: yd / 1760,
                'yd': self.to_self
            },
            'ft': {  # Feet
                'cm': lambda ft: ft * 30.48,
                'm': lambda ft: ft * 0.3048,
                'km': lambda ft: ft / 3280.84,
                'yd': lambda ft: ft / 3,
                'mi': lambda ft: ft / 5280,
                'ft': self.to_self
            },
            'mi': {  # Miles
                'cm': lambda mi: mi * 160934,
                'm': lambda mi: mi * 1609.34,
                'km': lambda mi: mi * 1.60934,
                'yd': lambda mi: mi * 1760,
                'ft': lambda mi: mi * 5280,
                'mi': self.to_self
            },
        }