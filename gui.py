#!/usr/bin/python3
from tkinter import *
root = Tk()

root.geometry('722x400')
root.title('Spoof Email Sender by Padsala Tushal')


'''
Label(root, text="Welcome to Harry Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

'''
Label(root, text='Spoof Email Sender' , font='comicsansms 33 bold',pady=15, padx=225).grid(row=0, column=0)



#Text for our form
sender_name = Label(root, text='Sender Name')
sender_email = Label(root, text='Sender Email')
subject = Label(root, text='Subject')
reciever_email = Label(root, text='Reciever Email')
message = Label(root, text='Message') 

'''

'''
#Pack text for our form
sender_name.grid(row=1 , column=2)
sender_email.grid(row=2, column=2)
subject.grid(row=3, column=2)
reciever_email.grid(row=4, column=2)
message.grid(row=5, column=2)

'''
# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

'''




root.mainloop()
