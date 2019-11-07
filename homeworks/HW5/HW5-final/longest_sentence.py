from linked_list import Nil

def get_list_of_sentences(chapter1='swansway-chapter1.txt'):
    def to_sentences(p):
            for delimiter in '.?!': p = p.replace(delimiter, '|')
            return [s.strip('\" ') for s in p.split('|')]
    with open(chapter1, 'r', encoding='UTF-8') as f:
        paragraphs = f.readlines()

    sentences = [s for p in paragraphs for s in to_sentences(p) if len(s) > 1]
    list_of_sentences = Nil()
    for s in sentences[::-1]:
        list_of_sentences = list_of_sentences.prepend(s)
    return list_of_sentences


def longest_sentence():
    # returns the number of words in the longest sentence
    list_of_sentences = get_list_of_sentences()
    
    num_list = list_of_sentences.for_each(num_of_words)
    return num_list.reduce_right(larger)
    
    
def num_of_words(sentence):
    assert type(sentence) == str, Exception(f'Not a string')
    return len(sentence.split())

def larger(a, b):
    return a if a > b else b
