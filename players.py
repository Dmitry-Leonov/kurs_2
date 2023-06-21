class Player:
    def __init__(self, name_user):
        self.name_user = name_user
        self.word_user = list()

    def count_word_user(self):
        """получение количества использованных слов (возвращает int)"""
        return len(self.word_user)

    def add_word_user(self, word_user):
        """добавление слова в использованные слова (ничего не возвращает)"""
        self.word_user.append(word_user)

    def check_word_back(self, user_word):
        """проверка использования данного слова до этого (возвращает bool)"""
        return user_word in self.word_user

    def __repr__(self):
        return f'BasicWord(слово {self.name_user}, подслова {self.word_user}'
