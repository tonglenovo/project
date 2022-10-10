import csv
import tkinter as tk
from function import *
from tkinter import *
from pandasgui import show

master = Tk()
master.title('Hotel Selection: Reviews')
master.geometry("500x200")

#load data from csv
combinedReviews = loadReviewsList()
#remove empty inside the data
clearEmptyList = filterEmptyList(combinedReviews,False)
#remove reviews that contain negative keyword
sortBadKeywordOut = havingBadWordList(clearEmptyList,False)

#Store checkbox selected value
hotelCheckBox = []
starCheckBox = []

#def var_states(): #for reference only
   #print("Star rating 5: %d,\nStar rating 4: %d, \nStar rating 3: %d, \nStar rating 2: %d,\nStar rating 1: %d"% (var1.get(), var2.get(),var3.get(),var4.get(),var5.get()))

def rating(): #This is to check which variables are ticked(True), then Select the data
   ratingChoice = []
   for i in starCheckBox:
      value = i.get()
      if value:
         ratingChoice.append(int(value))
   return ratingChoice

def hotel(): #This is to check which variables are ticked(True), then select the data based on input
   hotelChoice = []
   for var in hotelCheckBox:
        value = var.get()
        if value:
            hotelChoice.append(value)
   return hotelChoice

def wordmap(): #redundant, must be a better way to do this
   List2 = [var6.get(), var7.get(), var8.get(), var9.get(), var10.get()]
   for i in List2:
      if i == 1:
         print('testing: make wordmap')
      else:
         print('Testing: nothing to see here')

def combined():
   # Hotel selection
   hotelChoice = hotel()
   # Rate selection
   ratingChoice = rating()
    #listName use sortBadKeywordOut as It filter the empty response and negative keyword.
    #hotelName is base on the check box Hotel A, Hotel B, Hotel C
    #Rate is base on the check box 5 Star, 4 Star, 3 Star
   result = reviewsByHotelAndRate(sortBadKeywordOut,hotelChoice,ratingChoice)
   
    #result['reviews'] to get all the reviews after filter the condition that is selected

   # print(hotel()+rating()) #PLACEHOLDER ONLY!
   # #Here, it should filter to hotels already selected
   # for i in rating(): #This is to see which ratings were selected
   #    if i ==1:
   #       print(i) #if the rating is selected, it should pull out the corresponding rating of the hotel.
   #    else: 
   #       print('nothing')

def chart():
    hotelChoice = hotel()
    ratingChoice = rating()
    sortByHotelName(sortBadKeywordOut,hotelChoice,ratingChoice)
#    a = reviewsByHotelAndRate(sortBadKeywordOut,hotelChoice,ratingChoice)
#    print(len(a['hotel']))

#This section is for the ratings
Label(master, text="Select the rating(s) you wish to see").grid(row=0)
for i in range(5):
    option = StringVar(value="")
    starCheckBox.append(option)
Checkbutton(master, text='5 Stars',variable=starCheckBox[0], onvalue="5", offvalue="").place(x=0,y=20)
Checkbutton(master, text='4 Stars',variable=starCheckBox[1], onvalue="4", offvalue="").place(x=100,y=20)
Checkbutton(master, text='3 Stars',variable=starCheckBox[2], onvalue="3", offvalue="").place(x=200,y=20)
Checkbutton(master, text='2 Stars',variable=starCheckBox[3], onvalue="2", offvalue="").place(x=300,y=20)
Checkbutton(master, text='1 Stars',variable=starCheckBox[4], onvalue="1", offvalue="").place(x=400,y=20)


Label(master, text="Select the Hotel(s)").place(x=0,y=60)
for i in range(5):
    option = StringVar(value="")
    hotelCheckBox.append(option)
Checkbutton(master, text='Pan Pacific Hotel',variable=hotelCheckBox[0], onvalue="Pan Pacific Hotel", offvalue="").place(x=0,y=80)
Checkbutton(master, text='Hotel B',variable=hotelCheckBox[1], onvalue="Hotel B", offvalue="").place(x=150,y=80)
Checkbutton(master, text='Hotel C',variable=hotelCheckBox[2], onvalue="Hotel C", offvalue="").place(x=250,y=80)
Checkbutton(master, text='Hotel D',variable=hotelCheckBox[3], onvalue="Hotel D", offvalue="").place(x=350,y=80)
Checkbutton(master, text='MBS', variable=hotelCheckBox[4], onvalue="Marina Bay Sands Hotel", offvalue="").place(x=0,y=100)

Button(master, text='Reviews', command=combined).place(x=150, y=160)#calls upon function var_states
Button(master, text='Wordmap', command=wordmap).place(x=220, y=160) #calls upon function var_states
Button(master, text='Chart', command=chart).place(x=310, y=160) #calls upon function var_states
Button(master, text='Quit', command=master.quit).place(x=380,y=160) #Quit the application
mainloop()
#Note: You can use either 1/True or 0/False for these conditions.
#if var1.get()==True:
#   print('ok')
#else:
#    print('nah')