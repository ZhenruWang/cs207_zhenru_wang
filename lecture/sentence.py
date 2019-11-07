class Sentence: # An iterable
    def __init__(self, text): 
        self.text = text
        self.words = text.split()

    def __iter__(self):
        for word in self.words:
            yield word

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)