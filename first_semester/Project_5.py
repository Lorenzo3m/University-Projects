#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Your dear friend Pico de Paperis sent you a very strange message scribbled on a postcard.
You haven't seen him in a long time and you've always had fun writing to each other in code.
To decode his message, go and look for a rather particular book in your library,
the Archimedes Pythagorean cipher. The cipher to be applied is the famous "Pharaoh's Cipher".
The decipherment with the Pharaoh's method is based on rules for substituting sequences of symbols in the text.
The reason why it is called "Pharaoh's cipher" is that in ancient Egyptian sequences made up of multiple hieroglyphs
could be written in any order, so any anagram of the sequences was valid.
To make things stranger, Pico de Paperis decided to use a cipher that is not exactly the one of Pharaoh,
but a variant of it. Instead of using anagrams he uses "quasi-anagrams", that is, anagrams that in the original text
have one more spurious character than the searched sequence.
The cipher contains pairs of sequences that indicate how to transform the text.
For example, the pair 'shampoo' -> 'soap' corresponds to searching for a point in the message where the sequence
'shampoo' appears (or an anagram of it) but with an extra character (e.g. 'pmQohaso')
and replace it with the sequence 'soap'.
Decoding the message can lead to more possible final messages, because there can be more sequences in the text
that can be transformed at any time and the order of transformations influences subsequent transformations.
At some point it will happen that none of the "quasi-anagrams" of a cipher sequence is present anywhere
in the sequence of symbols, and therefore it is no longer possible to make transformations.
We call these sequences final sequences.
Of all the possible final sequences, the one we are interested are all the shortest.

To decode the Pico de Paperis message you must implement the function
pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
which receives as arguments:
- the text that Pico de Paperis sent you, as a string of symbols (characters)
- the cipher to be applied, a dictionary whose keys are the sequences to search for a quasi-anagram in the text
    and as the associated value the string to replace the quasi-anagram found with.
The function must return the set of the shortest texts obtainable by repeatedly applying
the transformations until it is no longer possible to apply any of them.

Example:
encrypted_text  = 'astronaut-flying-cyrcus'
pharaohs_cypher = {'tuar': 'me', 'cniy': 'op', 'sorta': 'tur', 'fult': 'at', 'rycg': 'nc'}

Result: {'tmeopcus', 'metopcus', 'ameopcus', 'atmepcus'}
Notice, and all the transformations applied are those contained in the example.txt file
(in alphabetical order and without repetitions)

NOTE: At least one of the functions or methods you implement must be recursive
NOTE: the recursive function/method must be defined at the outermost level
      otherwise you will fail the recursion test.
'''


def pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
    #for every anagram i check for the pharaos and return the smallests
    # add here your code

    s = set()
    l = []
    
    li = combinations(encrypted_text, pharaohs_cypher, l)
    #return l, len(l)
    for e in li:
        s.add(e)
        
    
    g = sorted(s, key=sort)
    size = len(g[0])
    
    final_set = set()
    for e in g:
        if len(e) == size:
            final_set.add(e)
            
            
    return final_set
    
def sort(x):
    return len(x)

def combinations(text, cypher, l):
    l.append(text)
    
    for k, v in cypher.items():
        d = ''

        for i in range(len(text)):
            d += text[i]
            
            if len(d) - 1 == len(k) and is_half_anagram(k, d):
                st = text.replace(d, v)
                s1 = combinations(st, cypher, l)

            
            if len(d) > len(k):
                d = d[1:]
    return l
            
            
def is_half_anagram(str1, str2):
    str11 = sorted(str1)
    str22 = sorted(str2)
    if len(str2) - len(str1) > 1 or len(str2) - len(str1) < 0:
        return False
    
    if len(str11) == 0 and len(str22) == 1:
        return True
    
    if not str1 and not str2:
        return True
    
    if str11[0] == str22[0]:
        return is_half_anagram(str11[1:], str22[1:])
    
    if str11[0] != str22[0]:
        return is_half_anagram(str11, str22[1:])
    


if __name__ == '__main__':
    print(pharaohs_revenge('astronaut-flying-cyrcus', {'tuar': 'me', 'cniy': 'op', 'sorta': 'tur', 'fult': 'at', 'rycg': 'nc'}))
    # place here your own tests
