def make_album(artist, title):
    album = {'artist': artist.title(), 'title': title.title()}
    return album


while True:
    artist = input('\tName artist: ')
    title = input('\tName title: ')
    new_album = make_album(artist, title)
    break

print(f"\tAlbum title: {new_album['title']} \n\tArtist: {new_album['artist']}")
