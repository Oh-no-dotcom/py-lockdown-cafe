import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                "Alarm! One of client is not vaccinated!"
            )

        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError(
                "Dangerous! One of client out of the day vaccination!"
            )

        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError(
                "Attention! One of client is not wearing mask!"
            )

        return f"Welcome to {self.name}"
