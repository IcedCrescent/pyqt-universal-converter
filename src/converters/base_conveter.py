class BaseConverter:
    def __init__(self) -> None:
        self.conversion_rates = {}

    def convert(self, value, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.conversion_rates or to_unit not in self.conversion_rates[from_unit]:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

        conversion_func = self.conversion_rates[from_unit][to_unit]
        return conversion_func(value)
    
    def to_self(self, value):
        return value