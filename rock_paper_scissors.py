from tkinter import *
import random

root = Tk()

root.title("Rock Paper Scissors Game")
root.geometry("615x285")
root["bg"] = "#d9d9d9"

your_score = 0
computer_score = 0
tie = 0

#Rock Paper Scissors Label
rock_paper_scissors_label = Label(root, text = "Rock Paper Scissors")
rock_paper_scissors_label["font"] = ("bold", 17)
rock_paper_scissors_label["bg"] = "#d9d9d9"
rock_paper_scissors_label.place(x = 200,y = 10)

#Start of the game
lets_start_the_game_label = Label(root, text = "Let's Start the Game...")
lets_start_the_game_label["font"] = ("bold", 10)
lets_start_the_game_label["bg"] = "#d9d9d9"
lets_start_the_game_label["fg"] = "green"
lets_start_the_game_label.place(x = 230,y = 55)

#YourOptions Label
options_label = Label(root, text = "Your Options:")
options_label["bg"] = "#d9d9d9"
options_label.place(x = 71, y = 76)

#Score Label
score_label = Label(root, text = "Score:")
score_label["bg"] = "#d9d9d9"
score_label.place(x = 86, y = 150)

#you selected label
you_selected_label = Label(root,text= "You Selected:")
you_selected_label["bg"] = "#d9d9d9"
you_selected_label.place(x = 165, y = 175)

#you selected textbox
you_selected_textbox = Text(root,height = 1,width = 7)
you_selected_textbox["bg"] = "#d9d9d9"
you_selected_textbox.place(x = 250,y = 175)

#computer selected label
computer_selected_label = Label(root,text = "Computer Selected:")
computer_selected_label["bg"] = "#d9d9d9"
computer_selected_label.place(x = 150,y = 215)

#computer selected textbox
computer_selected_textbox = Text(root,height = 1,width = 7)
computer_selected_textbox["bg"] = "#d9d9d9"
computer_selected_textbox.place(x = 270,y = 215)

def rock():
    global your_score
    global computer_score

    you_selected = "Rock"
    you_selected_textbox.delete("1.0",END)
    you_selected_textbox.insert(INSERT,you_selected)
    
    computer_selected_list = ["Rock", "Paper", "Scissors"]
    computer_selected = random.choice(computer_selected_list)
    computer_selected_textbox.delete("1.0",END)
    computer_selected_textbox.insert(INSERT,computer_selected)
    
    if computer_selected == "Scissors":
        your_score += 1
    
    elif computer_selected == "Paper":
        computer_score += 1

    else:
        result = tie
    
    your_score_label.config(text = "Your Score: " + str(your_score))
    computer_score_label.config(text = "Computer Score: " + str(computer_score))

def paper():
    global your_score
    global computer_score

    you_selected = "Paper"
    you_selected_textbox.delete("1.0",END)
    you_selected_textbox.insert(INSERT,you_selected)
    
    computer_selected_list = ["Rock", "Paper", "Scissors"]
    computer_selected = random.choice(computer_selected_list)
    computer_selected_textbox.delete("1.0",END)
    computer_selected_textbox.insert(INSERT,computer_selected)

    if computer_selected == "Scissors":
        computer_score += 1
    
    elif computer_selected == "Paper":
        result = tie

    else:
        your_score += 1

    your_score_label.config(text = "Your Score: " + str(your_score))
    computer_score_label.config(text = "Computer Score: " + str(computer_score))

def scissors():
    global your_score
    global computer_score

    you_selected = "Scissors"
    you_selected_textbox.delete("1.0",END)
    you_selected_textbox.insert(INSERT,you_selected)
    
    computer_selected_list = ["Rock", "Paper", "Scissors"]
    computer_selected = random.choice(computer_selected_list)
    computer_selected_textbox.delete("1.0",END)
    computer_selected_textbox.insert(INSERT,computer_selected)

    if computer_selected == "Scissors":
        result = tie
    
    elif computer_selected == "Paper":
        your_score += 1

    else:
        computer_score += 1

    your_score_label.config(text = "Your Score: " + str(your_score))
    computer_score_label.config(text = "Computer Score: " + str(computer_score))

#Rock Button
rock_button = Button(root, text = "Rock",height = 0, width = 11,command= rock)
rock_button.place(x = 160, y = 110)
rock_button["bg"] = "#FFE2E8"

#Paper Button
paper_button = Button(root, text = "Paper", height = 0,width = 12,command= paper)
paper_button.place(x = 265, y = 110)
paper_button["bg"] = "#b6b6b6"

#scissors button
scissor_button = Button(root, text = "Scissors", height = 0, width = 12,command= scissors)
scissor_button.place(x = 375, y = 110)
scissor_button["bg"] = "#ccdfff"

#your score label
your_score_label = Label(root,text= "Your Score: " + str(your_score))
your_score_label["bg"] = "#d9d9d9"
your_score_label.place(x = 350, y = 175)

#computer score label 
computer_score_label = Label(root, text = "Computer Score: " + str(computer_score))
computer_score_label["bg"] = "#d9d9d9"
computer_score_label.place(x = 370, y = 215)

root.mainloop()