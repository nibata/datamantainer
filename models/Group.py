from services.database import db


class Group(db.Model):
    __tablename__ = 'groups'
    __table_args__ = {"schema": "test_schema"}

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)
    description = db.Column(db.String)

    @property
    def serialize(self):
        return {
                    'id': self.id,
                    'code': self.code,
                    'description': self.description
               }
