import requests, random

from basic_word import BasicWord


def load_random_word(url):
    """- получит список слов с внешнего ресурса, выберет случайное слово,
        создаст экземпляр класса `BasicWord`, вернет этот экземпляр."""
    resp = requests.get(url)
    random_word = random.choice(resp.json())
    word_basicword = BasicWord(random_word['word'], random_word['subwords'])
    return word_basicword
