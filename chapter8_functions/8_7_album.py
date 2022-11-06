

def make_album(artist, title, songs=None):
    print(songs)
    album = {'artist': artist.title(), 'title': title.title()}
    if songs:
        album['songs'] = songs
    return album
    
irvin = make_album('Irvin Goodman', 'Valtiovalta')
eminem = make_album('eminem', 'marshall mathers', 20)
me = make_album('sampsa', 'no album')

def print_data(artist):
    if 'songs' in artist:
        print(f"\tArtist: {artist['artist']} \n\tAlbum name: {artist['title']} \n\tSongs: {artist['songs']} \n")
    else: 
        print(f"\tArtist: {artist['artist']} \n\tAlbum name: {artist['title']} \n")

print_data(irvin)
print_data(eminem)
print_data(me)
