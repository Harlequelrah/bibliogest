from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
)
from bibliogest.settings.database import Base
from sqlalchemy.orm import relationship

class Livre(Base):
    __tablename__ = 'livres'
    id = Column(Integer, primary_key=True,index=True)
    titre = Column(String(30), index=True)
    contenue = Column(Text)
    nbr_pages = Column(Integer)
    code_cat = Column(String(5), ForeignKey('categories.code'))
    categorie = relationship("Categoriz", back_populates="livres")
    livres_ecritures = relationship("Ecriture", back_populates="livre")



metadata= Base.metadata
