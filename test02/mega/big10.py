from tkinter import messagebox
name=input("짝 이름: ")
hobbit=input("짝의 관심사: ")
messagebox.showinfo("짝 이름 ",name)
messagebox.showinfo("짝 관심사",hobbit)

if hobbit == "파이썬":
    answer=messagebox.askquestion("파이썬이 확실한가요?")
    if answer == "yes":
        messagebox.showinfo("결과","열심히하세요!")
    else:
        messagebox.showinfo("결과","그럼 생각중이시군요!")
else:
    messagebox.showinfo("결과","데이터 분석가가 되실 거군요")