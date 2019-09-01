from sqlalchemy import (MetaData, Table, Column, Integer, String,
                        ForeignKey, create_engine)
 

def create_database():

    metadata = MetaData()

    country = Table('country', metadata,
    Column('id', Integer(), primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False)
    )

    author  = Table('author', metadata,
    Column('id', Integer(), primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False),
    Column('country_id', ForeignKey('country.id'))
    )

    book = Table('book', metadata,
    Column('id', Integer(), primary_key=True, autoincrement=True),
    Column('title', String(255), nullable=False),
    Column('isbn', String(50)),
    Column('author_id', ForeignKey('author.id'))
    )

    db_dict = {
        'metadada': metadata,
        'tables':{
            'country': country,
            'author': author,
            'book': book
        }
    }

    return db_dict