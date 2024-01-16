
from tkinter import *
from PIL import ImageTk, Image
import random

root=Tk()
root.title("Endless Battle Game")
root.geometry("800x600")
root.configure(background="orange")

img=ImageTk.PhotoImage(Image.open ("button.jpg"))

pikachu=ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
bulbasaur=ImageTk.PhotoImage(Image.open ("bulbasaur.jpg"))
charmander=ImageTk.PhotoImage(Image.open ("charmander.jpg"))
squirtle=ImageTk.PhotoImage(Image.open ("squirtle.jpg"))
rattata=ImageTk.PhotoImage(Image.open ("rattata.jpg"))
nidoking=ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
jigglypuff=ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
meowth=ImageTk.PhotoImage(Image.open ("meowth.jpg"))
img=ImageTk.PhotoImage(Image.open ())



pokemon_list = ("abra","bulbasaur","charmander","ivysaur","kadabra","meowth","nidoking","paris","persian","pikachu","rattata","squirtle"
           )


player1 = Label(root, text = "Player 1", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor =  CENTER)

player2 = Label(root, text = "Player 2", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely = 0.3 , anchor =  CENTER)

player_1_score_label = Label(root , bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4 , anchor =  CENTER)

player_2_score_label = Label(root , bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4 , anchor =  CENTER)

random_dice_label = Label(root,bg = "chocolate1", fg = "white")
random_dice_label.place(relx = 0.5, rely = 0.5 , anchor =  CENTER)



