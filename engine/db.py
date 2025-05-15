import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,' fc25', 'C:\\Program Files\\EA Games\\EA SPORTS FC 25\\FC25.exe')"
cursor.execute(query)
con.commit()

query = "INSERT INTO sys_command VALUES (null,'photoshop', 'C:\\Program Files\\Adobe\\Adobe Photoshop 2025\\Photoshop.exe')"
cursor.execute(query)
con.commit()

##################################################################################################################################################################################

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'monday', 'https://crc-marketing.monday.com/boards/230994047')"
# cursor.execute(query)
# con.commit()


# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null,'facebook', 'https://www.facebook.com/')"
# cursor.execute(query)
# con.commit()

# 🧹 Remove everything for sys_command (keep one with lowest id)
# cursor.execute("DELETE FROM sys_command;")
# con.commit()


# 🧹 Remove duplicates for web_command(keep one with lowest id)
# delete_duplicates_query = """
# DELETE FROM web_command
# WHERE id NOT IN (
#     SELECT MIN(id)
#     FROM web_command
#     GROUP BY name, url
# );
# """
# cursor.execute(delete_duplicates_query)
# con.commit()
