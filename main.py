import csv
import tkinter as tk
from function import *
from tkinter import *
master = Tk()
master.title('Hotel Selection: Reviews')
master.geometry("500x200")

#load data from csv
combinedReviews = loadReviewsList()
#remove empty inside the data
clearEmptyList = filterEmptyList(combinedReviews,False)
#remove reviews that contain negative keyword
sortBadKeywordOut = havingBadWordList(clearEmptyList,False)

#def var_states(): #for reference only
   #print("Star rating 5: %d,\nStar rating 4: %d, \nStar rating 3: %d, \nStar rating 2: %d,\nStar rating 1: %d"% (var1.get(), var2.get(),var3.get(),var4.get(),var5.get()))

def rating(): #This is to check which variables are ticked(True), then Select the data
   List1 = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]
   for i in List1:
      if i ==1:
         print('Testing: Selected data R')
      else:
         print('Testing: not selected R')
   return List1

def hotel(): #This is to check which variables are ticked(True), then select the data based on input
   List2 = [var6.get(), var7.get(), var8.get(), var9.get(), var10.get()]
   for i in List2:
      if i == 1:
         print('Testing: Selected data H')
      else:
         print('Testing: nothing to see here H')
   return List2

def wordmap(): #redundant, must be a better way to do this
   List2 = [var6.get(), var7.get(), var8.get(), var9.get(), var10.get()]
   for i in List2:
      if i == 1:
         print('testing: make wordmap')
      else:
         print('Testing: nothing to see here')

def combined():
    #listName use sortBadKeywordOut as It filter the empty response and negative keyword.
    #hotelName is base on the check box Hotel A, Hotel B, Hotel C
    #Rate is base on the check box 5 Star, 4 Star, 3 Star
    #reviewsByHotelAndRate(listName,hotelName,Rate):
   print(hotel()+rating()) #PLACEHOLDER ONLY!
   #Here, it should filter to hotels already selected
   for i in rating(): #This is to see which ratings were selected
      if i ==1:
         print(i) #if the rating is selected, it should pull out the corresponding rating of the hotel.
      else: 
         print('nothing')

#This section is for the ratings
Label(master, text="Select the rating(s) you wish to see").grid(row=0)
var1 = IntVar()
Checkbutton(master, text="5 Stars", variable=var1).place(x=0,y=20)
var2 = IntVar()
Checkbutton(master, text="4 Stars", variable=var2).place(x=100, y=20)
var3 = IntVar()
Checkbutton(master, text="3 Stars", variable=var3).place(x=200,y=20)
var4 = IntVar()
Checkbutton(master, text="2 Stars", variable=var4).place(x=300,y=20)
var5 = IntVar()
Checkbutton(master, text="1 Star", variable=var5).place(x=400,y=20)

Label(master, text="Select the Hotel(s)").place(x=0,y=60)
var6 = IntVar()
Checkbutton(master, text="Hotel A", variable=var6).place(x=0,y=80)
var7 = IntVar()
Checkbutton(master, text="Hotel B", variable=var7).place(x=100, y=80)
var8 = IntVar()
Checkbutton(master, text="Hotel C", variable=var8).place(x=200,y=80)
var9 = IntVar()
Checkbutton(master, text="Hotel D", variable=var9).place(x=300,y=80)
var10 = IntVar()
Checkbutton(master, text="Hotel E", variable=var10).place(x=400,y=80)

Button(master, text='Reviews', command=combined).place(x=150, y=120)#calls upon function var_states
Button(master, text='Wordmap', command=wordmap).place(x=220, y=120) #calls upon function var_states
Button(master, text='Quit', command=master.quit).place(x=300,y=120) #Quit the application
mainloop()
#Note: You can use either 1/True or 0/False for these conditions.
#if var1.get()==True:
#   print('ok')
#else:
#    print('nah')