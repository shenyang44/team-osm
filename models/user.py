from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    name = pw.CharField(unique=False)
    password = pw.CharField(unique=False)
    email = pw.CharField(unique=True)
    address = pw.TextField(unique=False, null=True)
    blood_group = pw.CharField(unique=False, null=True)

    def validate(self):
        email_taken = User.get_or_none(self.email == User.email)
        if email_taken:
            self.errors.append('That email is taken.')

        if self.blood_group not in ['A pos.', 'B pos.', 'O pos.', 'AB pos.', 'A neg.', 'B neg.', 'O neg.', 'AB neg.']:
            self.errors.append(
                'Blood group only accepts this format (A neg. | O pos.)')
