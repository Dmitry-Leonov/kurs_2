from players import Player
from utils import load_random_word

def main():
    url_words = 'https://api.npoint.io/7a5d4b0c8663b9c35810'
    basic_word = load_random_word(url_words)
    user_name = input("Введите имя игрока: ")
    user = Player(user_name)
    print(f'Привет {user.name_user}')
    print(f'Составьте {basic_word.count_subwords()} слов из слова {basic_word.word.upper()}')
    print("Слова должны быть не короче 3 букв\n"
          "Чтобы закончить игру, угадайте все слова или напишите 'stop' или 'стоп'\n"
          "Поехали, ваше первое слово?")
    while basic_word.count_subwords() != user.count_word_user():
        word = input().lower().strip()
        if word in ('stop', 'стоп'):
            break
        elif len(word) < 3:
            print("слишком короткое слово")
        elif not basic_word.check_word(word):
            print("неверно")
        elif user.check_word_back(word):
            print("уже использовано")
        else:
            user.add_word_user(word)
            print(f"верно, угадал: {user.count_word_user()} слов из {basic_word.count_subwords()}")
    print(f"Игра завершена, вы угадали {user.count_word_user()} слов")


if __name__ == '__main__':
    main()
