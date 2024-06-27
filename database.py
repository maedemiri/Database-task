from dataclasses import dataclass
from sqlalchemy import Column , Inteager , String 
from sqlalchemy.ext.declarative import declarative_base

Base= declarative_base()
@dataclass
class User(Base):
    __tablename__= "user"
    id= Column(Inteager,primary_key= True)
    name= Column(String)
    age= Column(Inteager)
    
class Post(User):
    __tablename__= 'post'
    id= Column(Inteager,primary_key= True)
    txt=Column(String)

from sqlalchemy import create_engine
engine= create_engine('sqlite:///test,db')
Base.metadata.create_all(bind=engine)
