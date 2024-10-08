def single_root_words(root_word, *other_words):
    same_words = []
    # low_other_words = other_words.lower()
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
    print(same_words)

single_root_words('rIch', "RiCh", 'richyT', 'doog')


