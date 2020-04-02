from models.base_model import BaseModel
import peewee as pw
from models.establishment import Establishment


class Event(BaseModel):
    location = pw.CharField(unique=False)
    date = pw.CharField(unique=False)
    time = pw.CharField(unique=False)
    event_name = pw.CharField(unique=False)
    description = pw.CharField(unique=False)
    date = pw.CharField(unique=False)
    establishment = pw.ForeignKeyField(
        Establishment, backref="events")

    def validate(self):
        return
