import psycopg2

# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the Artist table
# cursor.execute('SELECT * FROM "Artist"')

# query 2 - names from Artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - QUeen from Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# query 4 - ArtistId 51
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# query 5 - Albums for artist 51
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# query 6 - songs by artist
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["AC/DC"])

# fetch the results (multiple)
results = cursor.fetchall()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
