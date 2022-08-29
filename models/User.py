from services.database import db


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {"schema": "test_schema"}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.String(120))
    address = db.Column(db.String(120))
    last_name = db.Column(db.String)

    @property
    def serialize(self):
        return {
                    'id': self.id,
                    'name': self.name,
                    'city': self.city,
                    'state': self.state,
                    'address': self.address,
                    'last_name': self.last_name
               }
