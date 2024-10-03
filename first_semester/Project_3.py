#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Ajeje the librarian, recently found a hidden room
in the Keras Library (a great place located in
Umkansa, the largest village in the White Mountains).
There, she discovered several books, containing
music scores of ancient Tarahumara songs.
So, she invited over a musician friend to have a look
at them, and he informed her that the scores are
written in Tarahumara notation and need to be translated
into a notation familiar to Umkansanian musicians,
so they can play them back.

Tarahumaras used numbers instead of letters for
writing notes:
0 in place of A, 1 in place of B, and so on, until
7 in place of G. Flat (b) and sharp (#) notes
(see note 3 below, if you do not know what flat
and sharp notes are)
were followed by a - and a +, respectively (for example,
0- meant flat A). Moreover, they just repeated the
same number multiple times to represent the note's
duration. For example, 0000 would mean that the
A note had a length of 4, while 0-0-0-0- would mean
that the A flat note had a length of 4.
Pauses were written down
as spaces; for example, twelve spaces represent
a pause of 12. Both notes and pauses could span
different lines of the score (e.g., starting on line
x and continuing on line x + 1, x + 2, and so on).
Finally, music scores were written from right
to left and from top to bottom, and going to a new
line did not mean anything in terms of the music score.
Umkansanians, instead, are used to write down notes using letters,
and each note is followed by its duration (so, the example
above would be written as A4). Flat and sharp notes are
followed by a b or a #, respectively (for example, A flat
is written as Ab, so the example above would be written ad
Ab4). Pauses are written using the letter P, followed by
their duration, and no spaces are used at all.
Finally, they are used to read music from left
to right on a single row.

As Ajeje knows that you are a skilled programmer, she
provides you with a folder containing the transcription
of all the Tarahumara songs she found, organized in
multiple subfolders and files (one song per file).
Also, she prepared an index file in which each row
contains the title of a Tarahumara song (in quotes),
followed by a space and the path of the file containing
that song (in quotes, relative to the root folder).
She would like to translate all the songs listed in
the index and store them into new files, each one
named with the title of the song it contains (.txt),
in a folder structure matching the original one.
Also, she would like to store in the root folder of
the created structure, a file containing on each row
the title of a song (in quotes) and the corresponding
song length, separated by a space. Songs in the index
need to be ordered in descending length and, if the
length of some songs is the same, in ascending alphabetical
order. The length of a song is the sum of the durations
of all notes and pauses it is made of.

Would you be able to help Ajeje out in translating
the Tarahumara songs into Umkansanian ones?

Note 0: below, you are provided with a function to
Umkansanize the Tarahumara songs; after being executed,
it must return a dictionary in which each key is a song
title and the associated value is the song's duration

Note 1: the songs index file index.txt
is stored in the source_root folder

Note 2: the index of the translated songs
index.txt is in the target_root folder

Note 3: flat and sharp notes are just "altered" versions
of regular notes; for example an F# ("F sharp") is the
altered version of an F, that is, an F note which is a
half of a tone higher than a regular F; the same holds for
flat notes, which are a half of a tone lower than regular notes;
from the point of view of the homework, flat and sharp notes
must be treated the same as regular notes (except for their notation).

Note 4: to create the directory structure you can use the 'os' library functions
(e.g. os.makedirs)


'''

import os

def Umkansanize(source_root:str, target_root:str) -> dict[str,int]:
    #source_root = index.txt
    #target_root = traslated index.txt
    #every song should be tranlated in a file whose name is the name song and it is stored in the exact
    #same path as was the original song. 
    songs_names = []
    songs_paths = []
    duration = []
    with open(source_root + '/index.txt', 'r', encoding='utf-8') as original_index:
        for line in original_index:
           ls = line.split('"')         
           songs_names.append(ls[1])
           songs_paths.append(ls[3])
    
    for i, path in enumerate(songs_paths):
        song_open = open(source_root + '/' + path, 'r', encoding='utf-8')

        s1 = ''
        s = ''
        for line in song_open:
            s = line.replace('0', 'A').replace('1', 'B').replace('2', 'C').replace('3', 'D').replace('4', 'E').replace('5', 'F').replace('6', 'G').replace(' ', 'P').replace('\n', '').replace('-', 'b').replace('+', '#')
            s = s[::-1]
            s1 = s1 + s
            
        d = len(s1) - s1.count('#') - s1.count('b')           
        duration.append(d)
        #have to finish translating here
        translation_f = translation(s1)
        #now create a path with the translation in it
        all_path = path.split('/')
        name = '/' + songs_names[i] + '.txt'
        final_path = '/'.join(all_path[:-1])
        
        os.makedirs(target_root + '/' + final_path, exist_ok=True)
        
        f_translation = open(target_root + '/' + final_path + name, 'w', encoding='utf-8')
        f_translation.write(translation_f)
        f_translation.close()
        all_path = ''
        name = ''
        final_path = ''
        song_open.close()
    
    dict_f = dict(zip(songs_names, duration))
    dict_final = dict(sorted(sorted(dict_f.items(), key=lambda x:x[0]), key=lambda x:x[1], reverse=True))
    
    write_index = open(target_root + '/index.txt', 'w', encoding='utf-8')
    
    for keys in dict_final:
        write_index.write('"' + keys + '"' + ' ' + str(dict_final[keys]) + '\n')
        
    write_index.close()
        
    return dict_final       
                
def translation(str_pre):
    str_p = str_pre.replace('A#', 'h').replace('Ab', 'i').replace('B#', 'j').replace('Bb', 'k').replace('C#', 'l').replace('Cb', 'm').replace('D#', 'n').replace('Db', 'o').replace('E#', 'z').replace('Eb', 'q').replace('F#', 'r').replace('Fb', 's').replace('G#', 't').replace('Gb', 'u')
    translations = ''
    counter = 0
    previous = ''
    for index in range(len(str_p)):
      if index == 0:
        previous = str_p[index]
      if str_p[index] == previous:
        counter += 1
      else:
        translations = translations + previous + str(counter)
        previous = str_p[index]
        counter = 1
    translations = translations + previous + str(counter)
    
    
    str_r = translations.replace('h', 'A#').replace('i', 'Ab').replace('j', 'B#').replace('k', 'Bb').replace('l', 'C#').replace('m', 'Cb').replace('n', 'D#').replace('o', 'Db').replace('z', 'E#').replace('q', 'Eb').replace('r', 'F#').replace('s', 'Fb').replace('t', 'G#').replace('u', 'Gb')
    return str_r       

if __name__ == "__main__":
    Umkansanize("Tarahumara", "Umkansanian")
