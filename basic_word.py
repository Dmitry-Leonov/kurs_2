class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def check_word(self, word_user):
        """проверку введенного слова в списке допустимых подслов (вернет bool),"""
        return word_user in self.subwords

    def count_subwords(self):
        """подсчет количества подслов (вернет int)."""
        return len(self.subwords)

    def __repr__(self):
        return f'BasicWord(слово: {self.word}, подслова: {self.subwords}'
