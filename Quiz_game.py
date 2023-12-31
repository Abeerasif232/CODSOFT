from tkinter import *

question_no = 0
options_list = []
end_button_list = []
button_1 = None
score = 0

dic = {
    "questions": [
        "Who is the CEO of TESLA?",
        "Who is the CEO of Meta?",
        "Which planet is known as \"Red Planet\" ?",
        "Who was the first person to step foot on the Moon?"
    ],
    "choices": [
        ["Elon Musk", "Mark Zuckerberg", "Shahid Anwar"],
        ["Elon Musk", "Mark Zuckerberg", "Shahid Anwar"],
        ["Venus", "Mars", "Jupiter"],
        ["Neil Armstrong", "Buzz Aldrin", "Michael Collins"]
    ],
    "answers": [1, 2, 2, 1]
}

length = len(dic["questions"])


def Page1():
    global question_no, score
    question_no, score = 0, 0

    for i in end_button_list:
        i.destroy()

    canvas.create_rectangle(50, 140, 850, 600, fill="RoyalBlue4")
    canvas.create_text(450, 170, text="Introduction",
                       fill="white", font=("Arial", 30))
    canvas.create_text(
        450, 230,
        text="Welcome to the ultimate quiz challenge where your knowledge\n will be put to the test and only the sharpest minds will prevail!",
        fill="black",
        font=("Arial", 20)
    )
    canvas.create_text(130, 300, text="Rules:",
                       fill="white", font=("Arial", 30))
    canvas.create_text(
        300, 420,
        text="1. One question will be asked once.\n\n2. Only select one option at once.\n\n3. You can play multiple times.",
        fill="black",
        font=("Arial", 20)
    )

    global button_1
    button_1 = Button(
        canvas, text='>', height=1, width=1, bg="RoyalBlue4", fg="white", font=("Arial", 50), borderwidth=0, command=NEXT
    )
    button_1.place(x=780, y=470)


def NEXT():
    global button_1
    button_1.destroy()

    global question_no
    canvas.create_rectangle(50, 140, 850, 600, fill="RoyalBlue4")
    question_no += 1
    if question_no > len(dic["questions"]):
        End()
        return 0
    Question(question_no)


def Question(question_no):
    canvas.create_text(
        200, 200, text=f"Question {question_no}/{length}:", fill="White", font=("Arial", 30))
    canvas.create_text(
        450, 250, text=dic["questions"][question_no - 1], fill="White", font=("Arial", 20))
    if question_no <= length:
        options(question_no)


def options(question_no):
    option_1 = Button(
        canvas, text=dic["choices"][question_no - 1][0], height=1, width=18, bg="RoyalBlue4", fg="white",
        font=("Arial", 20), borderwidth=8, highlightbackground="grey",
        command=lambda: Update_score(question_no - 1, 1)
    )
    option_1.place(x=100, y=300)
    option_2 = Button(
        canvas, text=dic["choices"][question_no - 1][1], height=1, width=18, bg="RoyalBlue4", fg="white",
        font=("Arial", 20), borderwidth=8, highlightbackground="grey",
        command=lambda: Update_score(question_no - 1, 2)
    )
    option_2.place(x=100, y=400)
    option_3 = Button(
        canvas, text=dic["choices"][question_no - 1][2], height=1, width=18, bg="RoyalBlue4", fg="white",
        font=("Arial", 20), borderwidth=8, highlightbackground="grey",
        command=lambda: Update_score(question_no - 1, 3)
    )
    option_3.place(x=100, y=500)
    options_list.append(option_1)
    options_list.append(option_2)
    options_list.append(option_3)


def Update_score(x, y):
    global score
    if dic["answers"][x] == y:
        score += 1
    NEXT()


def End():
    for i in options_list:
        i.destroy()
    canvas.create_rectangle(50, 140, 850, 600, fill="grey")
    canvas.create_text(
        450, 220, text=f"You Scored {score} out of {length}", fill="black", font=("Arial", 40))
    canvas.create_text(450, 350, text="You want to play again?",
                       fill="black", font=("Arial", 30, UNDERLINE))
    YES = Button(
        canvas, text="YES", height=1, width=5, bg="grey", fg="black",
        font=("Arial", 20), borderwidth=0, command=Page1
    )
    YES.place(x=200, y=450)
    NO = Button(
        canvas, text="NO", height=1, width=5, bg="grey", fg="black",
        font=("Arial", 20), borderwidth=0, command=exit
    )
    NO.place(x=600, y=450)
    end_button_list.append(YES)
    end_button_list.append(NO)


win = Tk()
win.geometry("900x700")
win.title("Quiz Game")

canvas = Canvas(win, width=900, height=700, bg="black")
canvas.create_text(450, 70, text="Quiz Game", fill="white", font=("Arial", 40))
canvas.create_rectangle(650, 40, 250, 100, outline="white", width=2)

canvas.pack()

Page1()

win.mainloop()
