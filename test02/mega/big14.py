#자동 주석 처리 (컨트롤 + / )
#1
b=0
while b<100:
    print(b)
    b+=1
#2
b=0
while b<100:
    b+=1
    print(b)
#3
b=0
while b<100:
    b=b+1
    if(b%2==0):
        print(b)
#4
b=0
while b<100:
    b = b + 1
    if(b%3==0):
        print(b)

#5
a=0
b=0
while b<100:
    if(b%5==0 and b!=0):
        a=a+1
    b=b+1
print("5의 배수의 개수는",a)
#6
b=0
while b<5:
    print("안녕히가세요")
    b=b+1

