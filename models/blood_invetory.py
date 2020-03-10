from models.base_model import BaseModel
import peewee as pw
from models.establishment import Establishment


class Blood_Inventory(BaseModel):
    blood_type = pw.CharField(unique=False)
    quantity = pw.CharField(unique=False)
    establishment = pw.ForeignKeyField(
        Establishment, backref="blood_inventory")

    def validate(self):
        return
