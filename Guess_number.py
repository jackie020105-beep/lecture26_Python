# 1.컴퓨터가 숫자를 생각한다 (1~50)
# 2.사용자가 숫자를 말한다
# 3.숫자가 맞으면 사용자 Win
# 4.숫자가 맞으면 사용자 WindowsError틀리면 컴퓨터가 up, down을 알려준다
# 5.2~4번까지 7번 반복
# 6.7번 내에 맞추지 못하면 computer win

import random
limit = 100
tr = 8

def guess_number():
    number = random.randint(1, limit+1)
    print(f"숫자를 맞춰보세요! (1-{limit})")

    for i in range(1, tr+1):
        try:
            guess = int(input("숫자를 입력하세요: "))

            if guess < number:
                print("더 큰 숫자입니다.")
                
            elif guess > number:
                print("더 작은 숫자입니다.")
            else:
                print("축하합니다! " + str(i) + "번 만에 숫자를 맞췄습니다!")
                break
            if i == tr:
                print("(Computer-Win)아쉽지만, 정답은 " + str(number) + "였습니다.")
                break
        except ValueError:
            print("유효한 숫자를 입력해주세요.")

guess_number()