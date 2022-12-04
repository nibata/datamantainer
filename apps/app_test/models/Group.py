from typing import Dict
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
    

    def __repr__(self) -> str:
        return f"<Group {self.code}>"


    @property
    def serialize(self) -> Dict:
        """Objeto group serializado como dict

        Returns
        -------
        Dict
            Representacion en diccionario del objeto
        """
        return {
                    'id': self.id,
                    'code': self.code,
                    'description': self.description
               }
