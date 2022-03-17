from tkinter import *
import random
from PIL import ImageTk, Image
root=Tk()

root.title("Pokemon Game")
root.geometry("600x600")
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
image=ImageTk.PhotoImage(Image.open("button.jpg")) 

pokemon_images= [abra,bulbasour,charmender,Iyvasour,JigglyPuff,Kadabra,Meowth,Nidoking,paras,Persion,Pikachu,Ratata,Squirtle]
power=[30,60,50,100,70,70,60,90,40,70,200,40,50]

player1=Label(root,text="Player 1", bg="white", fg="black")
player1.place(relx=0.1, rely=0.3, anchor=CENTER)


player2=Label(root,text="Player 2", bg="white", fg="black")
player2.place(relx=0.9, rely=0.3, anchor=CENTER)

score_1=Label(root, bg="white", fg="black")
score_1.place(relx=0.1,rely=0.4,anchor=CENTER)

score_2=Label(root, bg="white", fg="black")
score_2.place(relx=0.9,rely=0.4,anchor=CENTER)

random_card=Label(root,bg="beige",fg="black")
random_card.place(relx=0.5,rely=0.5,anchor=CENTER)


player1_score=0

def player_1():
    global player1_score
    random_no = random.randint(0,+1)
    random_variable=pokemon_images[random_no]
    random_card["image"]=random_variable
    power_list=power[random_no]
    player1_score=player1_score+power_list
    score_1["text"]=str(player1_score)
    
player1_btn=Button(root,image=image,command=player_1)
player1_btn.place(relx=0.1,rely=0.6,anchor=CENTER)


player2_score=0
def player_2():
    global player2_score
    random_no2 = random.randint(0,+1)
    random_variable2=pokemon_images[random_no2]
    random_card["image"]=random_variable2
    power_list2=power[random_no2]
    player2_score=player2_score+power_list2
    score_2["text"]=str(player2_score)
    
player2_btn=Button(root,image=image,command=player_2)
player2_btn.place(relx=0.9,rely=0.6,anchor=CENTER)


root.mainloop()
