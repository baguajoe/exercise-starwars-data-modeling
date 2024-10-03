import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(256), nullable=False)
    favorites=relationship("Favorite", backref="user")
    
    def to_dict(self):
        return {
            "id": self.id, 
            "username": self.username,
            "email": self.email,
            "favorites": [favorite.serialize() for favorite in self.favorites]
        }

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=True)
    height = Column(String(50), nullable=True)
    weight = Column(Integer, nullable=True)
    favorites=relationship("Favorite", backref="character")

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(String(50), nullable=True)
    terrain = Column(String(50), nullable=True)
    climate = Column(String(50), nullable=True)
    favorites=relationship("Favorite", backref="planet")
    
    
class Favorite(Base):
    __tablename__='favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    planet_id = Column(Integer, ForeignKey("planet.id", ondelete="CASCADE"), nullable=True)
    character_id = Column(Integer, ForeignKey("character.id", ondelete="CASCADE"), nullable=True)

    def serialize(self):
        return {
            "type": "character"if self.character else "planet",
            "id": self.character.id if self.character else self.planet.id,
            "name": self.character.name if self.character else self.planet.name 
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
