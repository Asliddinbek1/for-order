import sqlite3
import settings

# Create database
connection = sqlite3.connect(settings.db_path)


# Create table in database
cursor = connection.cursor()


# cursor.execute(
#     """
#         CREATE TABLE User(
#             id  not null primary key autoincrement,
#             name char(30) not null,
#             contact int not null
            
#         )
#     """   
# )



connection.commit()
connection.close()