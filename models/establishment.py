from models.base_model import BaseModel
import peewee as pw


class Establishment(BaseModel):
    name = pw.CharField(unique=False)
    address = pw.CharField(unique=False)
    hospital_type = pw.CharField(unique=False, null=True)

    def validate(self):
        address_taken = Establishment.get_or_none(
            self.address == Establishment.address)
        if address_taken:
            self.errors.append('Establisment has been registered.')
