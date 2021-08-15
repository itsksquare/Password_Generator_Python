from tkinter import *
import random, string
import pyperclip

root =Tk()
root.geometry("400x250")
root.resizable(0, 0)
root.title("PASSWORD GENERATOR")
root.configure(bg="#FFFFFF")

#heading
heading = Label(root, text = 'PASSWORD GENERATOR', font ='calibri 15 bold').pack()

pass_len = IntVar()
pass_str = StringVar()


###select password length
Label(root, text = 'PASSWORD LENGTH', font = 'calibri 10 bold').place(x = 50, y= 50)
length = Spinbox(root, from_= 8, to_ = 32, textvariable = pass_len, width = 15).place(x = 200, y= 50)
# YOUR PASSWORD
Label(root, text = 'YOUR PASSWORD', font = 'calibri 10 bold').place(x = 50, y= 80)
Entry(root, textvariable = pass_str).place(x = 200, y= 80)


#####define function



def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase)+\
                   random.choice(string.ascii_lowercase)+\
                   random.choice(string.digits)+\
                   random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase +
                                          string.ascii_lowercase +
                                          string.digits +
                                          string.punctuation)
    pass_str.set(password)


def Copy_password():
    pyperclip.copy(pass_str.get())


Button(root, text = "GENERATE", command = Generator).place(x = 100, y= 120)
Button(root, text = 'COPY', command = Copy_password).place(x = 200, y= 120)


# loop to run program
root.mainloop()


