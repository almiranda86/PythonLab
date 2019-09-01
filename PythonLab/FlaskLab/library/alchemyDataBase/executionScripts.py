from sqlalchemy import (MetaData, create_engine)
#from createDataBase import (create_database)
from library.alchemyDataBase.createDataBase import (create_database)
#from initialData import InitialData
from library.alchemyDataBase.initialData import InitialData
import pyodbc
from urllib.parse import quote_plus

def execute_scripts():
    parametros = (
    'DRIVER={SQL Server Native Client 11.0};'
    'SERVER=(localdb)\MSSQLLocalDB;'
    'DATABASE=PythonLab;')

    url_db = quote_plus(parametros)

    db_dict = create_database()   
    #engine = create_engine('sqlite:///librady.db')
    engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % url_db)
    metadata = db_dict['metadada']
    metadata.drop_all(engine)
    metadata.create_all(engine)
    connection = engine.connect()

    data = InitialData()

    for table in db_dict['tables']:
        script = data.generateInsertScript(table, db_dict['tables'][table])
        
        if script is not None:
                result = connection.execute(script)