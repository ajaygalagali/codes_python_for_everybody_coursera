import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('mytrack.sqlite')
c = conn.cursor()
c.executescript('''

DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER

);
''')
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None
# fhand = open("Library.xml")
xmlStuff = ET.parse("Library.xml")
xmlContent = xmlStuff.find('dict/dict')

for entry in xmlContent:
    if ( lookup(entry, 'Track ID') is None ) : continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry,'Genre')
    # length = lookup(entry,'Length')
    # rating = lookup(entry,'Rating')
    if name is None or artist is None or album is None or genre is None :
        continue
    print("Name   :",name)
    print("Artist :",artist)
    print("Album  :",album)
    print("Genre  :",genre)
    print()
    c.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES ( ? )''', (artist,))
    c.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = c.fetchone()[0]

    c.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES ( ?, ? )''', (album, artist_id))
    c.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = c.fetchone()[0]

    c.execute('''INSERT OR IGNORE INTO Genre (name) 
            VALUES ( ?)''', (genre,))
    c.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = c.fetchone()[0]

    c.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id) 
            VALUES ( ?, ?, ?)''',
                (name, album_id, genre_id))

    conn.commit()