from sqlite3 import connect

connection = connect('movies.db')
cursor = connection.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS movies(id INT, name TEXT, imdb FLOAT)")
    connection.commit()


def insert_data(id, name, imdb):
    cursor.execute("INSERT INTO movies VALUES(?, ?, ?)", (id, name, imdb))
    connection.commit()


def get_all_movies():
    cursor.execute("SELECT * FROM movies")
    for row in cursor:
        print(row)


def update_imdb(name, new_imdb):
    cursor.execute("UPDATE movies SET imdb = ? WHERE name = ?", (new_imdb, name))
    connection.commit()


def delete_data(name):
    cursor.execute("DELETE FROM movies WHERE name = ?", (name,))


create_table()

insert_data(1, 'The Dark Knight', 9.0)
insert_data(2, 'Pulp Fiction', 8.9)
insert_data(3, 'Fight Club', 8.8)
insert_data(4, 'Forrest Gump', 8.8)
insert_data(5, 'The Shawshank Redemption', 9.3)
insert_data(6, 'Interstellar', 8.6)
insert_data(7, 'The Prestige', 8.5)
insert_data(8, 'Gladiator', 8.3)
insert_data(9, 'Saving Private Ryan', 8.6)
insert_data(10, 'The Silence of the Lambs', 8.6)
insert_data(11, 'The Usual Suspects', 8.5)
insert_data(12, 'Schindler\'s List', 8.9)
insert_data(13, 'Whiplash', 8.5)

update_imdb('Gladiator', 8.5)
delete_data('Saving Private Ryan')

get_all_movies()

cursor.close()
connection.close()