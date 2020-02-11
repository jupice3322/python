# price.py
def info():
    name = input("이름: ")
    relate = input("관계: ")
    print("같이 볼 사람 이름은", name + "이고 관계는", relate + "이다.")


def pay():
    price = 10000
    people = int(input("인원수 입력: "))
    sum = price * people
    print("지불할 금액은", str(sum) + "원 입니다.")

# 컨트롤 + 쉬프트 +f(자동포맷팅, 코드 자동 정리)
