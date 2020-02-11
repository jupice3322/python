#1
money=int(input("1년 만기 정기 예금을 얼마나 예치하시겠습니까?: "))
iza=int(money/10)
print("원금이",str(money)+"원 이시군요.!")
print("이자는",str(iza)+"원 입니다.")
print("원리합계는",str(money+iza)+"원 입니다.")

#2
english=int(input("영어 점수 입력: "))
math=int(input("수학 점수 입력: "))
korea=int(input("국어 점수 입력: "))
sum=english+math+korea
ave=int(sum/3)
print("----------------------------------")
print("세 과목의 합은",str(sum)+"점")
print("세 과목의 평균은",str(ave)+"점")

#3
time=int(input("지금은 몇 시 입니까?(1-24): "))
if time<12:
    print("점심 전입니다. 맛있게 드세요.!")
else:
    print("점심 후입니다.")

#4
id=input("로그인 할 id를 입력: ")

if id == "root":
    print("로그인 되었습니다.")
else:
    print("로그인 되지 않았습니다.")

#5
sticker = int(input("스티커 구매 개수: "))
sticker_price= 1000*sticker
book = int(input("책갈피 구매 개수: "))
book_price=2500*book
sum=sticker_price+book_price
sum_user=int(sum*0.9)
user=input("우수회원 이신가요?(yes/no): ")

if user == "yes":
    print("우수회원 할인으로 10% 할인을 받았습니다.")
    print("내가 낸 총 금액은",sum_user,"원 입니다.")
else:
    print("우수회원 할인을 받지 못했습니다.")
    print("내가 낸 총 금액은",sum,"원 입니다.")