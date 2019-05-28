import MySQLdb
import base64
import pandas as pd
import matplotlib.pyplot as plt
from MySQLdb import Error
from io import BytesIO


class DataBase:
    """
    Initialises/closes MySQL database connection.

    """
    def connect_db(self, addr, uname, psswd, dbname):
        """
        Establish DB connection.
        """
        try:
            db = MySQLdb.connect(
                addr,
                uname,
                psswd,
                dbname,
            )
            if db:
                print('Connected to db: \n', db.get_server_info())
                return db

        except Error as e:
            print('Database connection failed:', e)


class DataFrameMaker:

    """
    Sends a query to database,
    reads query-data with pandas method
    builds tables or plots based on received query-data
    """

    def __init__(self, db, query):
        self.db = db
        self.query = query
        self.df = pd.read_sql(self.query, self.db)

    def get_frame(self, html=False):
        """Return whole table dataframe"""
        if html:
            return self.df.to_html()
        return self.df

    def get_nunique_messages(self, html=False):
        """Return dataframe with a number of non-unique messages"""
        if html:
            df = pd.DataFrame(self.df.nunique())
            return df.to_html()
        return self.df.nunique()

    def get_last_messages(self, num, html=False):
        """Return number of last messages"""
        if html:
            return self.df.tail(num).to_html()
        return self.df.tail(num)

    def get_plot(self, html=False):
        """Processes and returns plot image."""
        if html:

            ### stack overflow solution ###
            ### https://stackoverflow.com/questions/17551956/python-given-a-bytesio-buffer-generate-img-tag-in-html ###
            self.df.plot()
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()
            graphic = base64.b64encode(image_png)
            graphic = graphic.decode('utf-8')

            return graphic

        return self.df.plot()


dbase = DataBase()
conn = dbase.connect_db(
    'localhost',
    'testuser',
    'testuser1',
    'test_task'
)


query = """
    SELECT
    *
    FROM device
    """

dm = DataFrameMaker(conn, query)

print(dm.get_nunique_messages(html=True))