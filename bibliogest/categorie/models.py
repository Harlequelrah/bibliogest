from sqlalchemy import (
    Column,
    String,
)
from bibliogest.settings.database import Base

from sqlalchemy.orm import relationship




class Categorie(Base):
    __tablename__ = 'categories'
    code = Column(String(5),index=True,primary_key=True)
    nom = Column(String(30), index=True)
    livres = relationship("Livre", back_populates="categorie")


metadata= Base.metadata
