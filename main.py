import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils


stream = cv2.VideoCapture("clip.mp4")
def play(speed):
    print('clicked on next: speed is',speed)

    frame1= stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    frame = imutils.resize(frame,width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    canvas.create_text(135,29, fill='green', font='Times 25 italic bold', text='decision Pending' )

def pending(decision):
    frame = cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)

    time.sleep(1)
    if decision == 'out':
        decisionImg = 'out.png'
    else:
        decisionImg = 'not_out.png'

    frame = cv2.cvtColor(cv2.imread("sponsor.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)

    time.sleep(1)
    if decision == 'out':
        decisionImg = 'out.png'
    else:
        decisionImg = 'not_out.png'

    frame = cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)

    
    pass

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is NOT out")


SET_WIDTH = 650
SET_HEIGHT = 368

window = tkinter.Tk()
window.title("CodewithNikhil")
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH,height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()


btn = tkinter.Button(window,text= "<< Previous(fast)",width=50 , command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window,text= "<< Previous(slow)",width=50 , command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window,text= "< next(fast) >>",width=50 , command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window,text= " next(slow) >>",width=50 , command=partial
(play, 2))
btn.pack()

btn = tkinter.Button(window,text= " Give Out",width=50, command=out)
btn.pack()

btn = tkinter.Button(window,text= " Give not Out",width=50, command=not_out)
btn.pack()


window.mainloop()
