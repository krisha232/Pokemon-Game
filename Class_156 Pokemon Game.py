from tkinter import *
from PIL import ImageTk, Image
root=Tk()

root.title("Pokemon Game")
root.geometry("600x400")
root.configure(background="maroon")

abra=ImageTk.PhotoImage(Image.open("abra.jpg")) 
bulbasour=ImageTk.PhotoImage(Image.open("bulbasour.jpg")) 
charmender=ImageTk.PhotoImage(Image.open("charmender.jpg")) 
Iyvasour=ImageTk.PhotoImage(Image.open("Iyvasour.jpg")) 
JigglyPuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg")) 
Kadabra=ImageTk.PhotoImage(Image.open("kadabra.jpg")) 
Meowth=ImageTk.PhotoImage(Image.open("meowth.jpg")) 
Nidoking=ImageTk.PhotoImage(Image.open("nidoking.jpg")) 
paras=ImageTk.PhotoImage(Image.open("paras.jpg")) 
Persion=ImageTk.PhotoImage(Image.open("persion.jpg")) 
Pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg")) 
Ratata=ImageTk.PhotoImage(Image.open("ratata.jpg")) 
Squirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg")) 

player1=Label(root,text="Player 1", bg="white", fg="black")
player1.place(relx=0.1, rely=0.3, anchor=CENTER)


player2=Label(root,text="Player 2", bg="white", fg="black")
player2.place(relx=0.9, rely=0.3, anchor=CENTER)

score_1=Label(root, bg="white", fg="black")
score_1.place(relx=0.1,rely=0.4,anchor=CENTER)

score_2=Label(root, bg="white", fg="black")
score_2.place(relx=0.9,rely=0.4,anchor=CENTER)

random_dice=Label(root,bg="beige",fg="black")
random_dice.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()