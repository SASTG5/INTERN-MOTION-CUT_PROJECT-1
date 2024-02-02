#by SASHANG UMANATH S
#on 1.2.2024
#for MOTION CUT INTERN
####################################################   QUIZ APP(TKINTER)   #########################################################

#####################################################      code start     ###########################################################
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk
from PIL import Image

#define question dictionary
question = {
    "Which is the Capital City of Andhra Pradesh": ['Sriram City', 'Hyderabad', 'Vishakapthinam', 'Amaravati'],
    "How many Lok Sabha seats in India": ['345', '124', '543','534'],
    "Which is parent comany of Google": ['Abcde', 'Meta', 'Cadabra', 'Alphabet']
}
qn=list(question.keys())
tot=len(question)

#define answer list
global ans 
ans= ['Amaravati', '543', 'Alphabet']
 
global current_question
current_question=0
correct=0
wrong=0

#start app
def start_quiz():
    start_button.forget()
    q_screen()
    next_qn()
    
#display question    
def disp_qn():
    ques=('Question '+str(current_question+1)+':'+( qn[current_question]))
    Label(win,text= ques,width=42,font=("ariel",12," bold"),relief=FLAT,padx=10, 
          pady=9,bg='gold',borderwidth=0).place(x=98,y=78)
    q_in=Entry(win,textvariable=user_ans,width=56,font=("ariel",11," bold"),
               relief=FLAT,bg='blue',fg='white')
    q_in.place(x=98,y=113)
    q_in.bind("<FocusIn>")
    #user_ans.set(q_in.get())
    print(user_ans.get())

def next_qn():
    global current_question
    x=0
    if (x<tot):
        disp_qn()
        radio_button_a()
        radio_button_b()
        radio_button_c()
        radio_button_d()
        check_ans()
        current_question+=1
        x+=1
        print(x)
        if x==tot-1:
            nxt_button.destroy()
        
#for checking answer
def check_ans():
    global user_score,correct
    temp_ans = user_ans.get()
    crt_ans=ans[current_question-1]
    if (temp_ans != 'None' and temp_ans ==crt_ans):
        user_score.set(user_score.get()+1)
        correct+=1

#display result window
def disp_res():
    global correct,wrong
    check_ans()
    mb.showinfo(title='result',message=('RESULT: '+str(user_score.get())+
                                        '\n\nCorrect: '+str(correct)+'\nWrong: '+str(tot-correct)))
    if user_score.get()==tot:
        mb.showinfo(title='congratulations',message=('CONGRATULATIONS\n You got a full Score'))
    

def disp_correct():
    win3=Tk()
    win3.title('window 3')
    win3.geometry('632x360')
    win3.minsize(632,360)
    win3.configure(bg='gold')
    ypos=48
    global user_score,correct,ans,current_question
    temp_ans = user_ans.get()
    us_ans=('Your answer\n'+temp_ans)
    t=Label(win3,text=us_ans,width=52,font=("ariel",10," bold"),relief=FLAT,padx=10, 
          pady=9,bg='gold',borderwidth=0)
    t.place(x=98,y=ypos)
    
    crt_ans=ans[current_question-1]
    
    if temp_ans==crt_ans:
        crt=('!!WELL DONE!!\n\nCorrect answer\n'+(crt_ans))
        Label(win3,text=crt ,width=52,font=("ariel",10," bold"),relief=FLAT,padx=10, 
          pady=9,bg='gold',borderwidth=0).place(x=98,y=ypos+40)
    else:
        wrg=('??DID U KNOW??\n\nWRONG ANSWER\n\nCorrect answer\n'+(crt_ans))
        Label(win3,text=wrg ,width=52,font=("ariel",10," bold"),relief=FLAT,padx=10, 
          pady=9,bg='gold',borderwidth=0).place(x=98,y=ypos+40)
    win3.after(3000,lambda:win3.destroy())

##display question screen after start    
def q_screen():
    back=Label(win,image=bg,compound=CENTER)
    back.place(x=0,y=0)
    
    disp_qn()
    radio_button_a()
    radio_button_b()
    radio_button_c()
    radio_button_d()
    
    win.wm_attributes('-transparentcolor')
    #next button
    nxt_button=Button(win, text="Next",command=lambda:[disp_correct(),next_qn()],relief=RIDGE,width=4,
                      height=1,bg="blue",fg="white",font=("ariel",10,"bold"))
    nxt_button.place(x=296,y=320)
    #quit button
    quit_button = Button(win, text="Quit", command=win.destroy,width=4,bg="blue", 
                         fg="white",font=("ariel",10," bold"))
    quit_button.place(x=30,y=320)
    #submit button
    submit_button=Button(win,text='Submit',command=lambda:[disp_res(),win.after(2000,lambda:win.destroy())],relief=RIDGE,bg='blue',
                         fg='white',width=5,font=("ariel",10,"bold"))
    submit_button.place(x=560,y=320)
    
#defining option buttons a,b,c,d
def radio_button_a():
    c_question = list(question.keys())[current_question]
    op=question[c_question]  
    radio_btn =  Radiobutton(win, padx=28,bg='gold',fg='black',font=("ariel",10,"bold"),
                             width=10,text=op[0],variable=user_ans,value=op[0],indicator=0)
    radio_btn.place(x = 100, y = 195)

def radio_button_b():
    c_question = list(question.keys())[current_question]
    op=question[c_question]
    radio_btn =  Radiobutton(win, padx=28,bg='gold',fg='black',font=("ariel",10,"bold"),
                             width=10,text=op[1],variable=user_ans,value=op[1],indicator=0)
    radio_btn.place(x = 400, y = 195)


def radio_button_c():
    c_question = list(question.keys())[current_question]
    op=question[c_question]   
    radio_btn =  Radiobutton(win, padx=28,bg='gold',fg='black',font=("ariel",10,"bold"),
                             width=10,text=op[2],variable=user_ans,value=op[2],indicator=0)
    radio_btn.place(x = 100, y = 265)

def radio_button_d():
    c_question = list(question.keys())[current_question]
    op=question[c_question]
    radio_btn =  Radiobutton(win, padx=28,bg='gold',fg='black',font=("ariel",10,"bold"),
                             width=10,text=op[3],variable=user_ans,value=op[3],indicator=0)
    radio_btn.place(x = 400, y = 265)
#defing option buttons end

#designing gui
if __name__ == "__main__":
    #setup main window
    win=Tk()
    win.title('window')
    win.geometry('632x360')
    win.minsize(632,360)

    img=(Image.open('D:\INTERNSHIP\MOTION CUT\ima.jpg'))
    resized_image= img.resize((632,360),Image.ANTIALIAS)
    bg= ImageTk.PhotoImage(resized_image)
    
    img_main=(Image.open('D:\INTERNSHIP\MOTION CUT\main.jpg'))
    resized_image_main= img_main.resize((632,360),Image.ANTIALIAS)
    bg_main= ImageTk.PhotoImage(resized_image_main)

    f= Frame(win,width=631,height=360)
    f.pack(fill=X)

    f1= Frame(win,width=631,height=360)
    f1.pack(fill=X)

    back_main=Label(f,image=bg_main,compound=CENTER)
    back_main.place(x=0,y=0)

    title=Label(win,text='by SASHANG UMANATH S',width=52,font=("ariel",10," bold"),relief=FLAT,padx=10, 
          pady=9,bg='blue',fg='white',borderwidth=0)
    title.place(x=98,y=28)

    start_button=Button(f, text="Start",command=start_quiz,relief=RIDGE,width=4,
                      height=1,bg="blue",fg="white",font=("ariel",10,"bold"))
    start_button.place(x=296,y=290)

    user_ans = StringVar()
    user_ans.set('')
    user_score = IntVar()
    user_score.set(0)
    print(user_score.get())
 
    win.mainloop()
#####################################################     code end     ###########################################################
