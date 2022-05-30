from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing instructions from chinook database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create class based model for Artist
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create class based model for Album
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# create class based model for Track
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting directly to the database, will adk for a session
# create new instance of sessionmaker, pointing to our db
Session = sessionmaker(db)
# opens actual session
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# Query 1
# artists = session.query(Artist)
# for artist in artists:
#    print(artist.ArtistId, artist.Name, sep=" || ")

# Query 2
# artists = session.query(Artist)
# for artist in artists:
#    print(artist.Name)

# Query 3
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#    print(album.AlbumId, album.Title, album.ArtistId, sep=" || ")

# Query 6
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(track.TrackId, track.Name, track.AlbumId, track.MediaTypeId, track.GenreId, track.Composer, track.Milliseconds, track.Bytes, track.UnitPrice, sep=" | ")
