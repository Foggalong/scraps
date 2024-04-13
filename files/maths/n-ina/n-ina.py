#!/usr/bin/env python3


def create_lists(n, word_list):
    last_verse = word_list.copy()  # will be modified, so make a hard copy
    verse_ends = []
    
    for i in range(1, n+1):
        verse_ends.append(last_verse.copy())

        # process for constructing the new verse
        new_verse = [] 
        while last_verse:
            new_verse.append(last_verse.pop(-1))
            if not last_verse: break  # HACK: handles odd verses
            new_verse.append(last_verse.pop(0))

        # check if we've looped back to the first verse
        if new_verse == word_list:
            # not valid if we've looped back in fewer than n iterations
            if i < n: return []
            # if took exactly n iterations, have a valid set
            else: return verse_ends
        
        # if we haven't, continue to the next verse
        last_verse = new_verse

    # not valid if takes more than n verses to loop
    return []


for n in range(1, 1000):
    word_list = [i for i in range(1,n+1)]
    verses = create_lists(n, word_list)
    if not verses: continue
    print("\nValid {}-ina:".format(n))
    for verse in verses:
        print(" ".join(["{:02d}".format(item) for item in verse]))

