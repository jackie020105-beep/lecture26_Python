from hangman_logic import Hangman
# import hangman_logic as hm



def load_word_list():
    filename = './voca.txt'
    with open(filename, 'r', encoding='utf-8') as f_read:
        word_list = f_read.read().splitlines()
    return word_list

print()
print('========== Hangman ============')

# 단어 선택

word_list = load_word_list()
hangman = Hangman(word_list)

print(f'{hangman.display_word} ({len(hangman.word)}글자)')

while True:
    # 알파벳 입력
    letter = input('>> 알파벳 입력 : ')

    # 정답 확인
    result = hangman.check_letter(letter)
    if result == Hangman.RIGHT:
        print(f'정답 : {hangman.display_word}')
    elif result == Hangman.WRONG:
        print(f'오답 : {hangman.num_try}회 시도')
    else:
        print(hangman.error_status)
        continue

    # 승패 확인
    result = hangman.is_win()
    if result == Hangman.WIN:
        print(f'You win ~~~~ !!! : {hangman.num_try}회 시도')
        break
    elif result == Hangman.LOOSE:
        print(f'You loose ~~~~ !!! : {hangman.word}')
        break