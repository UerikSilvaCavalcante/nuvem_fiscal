import os
import sys

sys.path.insert(0, os.path.abspath(".."))

from django.test import TestCase
import json
from nfse.enums import nfse_enums
from decimal import Decimal

# Create your tests here.


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj): # type: ignore
        if isinstance(obj, Decimal):
            return str(obj)  # Mantém precisão exata
        return super().default(obj)


payload = {
    "ambiente": nfse_enums.AMBIENTE.HOMO,
    "provedor": nfse_enums.PROVEDOR.PRADAO,
    "valor": Decimal("10.00"),
}

print(json.dumps(payload, cls=DecimalEncoder))
