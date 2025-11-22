from decimal import Decimal


def get_aliq_ibtp(vServ: Decimal, cNBS: str) -> dict[str, Decimal]:

    # values = requests.get()
    values = {
        "federal_media": Decimal(15.20),  # valor ficticio
        "estadual_media": Decimal(0.00),  # valor ficticio
        "municipal_media": Decimal(3.00),  # valor ficticio
    }
    return values
