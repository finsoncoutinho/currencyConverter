
from forex_python.converter import CurrencyRates 
from tkinter import *  
from tkinter import messagebox

# Create a GUI window 
root = Tk()

#Title of GUI window
root.title('CURRENCY CONVERTER')
#title on main window

#background colour of GUI window 
root.configure(background = "#F6E3C5") 

#configuration of GUI window (WidthxHeight)
root.geometry("800x200")

# Function to perform real time conversion
# from one currency to another currency
def RealTimeCurrencyConverter():

    c= CurrencyRates()
#to check if user used dropdown or Input box
    if(From.get()=="Select" and To.get()=="Select"):
      #if the entered currency is valid or not
        if (fromEntry.get() not in options or toEntry.get() not in options):
          messagebox.showerror("error","Invalid currency")
          clear_all()
        else:
          #if valid then take values from Entry
          from_currency=fromEntry.get() #get from currency
          to_currency=toEntry.get() #get to currency                 
    else:
      #user used dropdown so get those values
       from_currency=From.get() #get from currency
       to_currency=To.get() #get to currency

    am=amount.get() #get amount to convert

    #pass the from_currency, to_currency & am to convert function 
    #forex-python make API calls to "https://ratesapi.io/" for realtime currency rates
    #then returns the Amount in to_currency
    result= c.convert(from_currency,to_currency, float(am))
    result=round(float(result),4)

    result2 = c.convert(from_currency, from_currency, 1.0)
    result3 = c.convert(from_currency, to_currency, 1.0)
    result3=round(float(result3),4)

    #inserts converted amount in conv_amt Entry
    #0 denotes entry index
    conv_amt.insert(0, str(result))
    fromLable.insert(0, str(result2))
    toLable.insert(0, str(result3))
    
  


#delets amount in conv_amt & amount Entry 
#reset From & To 
def clear_all(): 
  amount.delete(0, END) 
  conv_amt.delete(0, END)
  From.set( "Select" )
  To.set( "Select" )
  fromEntry.delete(0, END) 
  toEntry.delete(0, END) 
  fromLable.delete(0, END) 
  toLable.delete(0, END) 


# Create a "Amount :" label  only text
#w = Label ( master, option, … )  syntax
amount_lable=Label(root, text = 'AMOUNT: ' , bg = "#4CACBC", font=('calibre',10, 'bold'))

# Create a Amount Entry   input
#entry = tk.Entry(parent, options)  syntax
amount = Entry(root,font=('calibre',10,'normal'))


# Dropdown menu options
options = ["INR","USD","EUR","CAD","IDR","BGN","ILS","GBP","DKK","JPY","HUF","RON","MYR","SEK","SGD","HKD","AUD","CHF","KRW","CNY","TRY","HRK","NZD","THB","NOK","RUB","MXN","CZK","BRL","PLN","PHP","ZAR"]
#options = ["INR","USD","EUR","CAD","JPY","SGD","HKD","AUD","KRW","CNY","NZD","THB","RUB","MXN","BRL"]
  
#Header text Label
head_lable=Label(root, text = ' REAL TIME CURRENCY CONVERTER ', bg = "#6CC4A1" , font=('calibre',10, 'bold'))

currencyrate_lable=Label(root, text = ' CURRENCY RATES: ', bg = "#6CC4A1" , font=('calibre',10, 'bold'))

# create  variables 
#currency names
From = StringVar() 
To = StringVar()
  
# initialise the variables
#first shown as selct in dropdown then choose it gets changed
From.set( "Select" )  
To.set( "Select" )
  
# Create a "From: " label 
from_lable=Label(root, text = 'FROM: ', bg = "#4CACBC" , font=('calibre',10, 'bold'))

# Create a "To: " label 
to_lable=Label(root, text = 'TO: ' , bg = "#4CACBC", font=('calibre',10, 'bold'))

# create a drop down menu using OptionMenu function/class
# which takes window name, variable and choices as
# an argument.
# use * before the name of the list to unpack the values
#root=window name
drop1 = OptionMenu( root , From , *options )
drop2 = OptionMenu( root , To , *options )

fromEntry = Entry(root,font=('calibre',10,'normal'))
toEntry = Entry(root,font=('calibre',10,'normal'))

fromLable=Entry(root,font=('calibre',10,'normal'))
toLable=Entry(root,font=('calibre',10,'normal'))

# Create button, to convert Amount from_currency to to_currency
button = Button( root , text = "Convert" , bg="#A0D995",command = RealTimeCurrencyConverter )

# Create a "Converted Amount :" label
Conv_lable=Label(root, text = 'CONVERTED AMOUNT: ' , bg = "#4CACBC", font=('calibre',10, 'bold'))

# Create Entry for "Converted Amount" 
conv_amt = Entry(root,font=('calibre',10,'normal'))

# Create a Clear Button
reset = Button(root, text = "Clear", command = clear_all)


# grid method is used for placing 
# the widgets at respective positions 
# in table like structure.  
head_lable.grid(row=0,column=1)
amount_lable.grid(row=2,column=0)
from_lable.grid(row=3,column=0)
to_lable.grid(row=4,column=0)
Conv_lable.grid(row=6,column=0)

amount.grid(row = 2, column = 1, ipadx ="25")
drop1.grid(row = 3, column = 1, ipadx = "10")
fromEntry.grid(row=3,column=2,ipadx="10")
fromLable.grid(row=3,column=3,ipadx="10")
currencyrate_lable.grid(row=2,column=3,ipadx="10")
drop2.grid(row = 4, column = 1, ipadx = "10")
toEntry.grid(row=4,column=2,ipadx="10")
toLable.grid(row=4,column=3,ipadx="10")
button.grid(row = 5, column = 1)
conv_amt.grid(row = 6, column = 1, ipadx ="25")
reset.grid(row = 7, column = 1)
 
# Start the GUI 
root.mainloop() 
