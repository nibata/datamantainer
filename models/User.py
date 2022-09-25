from services.database import db
from wtforms_alchemy import ModelForm


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {"schema": "test_schema"}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, info={"label": "Name"}, nullable=False)
    age = db.Column(db.Integer, info={"label": "Age"})
    address = db.Column(db.String(120), info={"label": "Address"})
    last_name = db.Column(db.String, info={"label": "Last Name"}, nullable=False)

    @property
    def serialize(self):
        return {
                    "id": self.id,
                    "name": self.name,
                    "age": self.age,
                    "address": self.address,
                    "last_name": self.last_name
               }

    @staticmethod
    def get_searchable_fields():
        return (User.name,
                User.last_name,
                User.age)


    @staticmethod
    def get_sortable_fields():
        return ("name", 
                "age", 
                "last_name")


class UserForm(ModelForm):
    class Meta:
        model = User
        
