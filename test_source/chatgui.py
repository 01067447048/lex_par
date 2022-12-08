
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))


def xx3t523qs(xcvwesr):
    xcvwe3r = nltk.word_tokenize(xcvwesr)
    xcvwe3r = [lemmatizer.lemmatize(word.lower()) for word in xcvwe3r]
    return xcvwe3r

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def xcf3x(vvv32, xd35, show_details=True):
    # tokenize the pattern
    cvxv = xx3t523qs(vvv32)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(xd35)
    for s in cvxv:
        for i,w in enumerate(xd35):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def xcv3(yyys3x, model):
    # filter out predictions below a threshold
    xxcwr = xcf3x(yyys3x, words, show_details=False)
    xe3 = model.predict(np.array([xxcwr]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(xe3) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    lrtecv = []
    for r in results:
        lrtecv.append({"intent": classes[r[0]], "probability": str(r[1])})
    return lrtecv

def yywerx235xgghje(vvewr5, vx35sdsdf):
    tag = vvewr5[0]['intent']
    sdf = vx35sdsdf['intents']
    for i in sdf:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def yyw235x(msg):
    ints = xcv3(msg, model)
    res = yywerx235xgghje(ints, intents)
    return res


#Creating GUI with tkinter
import tkinter
from tkinter import *


def uyerqu26():
    twt35 = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if twt35 != '':
        xx3wswsswf3e333.config(state=NORMAL)
        xx3wswsswf3e333.insert(END, "You: " + twt35 + '\n\n')
        xx3wswsswf3e333.config(foreground="#442265", font=("Verdana", 12))

        res = yyw235x(twt35)
        xx3wswsswf3e333.insert(END, "Bot: " + res + '\n\n')

        xx3wswsswf3e333.config(state=DISABLED)
        xx3wswsswf3e333.yview(END)


yrx = Tk()
yrx.title("Hello")
yrx.geometry("400x500")
yrx.resizable(width=FALSE, height=FALSE)

#Create Chat window
xx3wswsswf3e333 = Text(yrx, bd=0, bg="white", height="8", width="50", font="Arial", )

xx3wswsswf3e333.config(state=DISABLED)

#Bind scrollbar to Chat window
wnuw = Scrollbar(yrx, command=xx3wswsswf3e333.yview, cursor="heart")
xx3wswsswf3e333['yscrollcommand'] = wnuw.set

#Create Button to send message
oeity34 = Button(yrx, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                 bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff',
                 command= uyerqu26)

#Create the box to enter message
EntryBox = Text(yrx, bd=0, bg="white", width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
wnuw.place(x=376, y=6, height=386)
xx3wswsswf3e333.place(x=6, y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
oeity34.place(x=6, y=401, height=90)

yrx.mainloop()
