from services.database import db
from wtforms_alchemy import ModelForm


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {"schema": "test_schema"}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, info={"label": "Name"})
    age = db.Column(db.Integer, info={"label": "Age"})
    address = db.Column(db.String(120), info={"label": "Address"})
    last_name = db.Column(db.String, info={"label": "Last Name"})

    @property
    def serialize(self):
        return {
                    "id": self.id,
                    "name": self.name,
                    "age": self.age,
                    "address": self.address,
                    "last_name": self.last_name
               }



class UserForm(ModelForm):
    class Meta:
        model = User
        field_args = {
            "name": {"render_kw": {"class": "form-control",
                                   "placeholder":"First name"}},
            "address": {"render_kw": {"class": "form-control",
                                      "placeholder": "Address"}},
            "age": {"render_kw": {"class": "form-control"}},
            "last_name": {"render_kw": {"class": "form-control",
                                        "placeholder": "Last Name"}}}
