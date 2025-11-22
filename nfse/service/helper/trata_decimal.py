import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj): # type: ignore
        if isinstance(obj, Decimal):
            return str(obj)  # Mantém precisão exata
        return super().default(obj)