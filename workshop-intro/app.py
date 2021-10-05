from chalice import Chalice
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
import json
import form, requests
from chalice import CORSConfig
import urllib 
from urllib.request import urlopen

app = Chalice(app_name='workshop-intro')

  
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/adapa_website')

Base = declarative_base()


class User(Base):
        __tablename__='users'
        id = Column(Integer(), primary_key=True)
        name=Column(String(30), nullable=True, unique=True)
        email=Column(String(70), nullable=True, unique=True)
        phone =Column(String(30), nullable=True, unique=True)
        message=Column(String(50), nullable=True, unique=True)

        def __str__(self):
              return self.username 
Session = sessionmaker(engine)

session = Session()

if __name__ == '__main__':
	pass



@app.route('/movi',methods=['GET', 'PUT'])
def create_engine():
    url = 'http://localhost:3005/api/movies'
    res = requests.get(url)
    data = res.json()
    for json in data:
      nombre=json['nombre']
      emil=json['email']
      numero=json['numero']
      user1=User(name=nombre, email=emil, phone='25897641678', message='te amo me')
      session.add(user1)
      session.commit()
      return 'add'
    	
@app.route('/database',methods=['GET', 'PUT'])
def database():    	
    #request = app.current_request
    #if request.method == 'POST':
    #user1=User(name=nombre, email=emil, phone='6422547896', message='he')
    #session.add(user1)
    #session.commit()
    return 'add'



