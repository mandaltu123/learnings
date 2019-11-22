def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words"""
    return sorted(words)


def print_first_word(words):
    """Prints the first words after popping it off"""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the words in a sorted manner"""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and the last word of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words and then prints the first and the last from the sorted words"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# Here how it looks like when we import this as a python module of python shell and execute the program :
#
# hisenberg@cerebro:~/work/learnings/python-learning/brushup/string-bytes-character-encodings$ python3
# Python 3.7.5rc1 (default, Oct  8 2019, 16:47:45)
# [GCC 9.2.1 20191008] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import even_more_practice
# >>> sentence = "all good things come to those who wait."
# >>> words = even_more_practice.break_words(sentence)
# >>> words
# ['all', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words=even_more_practice.sort_words(words)
# >>> sorted_words
# ['all', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> even_more_practice.print_first_word(sorted_words)
# all
# >>> even_more_practice.print_last_word(sorted_words)
# who
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = even_more_practice.sort_sentence(sentence)
# >>> sorted_words
# ['all', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> even_more_practice.print_first_and_last(sentence)
# all
# wait.
# >>> even_more_practice.print_first_and_last_sorted(sentence)
# all
# who
# >>>
