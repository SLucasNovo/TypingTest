# TYPING TEST APPLICATION

# imports
from tkinter import *
from nltk.corpus import words
import nltk
import random


# <---------------------- APPLICATION -------------------->

nltk.download('words')
word_list = words.words()
wordings = []
points = 0
seconds = 60
timer = None
index = 9
all_inputs = []


def get_current_inputs():
    text = word_input.get()
    word_input += text
    return text


def calculate_points(inputs, word_dictionary):
    global points
    wrong_list = []
    for i, j in zip(word_dictionary, inputs):
        if i == j:
            points += len(i)
        elif i != j:
            wrong_list.append(i)
    return wrong_list


def create_words():
    global word_input, wordings, seconds, word_label1, word_label2, word_label3

    wordings = [random.choice(word_list).lower() for i in range(0, 100)]

    # Labels
    word_label1 = Label(text=wordings[:9], font=('Arial', 10))
    word_label1.grid(column=1, row=2, padx=20, pady=(30,0))
    word_label2 = Label(text=wordings[9:16], font=('Arial', 10))
    word_label2.grid(column=1, row=3, padx=20, )
    word_label3 = Label(text=wordings[16:25], font=('Arial', 10))
    word_label3.grid(column=1, row=4, padx=20, )

    below_label = Label(text='type below', font=('Arial', 10))
    below_label.grid(column=1, row=5, padx=20, pady=30)

    title.config(text='Start typing')

    # Entry
    word_input = Entry(width=100)
    word_input.grid(column=1, row=6, padx=20, pady=10)

    button_start.destroy()
    button_start2 = Button(text='Exit', highlightthickness=0, font=('Arial', 14), command=terminate)
    button_start2.grid(column=2, row=2)

    timer_countdown(seconds)


def refresh_labels():
    global index
    word_input.delete(0, 'end')
    index += 9
    word_label1.config(text=wordings[index-9:index], font=('Arial', 10))
    word_label2.config(text=wordings[index:index + 7], font=('Arial', 10))
    word_label3.config(text=wordings[index+7:index+15], font=('Arial', 10))


def timer_countdown(seconds):
    global index, word_label1, word_label2, word_label3, all_inputs

    canvas.itemconfig(canvas_timer, text=f'{seconds}')
    if seconds > 0:
        global timer
        timer = window.after(1000, timer_countdown, seconds-1)
        entries = word_input.get()
        entries_list = entries.split(' ')
        if len(entries_list) > 10:
            all_inputs += entries_list
            refresh_labels()

    else:
        words_wrong = calculate_points(all_inputs, wordings)
        word_label1.config(text=f"You have written: {len(all_inputs)} words."
                                f" Words you got wrong: {','.join(words_wrong)}. "
                                f"You have accomplished a total of {(round(points,0))} WPM", font=('Arial', 15))
        word_label2.destroy()
        word_label3.destroy()





def terminate():
    window.destroy()


# <---------------------- UI SETUP -------------------->


# Add an image , title , button , start
# Create point based

window = Tk()
window.title('Typing Test')
window.minsize(width=900, height=600)
window.config(padx=50, pady=50)


canvas = Canvas(width=150, height=150, highlightthickness=0)
# image = PhotoImage(file='Keyboard img.png')
# canvas.create_image(100,100, image=image)
# canvas.grid(column=1, row=1)
canvas_timer = canvas.create_text(102, 130, text=seconds, fill='white', font=('Arial', 35, "bold"))
canvas.grid(column=1, row=1)


# Label

title = Label(text='Welcome to the Typing Test, you have 60 seconds to type the most words you can', font=('Arial', 20))
title.grid(column=1, row=0, pady=50, padx=50)


# Button

button_start = Button(text='Start test', highlightthickness=0, font=('Arial', 14), command=create_words)
button_start.grid(column=2, row=1)




window.mainloop()