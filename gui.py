#!/usr/bin/python3
from tkinter import *
import requests
root = Tk()

root.geometry('500x400')
root.minsize(450,300)
# root.maxsize(700, 400)

root.title('Spoof Email Sender by Padsala Tushal')

Label(root, text='Spoof Email Sender' , font='comicsansms 33 bold').grid(row=0,column=2)

#Text for our form
sender_name = Label(root, text='Sender Name').grid(row=1,column=1)
sender_email = Label(root, text='Sender Email').grid(row=2, column=1)
subject = Label(root, text='Subject').grid(row=3, column=1)
reciever_email = Label(root, text='Reciever Email').grid(row=4, column=1)
message = Label(root, text='Message').grid(row=5, column=1)

#Tkinter variable for storing entries
sender_name_value = StringVar()
sender_email_value = StringVar()
subject_value = StringVar()
reciever_email_value = StringVar()
message_value = StringVar()


#Entries for our form
sender_name_entry = Entry(root, textvariable=sender_name_value).grid(row=1,column=2,pady=5,ipadx=70)
sender_email_entry = Entry(root, textvariable=sender_email_value).grid(row=2, column=2,pady=5,ipadx=70)
subject_entry = Entry(root, textvariable=subject_value).grid(row=3, column=2,pady=5,ipadx=70)
reciever_email_entry = Entry(root, textvariable=reciever_email_value).grid(row=4, column=2,pady=5,ipadx=70)
message_entry = Entry(root, textvariable=message_value).grid(row=5, column=2,pady=5,ipadx=70,ipady=30)

'''
def getvals():
	print(sender_name_value.get())
	print(sender_email_value.get())
	print(subject_value.get())
	print(reciever_email_value.get())
	print(message_value.get())
	print(type(sender_email_value.get()))
'''

def sendmail():
	url = "http://devilishere666.000webhostapp.com/mailer.php"
	
	#header of request analasis from burp with making request from website
	headers = {
		'Host': 'devilishere666.000webhostapp.com',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'en,en-US;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Content-Length': '121',
		'Origin': 'http://devilishere666.000webhostapp.com',
		'Connection': 'close',
		'Referer': 'http://devilishere666.000webhostapp.com/index.html',
		'Cookie': '_ga=GA1.2.1953321504.1637271960',
		'Upgrade-Insecure-Requests': '1',
	}

	#data for making request
	data = {
		's_name': sender_name_value.get(),
		's_email': sender_email_value.get(),
		'subject': subject_value.get(),
		'r_email': reciever_email_value.get(),
		'message': message_value.get(),
	}
	
	r = requests.post(url, headers=headers, data=data, allow_redirects=True)
	print(r.status_code)


Button(text='Send', command=sendmail, bg='brown', fg='white', font=('helvetica', 9, 'bold')).grid(row=6 , column=2)

root.mainloop()
