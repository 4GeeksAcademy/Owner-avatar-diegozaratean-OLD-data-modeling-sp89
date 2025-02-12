import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()





class Director(Base):
    __tablename__ = 'director'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    nacionalidad = Column(String(250), nullable=False)
    numero_peliculas = Column(Integer, nullable=False)
    
class Pelicula(Base):
    __tablename__ = 'pelicula'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    titulo = Column(String(250), nullable=False)
    duracion = Column(Integer, nullable=False)
    genero = Column(String(250), nullable=False)
    costo_produccion = Column(Integer, nullable=False)
    director_id = Column(Integer, ForeignKey('director.id'))
    director = relationship(Director)


class Actor(Base):
    __tablename__ = 'actor'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    nacionalidad = Column(String(250), nullable=False)


class PeliculaActor(Base):
    __tablename__ = 'pelicula_actor'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    pelicula_id = Column(Integer, ForeignKey('pelicula.id'))
    pelicula = relationship(Pelicula)
    actor_id = Column(Integer, ForeignKey('actor.id'))
    actor = relationship(Actor)


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
