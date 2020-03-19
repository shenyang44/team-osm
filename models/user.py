from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    name = pw.CharField(unique=False)
    password = pw.CharField(unique=False)
    email = pw.CharField(unique=True)
    address = pw.TextField(unique=False, null=True)
    number = pw.IntegerField(unique=True)
    blood_group = pw.CharField(unique=False, null=True)

    def validate(self):
        email_taken = User.get_or_none(self.email == User.email)
        if email_taken:
            self.errors.append('That email is taken.')

        number_taken = User.get_or_none(User.number == self.number)
        if number_taken:
            self.errors.append('Number taken, yo')
