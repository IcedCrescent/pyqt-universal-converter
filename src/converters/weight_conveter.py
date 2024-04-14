from converters.base_conveter import BaseConverter


class WeightConverter(BaseConverter):
    def __init__(self):
        super().__init__()

        self.conversion_rates = {
            'g': {
                'kg': self.gram_to_kilogram,
                't': self.gram_to_ton,
                'lbs': self.gram_to_pound,
                'g': self.to_self
            },
            'kg': {
                'g': self.kilogram_to_gram,
                't': self.kilogram_to_ton,
                'lbs': self.kilogram_to_pound,
                'kg': self.to_self
            },
            't': {
                'g': self.ton_to_gram,
                'kg': self.ton_to_kilogram,
                'lbs': self.ton_to_pound,
                'K': self.to_self
            },
            'lbs': {
                'g': self.pound_to_gram,
                'kg': self.pound_to_kilogram,
                't': self.pound_to_ton,
                'lbs': self.to_self
            }
        }

    def gram_to_kilogram(self, g):
        return g / 10**3
    def gram_to_ton(self, g):
        return g / 10**6
    
    def gram_to_pound(self, g):
        return g / 453.592
    
    def kilogram_to_gram(self, kg):
        return kg * 10**3
    
    def kilogram_to_ton(self, kg):
        return kg / 10**3
    
    def kilogram_to_pound(self, kg):
        return kg * 2.20462
    
    def ton_to_gram(self, t):
        return t * 10**6
    
    def ton_to_kilogram(self, t):
        return t * 10**3
    
    def ton_to_pound(self, t):
        return t * 2204.62
    
    def pound_to_gram(self, lbs):
        return lbs * 453.592

    def pound_to_kilogram(self, lbs):
        return lbs / 2.20462
    
    def pound_to_ton(self, lbs):
        return lbs / 2204.62