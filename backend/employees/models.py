from mongoengine import Document, StringField, EmailField,FileField,DateTimeField
from datetime import datetime
class Employee(Document):
    first_name = StringField(max_length=100)
    last_name = StringField(max_length=100)
    photo = FileField()
    email = EmailField(unique=True)
    designation = StringField(max_length=100)
    mobile_number = StringField(max_length=12, required=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"