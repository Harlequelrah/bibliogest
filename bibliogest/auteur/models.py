from sqlalchemy import (
    Column,
    Integer,
    String,
)
from bibliogest.settings.database import Base

from sqlalchemy.orm import relationship

class Auteur(Base):
    __tablename__ = 'auteurs'
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), index=True)
    prenom = Column(String(50), index=True)
    auteur_ecritures = relationship("Ecriture", back_populates="auteur")








metadata= Base.metadata
