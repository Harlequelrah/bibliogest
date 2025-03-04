from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
)
from bibliogest.settings.database import Base

from sqlalchemy.orm import relationship




class ECRITURE(Base):
    __tablename__ = 'ecritures'
    id = Column(Integer, primary_key=True, index=True)
    auteur_id = Column(Integer , ForeignKey('auteurs.id'))
    livre_id = Column(Integer , ForeignKey('livres.id'))
    auteur = relationship("Auteur", back_populates="auteur_ecritures")
    livre = relationship("Livre", back_populates="livre_ecritures")



metadata= Base.metadata
