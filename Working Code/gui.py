# Title: Identification Of Images using CBIR with Keras

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
import cv2

#load the trained model to classify the images

from keras.models import load_model
model = load_model('model.h5')

#dictionary to label all the CIFAR-10 dataset classes.

classes = { 
    0:'Aeroplane',
    1:'Automobile',
    2:'Bird',
    3:'Cat',
    4:'Deer',
    5:'Dog',
    6:'Frog',
    7:'Horse',
    8:'Ship',
    9:'Truck' 
}
#initialise GUI

top=tk.Tk()
top.geometry('800x600')
top.title('Identification Of Images using CBIR with Keras')
top.configure(background='#0b021f')
label=Label(top,background='#0b021f', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = cv2.imread(file_path)
    image = cv2.resize(image,(32,32))
    image = numpy.expand_dims(image, axis=0)
    predictions = model.predict(image)[0]
    # print(predictions)
    predictions = list(predictions)
    pred_val = max(predictions)
    pred = predictions.index(pred_val)
    sign = classes[pred]
    print(sign)
    # result 
    label.configure(foreground='#dff046', text=sign, font=('Open Sans',20,'bold')) 

# Classify Buttton
def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",
    command=lambda: classify(file_path),padx=12,pady=7)
    #classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.configure(background='#22069c', foreground='white',font=('arial',12,'bold'))
    classify_b.place(relx=0.74,rely=0.53)

# Upload Button
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),
        (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an Image",command=upload_image,padx=10,pady=5)

upload.configure(background='#22069c', foreground='white',font=('arial',12,'bold'))

# Title Labelling
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Identification Of Images using CBIR with Keras",pady=30, font=('arial',20,'bold'))

heading.configure(background='#0b021f',foreground='#39de18')
heading.pack()
top.mainloop()