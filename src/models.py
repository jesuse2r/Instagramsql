import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(30), nullable=False)
    email= Column(String(30), nullable = False)
    profile_picture= Column(String(100), nullable = True)
    bio = Column(String(250), nullable=True)
    gender= Column(String(15), nullable= False) 

class Post(Base):
    __tablename__= "post"
    id = Column(Integer, primary_key=True)
    img_post= Column(String(100), nullable = False)
    description=Column(String(100), nullable = True )
    date= Column(DateTime, nullable= False)
    user_id= Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

class Commentary(Base):
    __tablename__= "commentary"
    id = Column(Integer, primary_key=True)
    text= Column(String(250), nullable=False)
    date=Column(DateTime, nullable=False)
    user_id= Column(Integer, ForeignKey('user.id'))
    user= relationship(User)
    post_id=Column(String, ForeignKey('post.id'))
    post= relationship(Post)




    


class Preference(Base):
    
    __tablename__= "preference"
    id= Column(Integer, primary_key=True)
    is_private= Column(Boolean)
    is_dark= Column(Boolean, default = True)
    profile_picture=Column(String(100), nullable=True)
    bio= Column(String(250), nullable=True)
   
    user_id= Column(Integer, ForeignKey("user.id"))
    user = relationship(User)
  

class Favorite(Base):
    __tablename__= "Favorite"
   
    id= Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable= True)
    user= relationship(User)
    preference_id = Column(Integer, ForeignKey('preference.id'), nullable= True)
    preference= relationship(Preference)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
   
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
