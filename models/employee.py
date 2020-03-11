from models.base_model import BaseModel
import peewee as pw
from werkzeug.security import generate_password_hash


class Employee(BaseModel):
    email = pw.CharField(unique=True)
    username = pw.CharField(unique=True)
    password = pw.CharField(unique=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def validate(self):
        #     email_taken = Employee.get_or_none(self.email == Employee.email)
        #     if email_taken:
        #         self.errors.append('Email already taken.')

        #     username_taken = Employee.get_or_none(
        #         self.username == Employee.username)
        #     if username_taken:
        #         self.errors.append('Username already taken')

        #     if not self.id and(len(self.password) < 6 or len(self.password) > 13):
        #         self.errors.append('Password must be between 6-13')
        #     else:
        #         if not self.id:
        #             self.password = generate_password_hash(self.password)

        return True

#    existing_username = Employee.get_or_none(
#             Employee.username == self.username)
#         if existing.username and not existing_username.id == self.id:
#             self.errors.append('Username already taken')

#         existing_email = Employee.get_or_none(Employee.email == self.email)
#         if existing.email and not existing_email.id == self.id:
#             self.errors.append('Email already taken')
