"""Isle of Man Airport (IOM) destinations — April 2026."""

DESTINATIONS = {
    "IOM": {
        "name": "Isle of Man",
        "routes": {
            "AGP": "Malaga",
            "BHX": "Birmingham",
            "BRS": "Bristol",
            "DUB": "Dublin",
            "EDI": "Edinburgh",
            "FAO": "Faro",
            "IBZ": "Ibiza",
            "LCY": "London City",
            "LGW": "London Gatwick",
            "LHR": "London Heathrow",
            "LPL": "Liverpool",
            "LTN": "London Luton",
            "MAN": "Manchester",
            "NQY": "Newquay",
            "PMI": "Palma",
            "SOU": "Southampton",
            "TFS": "Tenerife South",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
