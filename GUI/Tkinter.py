from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=200 , height=100)
#Entry  grid

entry = Entry(width=10)

entry.grid(column=1,row=0)


#LABEL place

my_label = Label(text="I am a label", font=("Arial",10,"bold"))


my_label['text'] = 'new text'
my_label.config(text = 'Miles ')
my_label.grid(column=2,row=0) 


my_label1 = Label(text="I am a label", font=("Arial",10,"bold"))
my_label1['text'] = 'new text'
my_label1.config(text = 'is equal to ')
my_label1.grid(column=0,row=1)


my_label2 = Label(text="I am a label", font=("Arial",10,"bold"))
my_label2['text'] = 'new text'
my_label2.config(text = ' ')
my_label2.grid(column=1,row=1) 

my_label3 = Label(text="I am a label", font=("Arial",10,"bold"))
my_label3['text'] = 'new text'
my_label3.config(text = "km")
my_label3.grid(column=2,row=1) 

#BUTTON   pack
def Calculate():
    miles = float(entry.get())
    km = miles * 1.609
    my_label2.config(text = f"{km}" )

#calls action() when pressed
button = Button(text="Calculate", command= Calculate)
button.grid(column=1,row=2)

window.mainloop()   
