from sqlalchemy import insert

class InitialData:

    def __insertCountry(self, table) -> insert: 
        ins = insert(table).values(
            [
                {
                'name': 'United States'
                },
                {
                'name': 'England'
                },
                {
                'name': 'Argentina'
                },
                {
                'name': 'Scotland'
                },    
            ]
        )
        return ins

    def __insertAuthor(self, table):
        ins = insert(table).values(
            [
                {
                'name': 'Edgar Allan Poe',
                'country_id':1
                },
                {
                'name': 'Mark Twain',
                'country_id':1
                },
                {
                'name': 'Arthur Conan Doyle',
                'country_id':4
                },
                {
                'name': 'Jorge Luis Borges',
                'country_id':3
                },    
            ]
        )
        return ins      

    def generateInsertScript(self, table_name, table):
        if table_name in self.__options:
            func = self.__options[table_name]
            script = func(self, table)
            return script

    __options = {
        'country' : __insertCountry,
        'author' : __insertAuthor,
    }