import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData,Table,Column,Integer,String
engine = create_engine('sqlite:///college.db',echo =True)

meta = MetaData()

student = Table(
    'students',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String),
    Column('lastname',String),)
meta.create_all(engine)

ins = student.insert().values(name = 'Sarvesh')

print(ins.compile().params)