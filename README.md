README.MD template:
```
https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#file-readme-template-md
```

# PSQLInterface

Links up MySQL database with pandas. Able to pass its DataFrames to web apps such as Django or Flask).  

## including

* Return whole table dataframe.< /br>
```get_frame()```
* Return dataframe with a number of non-unique messages.< /br>
```get_nunique_messages()```
* Return number of dataframe last messages.< /br>
```get_last_messages()```
* Return dataframe-based plot image.< /br>
```get_plot()```

set ```html=True``` to return web-prepared dataframe.< /br>

Html tag to process dataframe-based plot with Django: < /br>
```<img src="data:image/png;base64,{{ graphic|safe }}">```

## Sample Usage
```
from psqli import DataBase, DataFrameMaker

dbase = DataBase()

conn = dbase.connect_db(
    'localhost',
    'username',
    'userpassword',
    'databasename'
)

query = "SELECT * FROM sample_table"

dm = DataFrameMaker(conn, query)

nunique = dm.get_nunique_messages(html=True)

print(nunique) #  prints dataframe within html tags 
```
