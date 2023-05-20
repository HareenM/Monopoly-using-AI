from tkinter import *
import random
import time
root = Tk()

#Title of the project
root.title('Monopoly using AI')

img = PhotoImage(file="monopoly.png")
img1 = PhotoImage(file="jail.png")
img2 = PhotoImage(file="parking.png")
img3 = PhotoImage(file="go.png")
img4 = PhotoImage(file="chance1.png")
img5 = PhotoImage(file="club.png")
img6 = PhotoImage(file="income.png")
Dice1=PhotoImage(file="Alea_1.png")
Dice2=PhotoImage(file="Alea_2.png")
Dice3=PhotoImage(file="Alea_3.png")
Dice4=PhotoImage(file="Alea_4.png")
Dice5=PhotoImage(file="Alea_5.png")
Dice6=PhotoImage(file="Alea_6.png")



# Setting the canvas for making the Monopoly board
board = Canvas(root, width=1000, height=800,bg='cyan')
board.pack(side=LEFT)
board.create_image(8,  250, image=img4, anchor="nw")
board.create_image( 325, 140, image = img,anchor = "nw")
board.create_image(8,650,image=img1,anchor="nw")
board.create_image(8, 5, image=img2, anchor="nw")
board.create_image(855, 650, image=img3, anchor="nw")
board.create_image(5,150, image=img4, anchor="nw")
board.create_image(855,450, image=img4, anchor="nw")
board.create_image(855,5, image=img5, anchor="nw")
board.create_image(575,8, image=img6, anchor="nw")
board.create_image(575,655, image=img6, anchor="nw")
# Functions for creating the edges and the corners of the board
def squarebox(x1, y1, x2, y2):
    board.create_rectangle(x1, y1, x2, y2)


def redbox(x1, y1, x2, y2):
    board.create_rectangle(x1, y1, x2, y2, fill='red')


def bluebox(x1, y1, x2, y2):
    board.create_rectangle(x1, y1, x2, y2, fill='blue')


def greenbox(x1, y1, x2, y2):
    board.create_rectangle(x1, y1, x2, y2, fill='green')


def yellowbox(x1, y1, x2, y2):
    board.create_rectangle(x1, y1, x2, y2, fill='yellow')


def whitebox(x1, y1, x2, y2):
    board.create_rectangle(x1, y1, x2, y2, fill='white')


def mainbox(x1, y1, x2, y2):
    board.create_rectangle(x1, y1, x2, y2)


# creating the corner tiles
TopLeft=[squarebox(5, 5, 155, 150)]
BottomLeft=[squarebox(5, 650, 155, 800)]
TopRight=[squarebox(845, 5, 995, 150)]
BottomRight=[squarebox(855, 650, 995, 795)]


# creating the left edge tiles
Left_Edge = [redbox(5, 650, 155, 550), bluebox(5, 550, 155, 450), greenbox(5, 450, 155, 350), yellowbox(5, 350, 155, 250),squarebox(5,250,155,150)]

# creating the top edge tiles
Top_Edge=[redbox(155, 5, 295, 150),bluebox(295, 5, 435, 150),yellowbox(435, 5, 575, 150),squarebox(575, 5, 715, 150),greenbox(715, 5, 855, 150)]

# creating the right edge tiles
Right_Edge=[redbox(855, 150, 995, 250),bluebox(855, 250, 995, 350),yellowbox(855, 350, 995, 450),squarebox(855, 450, 995, 550),greenbox(855, 550, 995, 650)]

# creating the bottom edge tiles
Bottom_Edge=[redbox(155, 655, 295, 795),bluebox(295, 655, 435, 795),yellowbox(435, 655, 575, 795),squarebox(575, 655, 715, 795),greenbox(715, 655, 855, 795) ]

# naming the left edge tiles
#board.create_text(500, 400, text="MONOPOLY", font=("Times", 30))
board.create_text(80, 600, text=" DELHI ", anchor="center")
board.create_text(80, 500, text="KOLKATA", anchor="center")
board.create_text(80, 400, text="AHMEDABAD", anchor="center")
board.create_text(80, 300, text="CHANDIGARH", anchor="center")

# naming the top edge tiles
board.create_text(225, 90, text="HYDERABAD", anchor="center")
board.create_text(368, 90, text="PANAJI", anchor="center")
board.create_text(503, 90, text=" LUCKNOW ", anchor="center")
board.create_text(783, 90, text=" JAIPUR ", anchor="center")

# naming the right edge tiles
board.create_text(930, 200, text="CHENNAI", anchor="center")
board.create_text(930, 300, text="PUNE", anchor="center")
board.create_text(930, 400, text=" NAGPUR ", anchor="center")
board.create_text(930, 600, text=" INDORE ", anchor="center")

# naming the bottom edge titles
board.create_text(225, 730, text="BANGLORE", anchor="center")
board.create_text(360, 730, text="MUMBAI", anchor="center")
board.create_text(495, 730, text=" KOCHI ", anchor="center")
board.create_text(775, 730, text=" SURAT ", anchor="center")

#functions for the commands of the buttons of tickets
def Surat():
    new_window=Toplevel(root)
    new_window.title("Surat")
    new_window.geometry("250x200")
    new_window['bg']='green'
    Label(new_window, text=" Price=Rs 8000\- \n\n Rent=Rs 1200\- \n ", bg='green').pack()
def Kochi():
    new_window=Toplevel(root)
    new_window.title("Kochi")
    new_window.geometry("250x200")
    new_window['bg']='yellow'
    Label(new_window, text=" Price=Rs 3500\- \n\n Rent=Rs 350\- \n",bg='yellow').pack()
def IncomeTax():
    new_window=Toplevel(root)
    new_window.title("IncomeTax")
    new_window.geometry("250x200")
    Label(new_window, text="100*number of tickects owned ").pack()
def Mumbai():
    new_window=Toplevel(root)
    new_window.title("Mumbai")
    new_window.geometry("250x200")
    new_window['bg'] = 'blue'
    Label(new_window, text=" Price=Rs 2500\- \n\n Rent=Rs 250\- \n ", bg="blue").pack()
def Banglore():
    new_window=Toplevel(root)
    new_window.title("Banglore")
    new_window.geometry("250x200")
    new_window['bg'] = 'red'
    Label(new_window, text=" Price=Rs 3000 \n\n Rent=Rs 300 \n ", bg="red").pack()
def Delhi():
    new_window=Toplevel(root)
    new_window.title("Delhi")
    new_window.geometry("250x200")
    new_window['bg'] = 'red'
    Label(new_window, text=" Price=Rs 6000 \n\n Rent=Rs 600 \n ", bg="red").pack()
def Kolkata():
    new_window=Toplevel(root)
    new_window.title("Kolkata")
    new_window.geometry("250x200")
    new_window['bg'] = 'blue'
    Label(new_window, text=" Price=Rs 4000 \n\n Rent=Rs 400 \n ", bg="blue").pack()
def Ahmedabad():
    new_window=Toplevel(root)
    new_window.title("Ahmedabad")
    new_window.geometry("250x200")
    new_window['bg'] = 'green'
    Label(new_window, text=" Price=Rs 2500 \n\n Rent=Rs 250 \n ", bg="green").pack()
def Chandigarh():
    new_window=Toplevel(root)
    new_window.title("Chandigarh")
    new_window.geometry("250x200")
    new_window['bg'] = 'yellow'
    Label(new_window, text=" Price=Rs 7000 \n\n Rent=Rs 900 \n ", bg="yellow").pack()
def Chance():
    new_window=Toplevel(root)
    new_window.title("Chance")
    new_window.geometry("250x200")
    Label(new_window, text=" A random event which may result\n in the player's profit or loss will be triggered ").pack()
def Hyderabad():
    new_window=Toplevel(root)
    new_window.title("Hyderabad")
    new_window.geometry("250x200")
    new_window['bg'] = 'red'
    Label(new_window, text=" Price=Rs 4000 \n\n Rent=Rs 400 \n ", bg="red").pack()
def Panaji():
    new_window=Toplevel(root)
    new_window.title("Panaji")
    new_window.geometry("250x200")
    new_window['bg'] = 'blue'
    Label(new_window, text=" Price=Rs 1500 \n\n Rent=Rs 200 \n ", bg="blue").pack()
def Lucknow():
    new_window=Toplevel(root)
    new_window.title("Lucknow")
    new_window.geometry("250x200")
    new_window['bg'] = 'yellow'
    Label(new_window, text=" Price=Rs 2800 \n\n Rent=Rs 280 \n ", bg="yellow").pack()
def IncomeTax():
    new_window=Toplevel(root)
    new_window.title("Income Tax")
    new_window.geometry("250x200")
    Label(new_window, text=" Income Tax of 300 \n will be deducted from the player ").pack()
def Jaipur():
    new_window=Toplevel(root)
    new_window.title("Jaipur")
    new_window.geometry("250x200")
    new_window['bg'] = 'green'
    Label(new_window, text=" Price=Rs 3000 \n\n Rent=Rs 300 \n ", bg="green").pack()
def Chennai():
    new_window=Toplevel(root)
    new_window.title("Chennai")
    new_window.geometry("250x200")
    new_window['bg'] = 'red'
    Label(new_window, text=" Price=Rs 2000 \n\n Rent=Rs 200 \n ", bg="red").pack()
def Pune():
    new_window=Toplevel(root)
    new_window.title("Pune")
    new_window.geometry("250x200")
    new_window['bg'] = 'blue'
    Label(new_window, text=" Price=Rs 5000 \n\n Rent=Rs 550 \n ", bg="blue").pack()
def Nagpur():
    new_window=Toplevel(root)
    new_window.title("Nagpur")
    new_window.geometry("250x200")
    new_window['bg'] = 'yellow'
    Label(new_window, text=" Price=Rs 3000 \n\n Rent=Rs 300 \n ", bg="yellow").pack()
def Indore():
    new_window=Toplevel(root)
    new_window.title("Indore")
    new_window.geometry("250x200")
    new_window['bg'] = 'green'
    Label(new_window, text=" Price=Rs 2700 \n\n Rent=Rs 200 \n ", bg="green").pack()

#creating a function for displaying the rules with the press of the "Rules" button
def RuleDisplay():
    new_window=Toplevel(root)
    new_window.title("Rules of the game")
    new_window.geometry("900x500")
    Label(new_window, text="\nObjective:The objective of the game is to become the wealthiest player\n\n"
                           "Both the player and the AI get Rs.15000 to start with\n\n"
                           "The details of the wealth and the places owned are displayed on the right side\n\n"
                           "The game starts with the player rolling the dice and each gets only a throw per turn\n\n"
                           "Each time a piece lands on or passes over GO, they get a  a Rs.1000 salary.\n\n"
                           "When you land on an unowned property you may choose to buy it with the 'buy' button\n\n"
                           "When you land on an owned property, the owner takes rent from you as given in the property information\n\n"
                           "When you land on chance, you an event will trigger which would either get you proft or loss\n\n"
                           "When you land on Income Tax, Rs.500 will be deducted from your account\n\n"
                           "If you land in Jail, Rs.500 will automatically be deducted\n\n"
                           "You are declared bankrupt if you owe more than you can pay\n\n", font=("Arial",14)).pack()


def EndGame():
    global money
    global places
    global places_ai
    if money[0]>money[1]:
        a1=board.create_text(720, 520, text="Player Won",anchor="center",font=('Helvetica','14'))
        root.after(10000, board.delete, a1)
    if money[1]>money[0]:
        a1 = board.create_text(720, 520, text="AI Won", anchor="center", font=('Helvetica', '14'))
        root.after(10000, board.delete, a1)

#button for expanding the Delhi ticket
tkt_btn1 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn1, borderwidth = 0, command=Delhi)
btn.place(x= 140, y= 635)

#button for expanding the Kolkata ticket
tkt_btn2 = PhotoImage(file ="button.png")
btn = Button(root, image = tkt_btn2, borderwidth = 0, command=Kolkata)
btn.place(x= 140, y= 535)

#button for expanding the Ahmedabad ticket
tkt_btn3 = PhotoImage(file ="button.png")
btn = Button(root, image = tkt_btn3, borderwidth = 0, command=Ahmedabad)
btn.place(x= 140, y= 435)

#button for expanding the Chandigarh ticket
tkt_btn4 = PhotoImage(file ="button.png")
btn = Button(root, image = tkt_btn4, borderwidth = 0, command=Chandigarh)
btn.place(x= 140, y= 335)

#button for expanding the Chance ticket
tkt_btn5 = PhotoImage(file ="button.png")
btn = Button(root, image = tkt_btn5, borderwidth = 0, command=Chance)
btn.place(x= 140, y= 235)

#button for expanding the Hyderabad ticket
tkt_btn6 = PhotoImage(file ="button.png")
btn = Button(root, image = tkt_btn6, borderwidth = 0, command=Hyderabad)
btn.place(x= 280, y= 135)

#button for expanding the Panaji ticket
tkt_btn7 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn7, borderwidth = 0, command=Panaji)
btn.place(x= 420, y= 135)

#button for expanding the Lucknow ticket
tkt_btn8 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn8, borderwidth = 0, command=Lucknow)
btn.place(x= 560, y= 135)

#button for expanding the Income Tax ticket
tkt_btn9 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn9, borderwidth = 0, command=IncomeTax)
btn.place(x= 700, y= 135)

#button for expanding Jaipur ticket
tkt_btn10 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn10, borderwidth = 0, command=Jaipur)
btn.place(x= 840, y= 135)

#button for expanding Chennai ticket
tkt_btn11 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn11, borderwidth = 0, command=Chennai)
btn.place(x= 980, y= 235)

#button for expanding Pune ticket
tkt_btn12 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn12, borderwidth = 0, command=Pune)
btn.place(x= 980, y= 335)

#button for expanding Nagpur ticket
tkt_btn13 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn13, borderwidth = 0, command=Nagpur)
btn.place(x= 980, y= 435)

#button for expanding Chance ticket
tkt_btn14 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn14, borderwidth = 0, command=Chance)
btn.place(x= 980, y= 535)

#button for expanding Indore ticket
tkt_btn15 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn15, borderwidth = 0, command=Indore)
btn.place(x= 980, y= 635)

#button for expanding Banglore ticket
tkt_btn16 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn16, borderwidth = 0, command=Banglore)
btn.place(x= 280, y= 780)

#button for expanding Mumbai ticket
tkt_btn17 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn17, borderwidth = 0, command=Mumbai)
btn.place(x= 420, y= 780)

#button for expanding Kochi ticket
tkt_btn18 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn18, borderwidth = 0, command=Kochi)
btn.place(x= 560, y= 780)

#button for expanding Income tax ticket
tkt_btn19 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn19, borderwidth = 0, command=IncomeTax)
btn.place(x= 700, y= 780)

#button for expanding Surat ticket
tkt_btn20 = PhotoImage(file = "button.png")
btn = Button(root, image = tkt_btn20, borderwidth = 0, command=Surat)
btn.place(x= 840, y= 780)

rounds=0
rounds_ai=0
count=1
flag1=1
flag2=1
flag3=1
flag4=1
flag5=1
flag6=1
flag7=1
flag8=1
flag9=1
flag10=1
flag11=1
flag12=1
flag13=1
flag14=1
flag15=1
flag16=1

def rent_ai():
    global flag1
    global flag2
    global flag3
    global flag4
    global flag5
    global flag6
    global flag7
    global flag8
    global flag9
    global flag10
    global flag11
    global flag12
    global flag13
    global flag14
    global flag15
    global flag16
    AIpos = board.bbox(ai)
    a1, b1, a2, b2 = AIpos
    if a1 > 715 and b1 > 655 and a2 < 855 and b2 < 795:
        if flag1==0:
            money[1]=money[1]-1200
            amt_ai.set(money[1])
            money[0]=money[0]+1200
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
    elif a1 > 435 and b1 > 655 and a2 < 575 and b2 < 795:
        if flag2==0:
            money[1]=money[1]-350
            amt_ai.set(money[1])
            money[0]=money[0]+350
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 295 and b1 > 655 and a2 < 435 and b2 < 795:
        if flag3 == 0:
            money[1] = money[1] - 250
            amt_ai.set(money[1])
            money[0] = money[0] + 250
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 155 and b1 > 655 and a2 < 295 and b2 < 795:
        if flag4 == 0:
            money[1] = money[1] - 300
            amt_ai.set(money[1])
            money[0] = money[0] + 300
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 5 and b1 < 650 and a2 < 155 and b2 > 550:
        if flag5 == 0:
            money[1] = money[1] - 600
            amt_ai.set(money[1])
            money[0] = money[0] + 600
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 5 and b1 < 550 and a2 < 155 and  b2 > 450:
        if flag6 == 0:
            money[1] = money[1] - 400
            amt_ai.set(money[1])
            money[0] = money[0] + 400
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 5 and b1 < 450 and a2 < 155 and b2 > 350:
        if flag7 == 0:
            money[1] = money[1] - 250
            amt_ai.set(money[1])
            money[0] = money[0] + 250
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 5 and b1 < 350 and a2 < 155 and b2 > 250:
        if flag8 == 0:
            money[1] = money[1] - 900
            amt_ai.set(money[1])
            money[0] = money[0] + 900
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 155 and b1 > 5 and a2 < 295 and b2 < 150:
        if flag9 == 0:
            money[1] = money[1] - 400
            amt_ai.set(money[1])
            money[0] = money[0] + 400
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 295 and b1 > 5 and a2 < 435 and b2 < 150:
        if flag10 == 0:
            money[1] = money[1] - 200
            amt_ai.set(money[1])
            money[0] = money[0] + 200
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 435 and b1 > 5 and a2 < 575 and b2 < 150:
        if flag11 == 0:
            money[1] = money[1] - 280
            amt_ai.set(money[1])
            money[0] = money[0] + 280
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 715 and b1 > 5 and a2 < 855 and b2 < 150:
        if flag12 == 0:
            money[1] = money[1] - 300
            amt_ai.set(money[1])
            money[0] = money[0] + 300
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 855 and b1 > 150 and a2 < 995 and b2 < 250:
        if flag13 == 0:
            money[1] = money[1] - 200
            amt_ai.set(money[1])
            money[0] = money[0] + 200
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 855 and b1 > 250 and a2 < 995 and b2 < 350:
        if flag14 == 0:
            money[1] = money[1] - 450
            amt_ai.set(money[1])
            money[0] = money[0] + 450
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 855 and b1 > 350 and a2 < 995 and b2 < 450:
        if flag15 == 0:
            money[1] = money[1] - 300
            amt_ai.set(money[1])
            money[0] = money[0] + 300
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 855 and b1 > 550 and a2 < 995 and b2 < 650:
        if flag16 == 0:
            money[1] = money[1] - 200
            amt_ai.set(money[1])
            money[0] = money[0] + 200
            amt.set(money[0])
            a1 = board.create_text(720, 500, text="AI paid rent to player", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)


def rent():
    global flag1
    global flag2
    global flag3
    global flag4
    global flag5
    global flag6
    global flag7
    global flag8
    global flag9
    global flag10
    global flag11
    global flag12
    global flag13
    global flag14
    global flag15
    global flag16
    playerpos = board.bbox(player1)
    a1, b1, a2, b2 = playerpos
    if a1 > 715 and b1 > 655 and a2 < 855 and b2 < 795:
        if flag1==2:
            money[0]=money[0]-1200
            amt.set(money[0])
            money[1]=money[1]+1200
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
    elif a1 > 435 and b1 > 655 and a2 < 575 and b2 < 795:
        if flag2==2:
            money[0]=money[0]-350
            amt.set(money[0])
            money[1]=money[1]+350
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 295 and b1 > 655 and a2 < 435 and b2 < 795:
        if flag3 == 2:
            money[0] = money[0] - 250
            amt.set(money[0])
            money[1] = money[1] + 250
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 155 and b1 > 655 and a2 < 295 and b2 < 795:
        if flag4 == 2:
            money[0] = money[0] - 250
            amt.set(money[0])
            money[1] = money[1] + 250
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 5 and b1 < 650 and a2 < 155 and b2 > 550:
        if flag5 == 2:
            money[0] = money[0] - 600
            amt.set(money[0])
            money[1] = money[1] + 600
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 5 and b1 < 550 and a2 < 155 and  b2 > 450:
        if flag6 == 2:
            money[0] = money[0] - 400
            amt.set(money[0])
            money[1] = money[1] + 400
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 5 and b1 < 450 and a2 < 155 and b2 > 350:
        if flag7 == 2:
            money[0] = money[0] - 250
            amt.set(money[0])
            money[1] = money[1] + 250
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 5 and b1 < 350 and a2 < 155 and b2 > 250:
        if flag8 == 2:
            money[0] = money[0] - 900
            amt.set(money[0])
            money[1] = money[1] + 900
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 155 and b1 > 5 and a2 < 295 and b2 < 150:
        if flag9 == 2:
            money[0] = money[0] - 400
            amt.set(money[0])
            money[1] = money[1] + 400
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 295 and b1 > 5 and a2 < 435 and b2 < 150:
        if flag10 == 2:
            money[0] = money[0] - 200
            amt.set(money[0])
            money[1] = money[1] + 200
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 435 and b1 > 5 and a2 < 575 and b2 < 150:
        if flag11 == 2:
            money[0] = money[0] - 280
            amt.set(money[0])
            money[1] = money[1] + 280
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 715 and b1 > 5 and a2 < 855 and b2 < 150:
        if flag12 == 2:
            money[0] = money[0] - 300
            amt.set(money[0])
            money[1] = money[1] + 300
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 855 and b1 > 150 and a2 < 995 and b2 < 250:
        if flag13 == 2:
            money[0] = money[0] - 200
            amt.set(money[0])
            money[1] = money[1] + 200
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 855 and b1 > 250 and a2 < 995 and b2 < 350:
        if flag14 == 2:
            money[0] = money[0] - 450
            amt.set(money[0])
            money[1] = money[1] + 450
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 855 and b1 > 350 and a2 < 995 and b2 < 450:
        if flag15 == 2:
            money[0] = money[0] - 300
            amt.set(money[0])
            money[1] = money[1] + 300
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)
    elif a1 > 855 and b1 > 550 and a2 < 995 and b2 < 650:
        if flag16 == 2:
            money[0] = money[0] - 200
            amt.set(money[0])
            money[1] = money[1] + 200
            amt.set(money[1])
            a1 = board.create_text(720, 500, text="Player paid rent to AI", anchor="center",
                                   font=('Helvetica', '12'))
            root.after(1500, board.delete, a1)

#creating a function for rolling the dice with the press of the the "Roll Dice" button
def Dice():
    global count
    count=count+1
    dice_input=random.randint(1, 6)

    #dice roll for 1
    if (dice_input==1):
        board.create_image(460, 420, image=Dice1, anchor="nw")
        single_move()
    #dice roll for 2
    if (dice_input==2):
        board.create_image(460, 420, image=Dice2, anchor="nw")
        single_move()
        single_move()
    #dice roll for 3
    if (dice_input==3):
        board.create_image(460, 420, image=Dice3, anchor="nw")
        single_move()
        single_move()
        single_move()
    #dice roll for 4
    if (dice_input==4):
        board.create_image(460, 420, image=Dice4, anchor="nw")
        single_move()
        single_move()
        single_move()
        single_move()
    #dice roll for 5
    if (dice_input==5):
        board.create_image(460, 420, image=Dice5, anchor="nw")
        single_move()
        single_move()
        single_move()
        single_move()
        single_move()
    #dice roll for 6
    if (dice_input==6):
        board.create_image(460, 420, image=Dice6, anchor="nw")
        single_move()
        single_move()
        single_move()
        single_move()
        single_move()
        single_move()
    if count%2==0:
        rent()
        pos = board.bbox(player1)
        a1, b1, a2, b2 = pos
        if money[0]==0:
            a1 = board.create_text(720, 520, text="AI won, Player Bankrupt", anchor="center",
                                   font=('Helvectica', '12'))
            root.after(10000, board.delete, a1)
        elif ((a1 > 575 and b1 > 655 and a2 < 715 and b2 < 795) or (a1 > 575 and b1 > 5 and a2 < 715 and b2 < 150)):
            money[0] = money[0] - 200
            amt.set(money[0])
            a1 = board.create_text(720, 520, text="Tax collected from Player", anchor="center", font=('Helvectica', '12'))
            root.after(2500, board.delete, a1)
        elif (a1 > 5 and b1 > 655 and a2 < 155 and b2 < 795):
            money[0] = money[0] - 500
            amt.set(money[0])
            a1 = board.create_text(720, 520, text="Player landed in Jail -Rs.500", anchor="center", font=('Helvectica', '12'))
            root.after(2500, board.delete, a1)
        elif (a1 > 845 and b1 > 5 and a2 < 995 and b2 < 150):
            money[0] = money[0] + 500
            amt.set(money[0])
            a1 = board.create_text(720, 520, text="Player landed in ClubHouse +Rs.500", anchor="center", font=('Helvectica', '12'))
            root.after(2500, board.delete, a1)
        elif ((a1 > 5 and b1 < 250 and a2 < 155 and b2 > 150) or (a1 > 855 and b1 > 450 and a2 < 995 and b2 < 550)):
            if (dice_input == 1):
                money[0] = money[0] - 500
                amt.set(money[0])
                a1 = board.create_text(720, 520, text="Player landed in Chance", anchor="center",
                                       font=('Helvectica', '12'))
                root.after(2500, board.delete, a1)
            if (dice_input == 2):
                money[0] = money[0] + 1000
                amt.set(money[0])
                a1 = board.create_text(720, 520, text="Player landed in Chance", anchor="center",
                                       font=('Helvectica', '12'))
                root.after(2500, board.delete, a1)
            if (dice_input == 3):
                money[0] = money[0] - 100
                amt.set(money[0])
                a1 = board.create_text(720, 520, text="Player landed in Chance", anchor="center",
                                       font=('Helvectica', '12'))
                root.after(2500, board.delete, a1)
            if (dice_input == 4):
                money[0] = money[0] + 700
                amt.set(money[0])
                a1 = board.create_text(720, 520, text="Player landed in Chance", anchor="center",
                                       font=('Helvectica', '12'))
                root.after(2500, board.delete, a1)
            if (dice_input == 5):
                money[0] = money[0] - 700
                amt.set(money[0])
                a1 = board.create_text(720, 520, text="Player landed in Chance", anchor="center",
                                       font=('Helvectica', '12'))
                root.after(2500, board.delete, a1)
            if (dice_input == 6):
                money[0] = money[0] + 500
                amt.set(money[0])
                a1 = board.create_text(720, 520, text="Player landed in Chance", anchor="center",
                                       font=('Helvectica', '12'))
                root.after(2500, board.delete, a1)
    else:
        rent_ai()
        pos = board.bbox(ai)
        a1, b1, a2, b2 = pos
        if money[0]==0:
            a1 = board.create_text(720, 520, text="Player won, AI Bankrupt", anchor="center",
                                   font=('Helvectica', '12'))
            root.after(10000, board.delete, a1)
        elif ((a1 > 575 and b1 > 655 and a2 < 715 and b2 < 795) or (a1 > 575 and b1 > 5 and a2 < 715 and b2 < 150)):
            money[1] = money[1] - 200
            amt_ai.set(money[1])
            a1 = board.create_text(720, 520, text="Tax collected from AI", anchor="center", font=('Helvectica', '12'))
            root.after(2500, board.delete, a1)
        elif (a1 > 5 and b1 > 655 and a2 < 155 and b2 < 795):
            money[1] = money[1] - 500
            amt_ai.set(money[1])
            a1 = board.create_text(720, 520, text="AI landed in Jail -Rs.500", anchor="center", font=('Helvectica', '12'))
            root.after(2500, board.delete, a1)
        elif (a1 > 845 and b1 > 5 and a2 < 995 and b2 < 150):
            money[1] = money[1] + 500
            amt_ai.set(money[1])
            a1 = board.create_text(720, 520, text="AI landed in ClubHouse +Rs.500", anchor="center",
                                   font=('Helvectica', '12'))
            root.after(2500, board.delete, a1)
        elif ((a1 > 5 and b1 < 250 and a2 < 155 and b2 > 150) or (a1 > 855 and b1 > 450 and a2 < 995 and b2 < 550)):
            if (dice_input == 1):
                money[1] = money[1] - 500
                amt_ai.set(money[1])
                a1 = board.create_text(720, 520, text="AI landed in Chance", anchor="center",
                                       font=('Helvectica', '12'))
                root.after(2500, board.delete, a1)
            if (dice_input == 2):
                money[1] = money[1] + 1000
                amt_ai.set(money[1])
                a1 = board.create_text(720, 520, text="AI landed in Chance", anchor="center",
                                       font=('Helvectica', '12'))
                root.after(2500, board.delete, a1)
            if (dice_input == 3):
                money[1] = money[1] - 100
                amt_ai.set(money[1])
                a1 = board.create_text(720, 520, text="AI landed in Chance", anchor="center",
                                       font=('Helvectica', '12'))
                root.after(2500, board.delete, a1)
            if (dice_input == 4):
                money[1] = money[1] + 700
                amt_ai.set(money[1])
                a1 = board.create_text(720, 520, text="AI landed in Chance", anchor="center",
                                       font=('Helvectica', '12'))
                root.after(2500, board.delete, a1)
            if (dice_input == 5):
                money[1] = money[1] - 700
                amt_ai.set(money[1])
                a1 = board.create_text(720, 520, text="AI landed in Chance", anchor="center",
                                       font=('Helvectica', '12'))
                root.after(2500, board.delete, a1)
            if (dice_input == 6):
                money[1] = money[1] + 500
                amt_ai.set(money[1])
                a1 = board.create_text(720, 520, text="AI landed in Chance", anchor="center",
                                       font=('Helvectica', '12'))
                root.after(2500, board.delete, a1)
count1=0
count1_ai=0

#function to move the piece from one ticket to another
def single_move():
    global rounds
    global rounds_ai
    global count1
    global count1_ai
    global count
    side = board.bbox(player1)
    x1, y1, x2, y2 = side
    side1 = board.bbox(ai)
    a1, b1, a2, b2 = side1
    if count%2==0: #Player's Turn
        count1 = count1 + 1
        if x1 < 995 and y1 > 650 and x2 > 155 and y2 > 650:
            board.move(player1, -135, 0)
        elif x1 < 155 and y1 < 800 and x2 < 155 and y2 > 150:
            board.move(player1, 0, -100)
        elif x1 > 5 and y1 < 150 and x2 < 845 and y2 < 150:
            board.move(player1, 135, 0)
        elif x1 > 650 and y1 > 5 and x2 > 855 and y2 < 650:
            board.move(player1, 0, 100)
        if count1 % 24 == 0:
            money[0] = money[0] + 1000
            amt.set(money[0])
            a1=board.create_text(720, 520, text="Player completed a turn", anchor="center", font=('Helvectica', '12'))
            root.after(2500, board.delete, a1)
            rounds = rounds + 1
    elif count%2!=0: #AI's Turn
        count1_ai = count1_ai +1
        if a1 < 995 and b1 > 650 and a2 > 155 and b2 > 650:
            board.move(ai, -135, 0)
        elif a1 < 155 and b1 < 800 and a2 < 155 and b2 > 150:
            board.move(ai, 0, -100)
        elif a1 > 5 and b1 < 150 and a2 < 845 and b2 < 150:
            board.move(ai, 135, 0)
        elif a1 > 650 and b1 > 5 and a2 > 855 and b2 < 650:
            board.move(ai, 0, 100)
        if count1_ai % 24 == 0:
            money[1] = money[1] + 1000
            amt_ai.set(money[1])
            a1 = board.create_text(720, 520, text="AI completed a turn", anchor="center", font=('Helvectica', '12'))
            root.after(2500, board.delete, a1)
            rounds_ai = rounds_ai + 1
rank=[0]*16
def ranking():
    global rank
    rank[0]=random.randint(1,16)
    rank[1] = random.randint(1, 16)
    rank[2] = random.randint(1, 16)
    rank[3] = random.randint(1, 16)
    rank[4] = random.randint(1, 16)
    rank[5] = random.randint(1, 16)
    rank[6] = random.randint(1, 16)
    rank[7] = random.randint(1, 16)
    rank[8] = random.randint(1, 16)
    rank[9] = random.randint(1, 16)
    rank[10] = random.randint(1, 16)
    rank[11] = random.randint(1, 16)
    rank[12] = random.randint(1, 16)
    rank[13] = random.randint(1, 16)
    rank[14] = random.randint(1, 16)
    rank[15] = random.randint(1, 16)
ranking()
for item in rank:
    print(item)
def Algorithm():
    AIpos = board.bbox(ai)
    a1, b1, a2, b2 = AIpos
    global rank
    if a1 > 715 and b1 > 655 and a2 < 855 and b2 < 795 and rank[0]<10:
        Yes_ai(1)
    elif a1 > 715 and b1 > 655 and a2 < 855 and b2 < 795 and rank[0]>=10:
        Yes_ai(17)
    elif a1 > 435 and b1 > 655 and a2 < 575 and b2 < 795 and rank[1]<10:
        Yes_ai(2)
    elif a1 > 435 and b1 > 655 and a2 < 575 and b2 < 795 and rank[1]>=10:
        Yes_ai(17)
    elif a1 > 295 and b1 > 655 and a2 < 435 and b2 < 795 and rank[2]<10:
        Yes_ai(3)
    elif a1 > 295 and b1 > 655 and a2 < 435 and b2 < 795 and rank[2]>=10:
        Yes_ai(17)
    elif a1 > 155 and b1 > 655 and a2 < 295 and b2 < 795 and rank[3]<10:
        Yes_ai(4)
    elif a1 > 155 and b1 > 655 and a2 < 295 and b2 < 795 and rank[3]>=10:
        Yes_ai(17)
    elif a1 > 5 and b1 < 650 and a2 < 155 and b2 > 550 and  rank[4]<10:
        Yes_ai(5)
    elif a1 > 5 and b1 < 650 and a2 < 155 and b2 > 550 and  rank[4]>=10:
        Yes_ai(17)
    elif a1 > 5 and b1 < 650 and a2 < 155 and b2 > 550 and  rank[5]<10:
        Yes_ai(6)
    elif a1 > 5 and b1 < 650 and a2 < 155 and b2 > 550 and  rank[5]>=10:
        Yes_ai(17)
    elif a1 > 5 and b1 < 450 and a2 < 155 and b2 > 350 and rank[6]<10:
        Yes_ai(7)
    elif a1 > 5 and b1 < 450 and a2 < 155 and b2 > 350 and rank[6]>=10:
        Yes_ai(17)
    elif a1 > 5 and b1 < 350 and a2 < 155 and b2 > 250 and rank[7]<10:
        Yes_ai(8)
    elif a1 > 5 and b1 < 350 and a2 < 155 and b2 > 250 and rank[7]>=10:
        Yes_ai(17)
    elif a1 > 155 and b1 > 5 and a2 < 295 and b2 < 150 and rank[8]<10:
        Yes_ai(9)
    elif a1 > 155 and b1 > 5 and a2 < 295 and b2 < 150 and rank[8]>=10:
        Yes_ai(17)
    elif a1 > 295 and b1 > 5 and a2 < 435 and b2 < 150 and rank[9]<10:
        Yes_ai(10)
    elif a1 > 295 and b1 > 5 and a2 < 435 and b2 < 150 and rank[9]>=10:
        Yes_ai(17)
    elif a1 > 435 and b1 > 5 and a2 < 575 and b2 < 150 and rank[10]<10:
        Yes_ai(11)
    elif a1 > 435 and b1 > 5 and a2 < 575 and b2 < 150 and rank[10]>=10:
        Yes_ai(17)
    elif a1 > 715 and b1 > 5 and a2 < 855 and b2 < 150 and rank[11]<10:
        Yes_ai(12)
    elif a1 > 715 and b1 > 5 and a2 < 855 and b2 < 150 and rank[11]>=10:
        Yes_ai(17)
    elif a1 > 855 and b1 > 150 and a2 < 995 and b2 < 250 and rank[12]<10:
        Yes_ai(13)
    elif a1 > 855 and b1 > 150 and a2 < 995 and b2 < 250 and rank[12]>=10:
        Yes_ai(17)
    elif a1 > 855 and b1 > 250 and a2 < 995 and b2 < 350 and rank[13]<10:
        Yes_ai(14)
    elif a1 > 855 and b1 > 250 and a2 < 995 and b2 < 350 and rank[13]>=10:
        Yes_ai(17)
    elif a1 > 855 and b1 > 350 and a2 < 995 and b2 < 450 and rank[14]<10:
        Yes_ai(15)
    elif a1 > 855 and b1 > 350 and a2 < 995 and b2 < 450 and rank[14]>=10:
        Yes_ai(17)
    elif a1 > 855 and b1 > 550 and a2 < 995 and b2 < 650 and rank[15]<10:
        Yes_ai(16)
    elif a1 > 855 and b1 > 550 and a2 < 995 and b2 < 650 and rank[15]>=10:
        Yes_ai(17)

def AIturn():
    Dice()
    Algorithm()



player1=board.create_rectangle(915,695,935,715,fill='orange')
ai=board .create_rectangle(915,725,935,745,fill='#ffbbdd')
#Button for displaying the rules
btn=Button(root, text='Rules', height=2,width=10,borderwidth=3, command=RuleDisplay,bd='5',bg='#cccccc')
btn.place(x=330, y=450)

#Button for rolling the dice
btn = Button(root, text='Dice Roll', height=2,width=10,borderwidth=3, command=Dice,bd='5',bg='#cccccc')
btn.place(x=330, y=550)

#Button for Ending the turn of the Player
btn = Button(root, text='End Turn', height=2,width=10,borderwidth=3, command=AIturn,bd='5',bg='#cccccc')
btn.place(x=590, y=450)

#Button for ending the game
btn = Button(root, text='End Game', height=2,width=10,borderwidth=3, command=EndGame,bd='5',bg='#cccccc')
btn.place(x=750,y=600)

money = [15000,15000]
amt=IntVar()
amt_ai=IntVar()
amt.set(money[0])
amt_ai.set(money[1])
places=[]
places_ai=[]
city=StringVar()
city_ai=StringVar()

def Yes(c):
    global Flag
    global flag1
    global flag2
    global flag3
    global flag4
    global flag5
    global flag6
    global flag7
    global flag8
    global flag9
    global flag10
    global flag11
    global flag12
    global flag13
    global flag14
    global flag15
    global flag16

    if c==1:
        if flag1==1:
          if money[0] < 8000:
              a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
              root.after(1000, board.delete, a1)
          else:
              money[0] = money[0] - 8000
              amt.set(money[0])
              places.append("Surat")
              city.set(places)
              print(money[0])
              board.create_oval(720, 660,740 , 680,fill='orange')
              flag1=0
          Flag = 1
          a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
          root.after(2500, board.delete, a1)
        else:
            a1=board.create_text(720,520,text="CANNOT BUY THE PROPERTY",anchor="center", font=('Helvetica','12'))
            root.after(2500, board.delete, a1)

    elif c==2:
        if flag2 == 1:
            if money[0] < 3500:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 3500
                amt.set(money[0])
                places.append("Kochi")
                city.set(places)
                print(money[0])
                board.create_oval(440, 660, 460, 680, fill='orange')
                flag2 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a2=board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a2)

    elif c==3:
        if flag3==1:
            if money[0] < 2500:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 2500
                amt.set(money[0])
                places.append("Mumbai")
                city.set(places)
                print(money[0])
                board.create_oval(300, 660, 320, 680, fill='orange')
                flag3 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a3=board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a3)

    elif c==4:
        if flag4 == 1:
            if money[0] < 3000:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 3000
                amt.set(money[0])
                places.append("Banglore")
                city.set(places)
                print(money[0])
                board.create_oval(160, 660, 180, 680, fill='orange')
                flag4 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a4 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a4)

    elif c==5:
        if flag5 == 1:
            if money[0] < 6000:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 6000
                amt.set(money[0])
                places.append("Delhi")
                city.set(places)
                print(money[0])
                board.create_oval(135, 555, 155, 575, fill='orange')
                flag5 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a5 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a5)

    elif c==6:
        if flag6 == 1:
            if money[0] < 4000:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 4000
                amt.set(money[0])
                places.append("Kolkata")
                city.set(places)
                print(money[0])
                board.create_oval(135, 455, 155, 475, fill='orange')
                flag6 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a6 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a6)

    elif c==7:
        if flag7 == 1:
            if money[0] < 2500:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 2500
                amt.set(money[0])
                places.append("Ahemdabad")
                city.set(places)
                print(money[0])
                board.create_oval(135, 355, 155, 375, fill='orange')
                flag7 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a7 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a7)
    elif c==8:
        if flag8 == 1:
            if money[0] < 7000:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 7000
                amt.set(money[0])
                places.append("Chandigarh")
                city.set(places)
                print(money[0])
                board.create_oval(135, 255, 155, 275, fill='orange')
                flag8 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a8 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a8)
    elif c==9:
        if flag9 == 1:
            if money[0] < 4000:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 4000
                amt.set(money[0])
                places.append("Hyderabad")
                city.set(places)
                print(money[0])
                board.create_oval(155, 145, 175, 125, fill='orange')
                flag9 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a9 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a9)
    elif c==10:
        if flag10 == 1:
            if money[0] < 1500:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 1500
                amt.set(money[0])
                places.append("Panaji")
                city.set(places)
                print(money[0])
                board.create_oval(295, 145, 315, 125, fill='orange')
                flag10 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a10 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a10)
    elif c==11:
        if flag11 == 1:
            if money[0] < 2800:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 2800
                amt.set(money[0])
                places.append("Lucknow")
                city.set(places)
                print(money[0])
                board.create_oval(440, 145, 460, 125, fill='orange')
                flag11 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a11 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a11)
    elif c==12:
        if flag12 == 1:
            if money[0] < 3000:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 3000
                amt.set(money[0])
                places.append("Jaipur")
                city.set(places)
                print(money[0])
                board.create_oval(725, 145, 745, 125, fill='orange')
                flag12 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a12 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a12)
    elif c == 13:
        if flag13 == 1:
            if money[0] < 2000:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 2000
                amt.set(money[0])
                places.append("Chennai")
                city.set(places)
                print(money[0])
                board.create_oval(855, 150, 875, 170, fill='orange')
                flag13 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a13 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a13)
    elif c==14:
        if flag14 == 1:
            if money[0] < 5000:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 5000
                amt.set(money[0])
                places.append("Pune")
                city.set(places)
                print(money[0])
                board.create_oval(855, 250, 875, 270, fill='orange')
                flag14 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a14 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a14)
    elif c==15:
        if flag15 == 1:
            if money[0] < 3000:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 3000
                amt.set(money[0])
                places.append("Nagpur")
                city.set(places)
                print(money[0])
                board.create_oval(855, 350, 875, 370, fill='orange')
                flag15 = 0
            Flag = 1
            a1 = board.create_text(720, 550, text="END TURN", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a1)
        else:
            a15 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a15)
    elif c==16:
        if flag16 == 1:
            if money[0] < 2700:
                a1 = board.create_text(720, 520, text="YOU DO NOT HAVE ENOUGH MONEY", anchor="center",font=('Helvetica', '12'))
                root.after(1000, board.delete, a1)
            else:
                money[0] = money[0] - 2700
                amt.set(money[0])
                places.append("Indore")
                city.set(places)
                print(money[0])
                board.create_oval(855, 550, 875, 570, fill='orange')
                flag16 = 0
        else:
            a16 = board.create_text(720, 520, text="CANNOT BUY THE PROPERTY", anchor="center", font=('Helvetica', '12'))
            root.after(2500, board.delete, a16)


def Yes_ai(c):
    global flag1
    global flag2
    global flag3
    global flag4
    global flag5
    global flag6
    global flag7
    global flag8
    global flag9
    global flag10
    global flag11
    global flag12
    global flag13
    global flag14
    global flag15
    global flag16
    if c==1:
        if flag1==1:
            if money[1] > 8000:
                money[1] = money[1] - 8000
                amt_ai.set(money[1])
                places_ai.append("Surat")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(720, 660,740 , 680,fill='#ffbbdd')
                flag1=2
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(1500, board.delete, a1)
    elif c==2:
        if flag2 == 1:
            if money[1] > 3500:
                money[1] = money[1] - 3500
                amt_ai.set(money[1])
                places_ai.append("Kochi")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(440, 660, 460, 680, fill='#ffbbdd')
                flag2 = 2
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==3:
        if flag3==1:
            if money[1] > 2500:
                money[1] = money[1] - 2500
                amt_ai.set(money[1])
                places_ai.append("Mumbai")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(300, 660, 320, 680, fill='#ffbbdd')
                flag3 = 2
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==4:
        if flag4 == 1:
            if money[1] > 3000:
                money[1] = money[1] - 3000
                amt_ai.set(money[1])
                places_ai.append("Banglore")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(160, 660, 180, 680, fill='#ffbbdd')
                flag4 = 2
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==5:
        if flag5 == 1:
            if money[1] > 6000:
                money[1] = money[1] - 6000
                amt_ai.set(money[1])
                places_ai.append("Delhi")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(135, 555, 155, 575, fill='#ffbbdd')
                flag5 = 2
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==6:
        if flag6 == 1:
            if money[1] > 4000:
                money[1] = money[1] - 4000
                amt_ai.set(money[1])
                places_ai.append("Kolkata")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(135, 455, 155, 475, fill='#ffbbdd')
                flag6 = 2
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==7:
        if flag7 == 1:
            if money[1] > 2500:
                money[1] = money[1] - 2500
                amt_ai.set(money[1])
                places_ai.append("Ahemdabad")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(135, 355, 155, 375, fill='#ffbbdd')
                flag7 = 2
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==8:
        if flag8 == 1:
            if money[1] > 7000:
                money[1] = money[1] - 7000
                amt_ai.set(money[1])
                places_ai.append("Chandigarh")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(135, 255, 155, 275, fill='#ffbbdd')
                flag8 = 2
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==9:
        if flag9 == 1:
            if money[1] > 4000:
                money[1] = money[1] - 4000
                amt_ai.set(money[1])
                places_ai.append("Hyderabad")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(155, 145, 175, 125, fill='#ffbbdd')
                flag9 = 2
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==10:
        if flag10==1:
            if money[1] > 1500:
                money[1] = money[1] - 1500
                amt_ai.set(money[1])
                places_ai.append("Panaji")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(295, 145, 315, 125, fill='#ffbbdd')
                flag10 = 2
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==11:
        if flag11 == 1:
            if money[1] > 2800:
                money[1] = money[1] - 2800
                amt_ai.set(money[1])
                places_ai.append("Lucknow")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(440, 145, 460, 125, fill='#ffbbdd')
                flag11 = 2
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==12:
        if flag12 == 1:
            if money[1] > 3000:
                money[1] = money[1] - 3000
                amt_ai.set(money[1])
                places_ai.append("Jaipur")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(725, 145, 745, 125, fill='#ffbbdd')
                flag12 = 2
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c == 13:
        if flag13 == 1:
            if money[1] > 2000:
                money[1] = money[1] - 2000
                amt_ai.set(money[1])
                places_ai.append("Chennai")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(855, 150, 875, 170, fill='#ffbbdd')
                flag13 = 0
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==14:
        if flag14 == 1:
            if money[1] > 5000:
                money[1] = money[1] - 5000
                amt_ai.set(money[1])
                places_ai.append("Pune")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(855, 250, 875, 270, fill='#ffbbdd')
                flag14 = 0
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==15:
        if flag15 == 1:
            if money[1] > 3000:
                money[1] = money[1] - 3000
                amt_ai.set(money[1])
                places_ai.append("Nagpur")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(855, 350, 875, 370, fill='#ffbbdd')
                flag15 = 0
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==16:
        if flag16 == 1:
            if money[1] > 2700:
                money[1] = money[1] - 2700
                amt_ai.set(money[1])
                places_ai.append("Indore")
                city_ai.set(places_ai)
                print(money[1])
                board.create_oval(855, 550, 875, 570, fill='#ffbbdd')
                flag16 = 0
                time.sleep(0.5)
                a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                                       font=('Helvetica', '12'))
                root.after(2000, board.delete, a1)
    elif c==17:
        time.sleep(0.5)
        a1 = board.create_text(720, 520, text="Player's Turn", anchor="center",
                               font=('Helvetica', '12'))
        root.after(2000, board.delete, a1)

def ticket1():
    new_window1 = Toplevel(root)
    new_window1.title("Surat")
    new_window1.geometry("500x400")
    new_window1.configure(background="#FFFFBB")
    lt = Label(new_window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(new_window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(1))
    but.place(x=170, y=190)
    but = Button(new_window1, text='No', height=3, width=10, borderwidth=4, command=new_window1.destroy)
    but.place(x=270, y=190)


def ticket2():
    window1 = Toplevel(root)
    window1.title("Kochi")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(2))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)


def ticket3():
    window1 = Toplevel(root)
    window1.title("Mumbai")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(3))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)


def ticket4():
    window1 = Toplevel(root)
    window1.title("Banglore")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(4))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)
def ticket5():
    window1 = Toplevel(root)
    window1.title("Delhi")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(5))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)
def ticket6():
    window1 = Toplevel(root)
    window1.title("Kolkata")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(6))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)
def ticket7():
    window1 = Toplevel(root)
    window1.title("Ahemdabad")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(7))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)
def ticket8():
    window1 = Toplevel(root)
    window1.title("Chandigarh")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(8))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)
def ticket9():
    window1 = Toplevel(root)
    window1.title("Hyderabad")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(9))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)
def ticket10():
    window1 = Toplevel(root)
    window1.title("Panaji")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(10))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)
def ticket11():
    window1 = Toplevel(root)
    window1.title("Lucknow")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(11))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)
def ticket12():
    window1 = Toplevel(root)
    window1.title("Jaipur")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(12))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)
def ticket13():
    window1 = Toplevel(root)
    window1.title("Chennai")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(13))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)
def ticket14():
    window1 = Toplevel(root)
    window1.title("Pune")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(14))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)
def ticket15():
    window1 = Toplevel(root)
    window1.title("Nagpur")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(15))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)
def ticket16():
    window1 = Toplevel(root)
    window1.title("Indore")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    lt = Label(window1, text="Do you want to buy this ticket?", bg="#FFFFBB", font="Times 16 bold")
    lt.place(x=130, y=130)
    but = Button(window1, text='YES', height=3, width=11, borderwidth=4, command=lambda: Yes(16))
    but.place(x=170, y=190)
    but = Button(window1, text='No', height=3, width=10, borderwidth=4, bg='orange', command=window1.destroy)
    but.place(x=270, y=190)

def buy():
    playerpos = board.bbox(player1)
    a1, b1, a2, b2 = playerpos
    if a1 > 715 and b1 > 655 and a2 < 855 and b2 < 795:
        ticket1()
    elif a1 > 435 and b1 > 655 and a2 < 575 and b2 < 795:
        ticket2()
    elif a1 > 295 and b1 > 655 and a2 < 435 and b2 < 795:
        ticket3()
    elif a1 > 155 and b1 > 655 and a2 < 295 and b2 < 795:
        ticket4()
    elif a1 > 5 and b1 < 650 and a2 < 155 and b2 > 550:
        ticket5()
    elif a1 > 5 and b1 < 550 and a2 < 155 and b2 > 450:
        ticket6()
    elif a1 > 5 and b1 < 450 and a2 < 155 and b2 > 350:
        ticket7()
    elif a1 > 5 and b1 < 350 and a2 < 155 and b2 > 250:
        ticket8()
    elif a1 > 155 and b1 > 5 and a2 < 295 and b2 < 150:
        ticket9()
    elif a1 > 295 and b1 > 5 and a2 < 435 and b2 < 150:
        ticket10()
    elif a1 > 435 and b1 > 5 and a2 < 575 and b2 < 150:
        ticket11()
    elif a1 > 715 and b1 > 5 and a2 < 855 and b2 < 150:
        ticket12()
    elif a1 > 855 and b1 > 150 and a2 < 995 and b2 < 250:
        ticket13()
    elif a1 > 855 and b1 > 250 and a2 < 995 and b2 < 350:
        ticket14()
    elif a1 > 855 and b1 > 350 and a2 < 995 and b2 < 450:
        ticket15()
    elif a1 > 855 and b1 > 550 and a2 < 995 and b2 < 650:
        ticket16()

#function which is called in Chance rules Button
def charule():
    window1 = Toplevel(root)
    window1.title("Chance Rules")
    window1.geometry("500x400")
    window1.configure(background="#FFFFBB")
    l1=Label(window1,text='The kind of chance you get is based on the dice roll you got\n'
                        '1:Deducted Rs.500 for Vehicle Repairs\n'
                        '2:Added bonus of Rs.1000 on the event of birthday\n'
                        '3:Deducted Rs.100 for parking violations\n'
                        '4:Loyalty bonus of Rs.700 added\n'
                        '5:Decremented Rs.700 due to banking chanrges\n'
                        '6:You got Rs.500 from the lucky wheel\n', bg='#FFFFBB')
    l1.place(x=100, y=100)
    global places
    print(places)

#Button for buying the ticket
btn = Button(root, text='BUY',height=2,width=10,borderwidth=3,command=buy,bd='5',bg='#cccccc')
btn.place(x=465, y=550)

#Button for showing the rules of chance
btn = Button(root, text='Chance Rules',height=2,width=10,borderwidth=3,bd='5',bg='#cccccc',command=charule)
btn.place(x=590, y=550)

#canvas for the second part of the window where the human and AI stats are displayed
board2 = Canvas(root, width=600, height=800, bg="#aaaaaa")
board2.pack(side=RIGHT)


#Dynamic view for the stats of the Player
board2.create_rectangle(85,45,450,395, fill='orange')
board2.create_text(270, 70, text="VINEET", anchor="center", font=('Helvetica','14','bold'))
board2.create_text(150, 140, text="TOTAL BALANCE  =", anchor="center")
lb = Label(root,textvariable=amt,bg='orange')
board2.create_window(220,140,window=lb,anchor=CENTER)
board2.create_text(140, 180, text="Properties Owned:", anchor="center")
l1 = Label(root,textvariable=city, bg='orange')
board2.create_window(260,200,window=l1)
board2.create_text(140, 180, text="\n")

#Dynamic view for the stats of the AI
board2.create_rectangle(85,455,450,785, fill='#ffbbdd')
board2.create_text(270, 470, text="HAREEN AMIT", anchor="center", font=('Helvetica','14','bold'))
board2.create_text(150, 510, text="TOTAL BALANCE = ", anchor="center")
lb_ai = Label(root,textvariable=amt_ai,bg='#ffbbdd')
board2.create_window(220,510,window=lb_ai,anchor=CENTER)
board2.create_text(150, 550, text="Properties Owned:", anchor="center")
l1_ai = Label(root,textvariable=city_ai, bg='#ffbbdd')
board2.create_window(260,550,window=l1_ai)


root.mainloop()
