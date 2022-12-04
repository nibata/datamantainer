from ..services.database import db

################################################################################################
# MODELO GROUP (TABLA groups)                                                                  #
################################################################################################
class Group(db.Model):
    __tablename__ = 'groups'
    __table_args__ = {"schema": "authentication"}

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    

    @property
    def serialize(self):
        return {
                    'id': self.id,
                    'code': self.code,
                    'description': self.description
               }
