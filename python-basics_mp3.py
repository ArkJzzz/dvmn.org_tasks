#!/usr/bin/python3

import os, sys
from tinytag import TinyTag
from itertools import groupby

path = 'music/'
artist = sys.argv[1]

def get_tags(path, artist):
    all_songs = []
    
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            tag = TinyTag.get(os.path.join(root, filename))
            all_songs.append(tag)

    all_songs = sorted(all_songs, key = lambda album: tag.album)
    
    return all_songs

def filter_songs(all_songs):
	filtered_songs = []

	for song in all_songs:
		if song.artist == artist:
			filtered_songs.append(song)

	return filtered_songs

def print_songs(all_songs):
    for key, group in groupby(all_songs, lambda track: track.album):
        print('{album}:\n'.format(album = key)) 
        for song in group:
            print('Название: {title} \nАльбом: {album} \nИсполнитель: {artist}\n'.format(title=song.title, album=song.album, artist=song.artist))

def main():
    songs = get_tags(path, artist)
    filtered_songs = filter_songs(songs)
    print_songs(filtered_songs)

if __name__ == '__main__':
    main()
