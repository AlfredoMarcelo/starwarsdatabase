import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    email = Column(String(10), nullable=False)
    
    password = Column (Integer)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userId = Column(Integer,ForeignKey('user.id'))

class Libro(Base):
    __tablename__ = 'libros'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userId = Column(Integer,ForeignKey('post.id'))

class Pelicula(Base):
    __tablename__ = 'película'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    fecha_de_estreno = Column(String)
    userId = Column(Integer,ForeignKey('post.id'))

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    especie = Column(String)
    afiliacion = Column(String)
    userId = Column(Integer,ForeignKey('post.id'))

class Serie(Base):
    __tablename__ = 'series'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    fecha_de_estreno = Column(String)
    userId = Column(Integer,ForeignKey('post.id'))

class Comentario(Base):
    __tablename__ = 'Comentarios'
    id = Column(Integer, primary_key=True)
    comentario = (String)
    autor_Id = Column(Integer,ForeignKey('user.id'))
    post_Id = Column(Integer,ForeignKey('post.id'))





    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')