from tkinter import *
import pyautogui

check_click = False

def on_click():
	global check_click
	check_click = True
	while True:
		if check_click:
			pyautogui.click()
			da.update()
def off_click():
	global check_click
	check_click = False
	da.update()

da = Tk()
da.title('Кликер')
da.geometry('200x400')

bg = '#01993b'
da['bg'] = bg

Label(da,text='Кликер',bg=bg,fg='white',font=('Arial',20)).place(x=50, y=0)

Button(da, text="Включить кликер",bd=5,bg=bg,fg='white',command=on_click).place(x=30, y=150)
Button(da, text="Отключить кликер",bd=5,bg=bg,fg='white',command=off_click).place(x=25, y=200)

da.mainloop()