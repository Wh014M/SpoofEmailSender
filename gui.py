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
sender_name = Label(root, text='Sender Name').grid(row=1 , column=2)
sender_email = Label(root, text='Sender Email').grid(row=2, column=2)
subject = Label(root, text='Subject').grid(row=3, column=2)
reciever_email = Label(root, text='Reciever Email').grid(row=4, column=2)
message = Label(root, text='Message').grid(row=5, column=2)


#Tkinter variable for storing entries
sender_name_value = StringVar()
sender_email_value = StringVar()
subject_value = StringVar()
reciever_email_value = StringVar()
message_value = StringVar()

#Entries for our form
sender_name_entry = Entry(root, textvariable='sender_name_value').grid(row=1, column=3)
sender_email_entry = Entry(root, textvariable='sender_email_value').grid(row=2, column=3)
subject_entry = Entry(root, textvariable='subject_value').grid(row=3, column=3)
reciever_email_entry = Entry(root, textvariable='reciever_email_value').grid(row=4, column=3)
message_entry = Entry(root, textvariable='message_value').grid(row=5, column=3)




root.mainloop()
