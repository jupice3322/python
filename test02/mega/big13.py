#네이버 로그인
#판단을 할 때 조건을 가지고 판단을 한다.
#조건이 하나가 아닌 경우 논리적으로 어떻게 판단할 것인가?
id = 'root'
pw = 'pass'

id2=input("아이디 입력: ")
pw2=input("패스워드 입력: ")

if id==id2 and pw==pw2:
    print("로그인 ok")
else:
    print("로그인 not")