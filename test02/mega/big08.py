#커피값 입력 및 변수 설정(정수)
pay=int(input("커피값 입력: "))
#커피 인원 수 입력 및 변수 설정(정수)
people=int(input("커피 인원수: "))
#계산 결과 변수 설정
result=pay*people
#조건문 계산 결과가 20000원 이상일 경우 아래 내용 전시
if result >= 20000:
    print("2000원을 할인해드립니다.")
    print(result-2000)
#조건문 계산 결과가 20000원 이하일 경우 아래 내용 전시
else:
    print("계산값을 다 지불하셔야합니다.")
    print(result)