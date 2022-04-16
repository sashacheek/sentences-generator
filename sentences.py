'''
Week 6 Assignment Sentences
Prints randomly contructed sentences from a series of words
May 29 2021
'''
import random


def main():
    tenses = ['past', 'present', 'future']
    for sentence in range(0, 5):
        quantity = random.randint(1, 2)
        tense = random.choice(tenses)
        determiner = get_determiner(quantity).capitalize()
        adjective = get_adjective()
        noun = get_noun(quantity)
        verb = get_verb(quantity, tense)
        quantity = random.randint(1, 2)
        prepositional_phrase = get_prepositional_phrase(quantity)
        print(f'{determiner} {adjective} {noun} {verb} {prepositional_phrase}.')


def get_determiner(quantity):
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    word = random.choice(words)
    return word


def get_adjective():
    words = ['important', 'annoying', 'unique', 'sad', 'outstanding',
             'tall', 'likeable', 'unkempt', 'loyal', 'clumsy']
    word = random.choice(words)
    return word


def get_noun(quantity):
    if quantity == 1:
        words = ['adult', 'bird', 'boy', 'car', 'cat',
                 'child', 'dog', 'girl', 'man', 'woman']
    else:
        words = ["adults", "birds", "boys", "cars", "cats",
                 "children", "dogs", "girls", "men", "women"]

    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    if tense.lower() == 'past':
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    if tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]

    word = random.choice(words)
    return word


def get_preposition():
    words = ["about", "above", "across", "after", "along",
             "around", "at", "before", "behind", "below",
             "beyond", "by", "despite", "except", "for",
             "from", "in", "into", "near", "of",
             "off", "on", "onto", "out", "over",
             "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = f'{preposition} {determiner} {noun}'
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    return prepositional_phrase


main()
