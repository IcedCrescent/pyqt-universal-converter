from converters.base_conveter import BaseConverter


class DataConverter(BaseConverter):
    def __init__(self):
        super().__init__()

        self.conversion_rates = {
            'B': {  # Bytes
                'KB': lambda b: b / 1024,
                'MB': lambda b: b / (1024 * 1024),
                'TB': lambda b: b / (1024 * 1024 * 1024),
                'B': self.to_self
            },
            'KB': {  # Kilobytes
                'B': lambda kb: kb * 1024,
                'MB': lambda kb: kb / 1024,
                'TB': lambda kb: kb / (1024 * 1024),
                'KG': self.to_self
            },
            'MB': {  # Megabytes
                'B': lambda mb: mb * (1024 * 1024),
                'KB': lambda mb: mb * 1024,
                'TB': lambda mb: mb / 1024,
                'MB': self.to_self
            },
            'TB': {  # Terabytes
                'B': lambda tb: tb * (1024 * 1024 * 1024),
                'KB': lambda tb: tb * (1024 * 1024),
                'MB': lambda tb: tb * 1024,
                'TB': self.to_self
            }
        }
        self.conversion_rates = {
            'B': {  # Bytes
                'KB': lambda b: b / (1024**1),
                'MB': lambda b: b / (1024**2),
                'GB': lambda b: b / (1024**3),
                'TB': lambda b: b / (1024**4),
                'B': self.to_self
            },
            'KB': {  # Kilobytes
                'B': lambda kb: kb * (1024**1),
                'MB': lambda kb: kb / (1024**1),
                'GB': lambda kb: kb / (1024**2),
                'TB': lambda kb: kb / (1024**3),
                'KG': self.to_self
            },
            'MB': {  # Megabytes
                'B': lambda mb: mb * (1024**2),
                'KB': lambda mb: mb * (1024**1),
                'GB': lambda mb: mb / (1024**1),
                'TB': lambda mb: mb / (1024**2),
                'MB': self.to_self
            },
            'GB': {  # Gigabytes
                'B': lambda gb: gb * (1024**3),
                'KB': lambda gb: gb * (1024**2),
                'MB': lambda gb: gb * (1024**1),
                'TB': lambda gb: gb / (1024**1),
                'GB': self.to_self
            },
            'TB': {  # Terabytes
                'B': lambda tb: tb * (1024**4),
                'KB': lambda tb: tb * (1024**3),
                'MB': lambda tb: tb * (1024**2),
                'GB': lambda tb: tb * (1024**1),
                'TB': self.to_self
            },
        }
