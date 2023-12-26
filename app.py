from tkinter import *
from tkinter import messagebox
from timeit import default_timer
import random
import difflib


window=Tk()
window.geometry('850x530')
window.title('Speed Tester')

words=['''Throwing yet another wad of paper into the trash,
trying to create a character.ADRIENAdrien wasn't conventionally
 beautiful.But there was something about her.Maybe herwits or 
 her signature kicks,something just stood out.Unbrokeneven with
 a past laced with grief,Adrien was me.

So this a typing speed game made by Mine,It gives you text to 
types,checks your speed and also corrects your errors,you see 
Mine has to finsh her 10 days of code in 2023.

 ''',
 '''This is another paragraph to test your typing spped.Avoid 
 destractions a nd typr fast ,that way you will be able to do 
 better in such short time.So the next time sombody you a siminly 
 insurmoontable projct ,What you should do is try to break it  
  down into pasts.Do not start I repeat do not start working one
   one aspect , whan you do not have an Idea of the entire project
    and how parts are interconnected.'''  ]


word = random.choice(words)
def Started():
    word = random.choice(words)
    start.config(text='next')
    content.config(text=word)

def Result():
    global word
    global text
    global starttime

    string=f'{text.get(1.0,END)}'

    end=default_timer()

    time=round(end-starttime,2)


    speed=round(len(word.split())*60/time,2)

    accuracy=difflib.SequenceMatcher(None,word,string).ratio()
    accuracy=str(round(accuracy*100))
    print(accuracy)

    message=f'Time= {time}seconds, Speed = {speed}wpm ,Acurracy= {accuracy}%'

    messagebox.showinfo('Result',message)

def Exit():
    window.destroy()



welcome=Label(window,text='Welcome To Speed Tester',font=('ariel',10))
welcome.place(x=625,y=30)

content=Label(window,font=('ariel',13),bd=0)
content.place(x=10,y=10)

text=Text(window,height=14,width=58,bd=0,font=('ariel',13))
text.place(x=30,y=250)


start=Button(window,text='start',bg='#D2F59F',bd=0,command=Started)
start.place(x=602,y=410)

result=Button(window,text='result',bg='#D2F59F',bd=0,command=Result)
result.place(x=602,y=350)

exit=Button(window,text='exit',bg='#D2F59F',bd=0,command=Exit)
exit.place(x=602,y=475)

starttime=default_timer()



mainloop()