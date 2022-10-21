import tkinter as tk
from function import *
from tkinter import *
from tkinter import messagebox
from pandasgui import show

master = tk.Tk()
master.title('Hotel Selection: Reviews')
master.geometry("550x300")
master.iconbitmap("art/logo1.ico")

reviewsList = loadReviewsList()
hotelCheckBox = []
starCheckBox = []
cleaningSelection = []

"""
This is to check which Rating are selected(True), then return the selected data based on input(GUI)
"""
def rating(): 
   ratingChoice = []
   for rating in starCheckBox:
      value = rating.get()
      if value:
         ratingChoice.append(int(value))
   return ratingChoice

"""
This is to check which Hotel are selected(True), then return the selected data based on input(GUI)
"""
def hotel(): 
   hotelChoice = []
   for hotel in hotelCheckBox:
         value = hotel.get()
         if value:
            hotelChoice.append(value)
   return hotelChoice

"""
This is to check which data cleaning are selected(True), then return the selected data based on input(GUI)
"""
def cleanOption():
   cleanChoice = []
   for filtering in cleaningSelection:
      value = filtering.get()
      if value:
         cleanChoice.append(value)
   return cleanChoice

"""
This is to get the option base on input(GUI) and return the list of data cleaning
"""
def dataCleaning():
   dataCleanList = {}
   cleanChoiceOption = cleanOption()
   if (len(cleanChoiceOption)==0):
      dataCleanList = reviewsList
   for clean in cleanChoiceOption:
      if(clean=='1'):
         if(len(dataCleanList) == 0):
            dataCleanList = filterEmptyList(reviewsList,False)
         else:
            dataCleanList = filterEmptyList(dataCleanList,False)
      elif(clean=='2'):
         if(len(dataCleanList) == 0):
            dataCleanList = languageDetect(reviewsList)
         else:
            dataCleanList = languageDetect(dataCleanList)
   return dataCleanList

"""
This is to check any empty input (Checkbox for rating and hotel) to prevent getting error
and show an output(error message) to let the user know what they are require to input
in order to not get the error message out.
"""
def checkEmpty():
   state = False
   if(len(hotel()) == 0 and len(rating()) == 0):
      messagebox.showerror('Error',"Please select a rating and a hotel")
   elif(len(rating()) == 0):
      messagebox.showerror('Error',"Please select a rating")
   elif(len(hotel()) == 0):
      messagebox.showerror('Error',"Please select a hotel")
   else:
      state = True
   return state

"""
This is function of the button on display wordmap
"""
def wordmap():
   finalReviews = dataCleaning()
   if (checkEmpty()):
      hotelChoice = hotel()
      ratingChoice = rating()
      wordCloud(finalReviews, hotelChoice,ratingChoice)

"""
This is function of the button on display reviews
"""
def combined():
   finalReviews = dataCleaning()
   hotelChoice = hotel()
   ratingChoice = rating()
   result = reviewsByHotelAndRate(finalReviews,hotelChoice,ratingChoice)
   if(checkEmpty()):
         dataFrame = pd.DataFrame.from_dict(result)
         show(dataFrame)
         master.geometry("550x300")

"""
This is function of the button base on keyword and display reviews,wordmap and chart
"""
def keywords():
   finalReviews = dataCleaning()
   keyword = entry.get()
   if(checkEmpty()):
      keyword = keyword.strip()
      if (len(keyword) == 0):
         messagebox.showerror('Error','Please input keyword')
      else:
         hotelChoice = hotel()
         ratingChoice = rating()
         result = reviewsByHotelAndRate(finalReviews,hotelChoice,ratingChoice)
         searchResult = searchByKeyword(result,keyword.lower())
         dataFrame = pd.DataFrame.from_dict(searchResult)
         show(dataFrame)
         master.geometry("550x300")

"""
This is function of the button on display the chart
"""
def chart():
   finalReviews = dataCleaning()
   keyword = entry.get()
   if(checkEmpty()):
      hotelChoice = hotel()
      ratingChoice = rating()
      displayChart(finalReviews,hotelChoice,ratingChoice,keyword)

"""
This is function of the button on clearing all the input in the GUI
"""
def clear():
   for rating in starCheckBox:
      rating.set(0)
   for hotel in hotelCheckBox:
      hotel.set(0)
   for filtering in cleaningSelection:
      filtering.set(0)
   
   entry.delete('0', END)


Label(master, text="Select data that you want to filter out").grid(row=0)
for i in range(2):
    option = StringVar(value="")
    cleaningSelection.append(option)
Checkbutton(master, text='Empty', variable=cleaningSelection[0], onvalue="1", offvalue="").place(x=0,y=20)
Checkbutton(master, text='Only English', variable=cleaningSelection[1], onvalue="2", offvalue="").place(x=100,y=20)

Label(master, text="Select the rating(s) you wish to see").place(x=0,y=60)
for i in range(5):
    option = StringVar(value="")
    starCheckBox.append(option)
Checkbutton(master, text='5 Stars',variable=starCheckBox[0], onvalue="5", offvalue="").place(x=0,y=80)
Checkbutton(master, text='4 Stars',variable=starCheckBox[1], onvalue="4", offvalue="").place(x=100,y=80)
Checkbutton(master, text='3 Stars',variable=starCheckBox[2], onvalue="3", offvalue="").place(x=200,y=80)
Checkbutton(master, text='2 Stars',variable=starCheckBox[3], onvalue="2", offvalue="").place(x=300,y=80)
Checkbutton(master, text='1 Stars',variable=starCheckBox[4], onvalue="1", offvalue="").place(x=400,y=80)

Label(master, text="Select the Hotel(s)").place(x=0,y=120)
for i in range(9):
    option = StringVar(value="")
    hotelCheckBox.append(option)
Checkbutton(master, text='Fort Canning', variable=hotelCheckBox[0], onvalue="Hotel Fort Canning", offvalue="").place(x=0,y=140)
Checkbutton(master, text='Four Seasons', variable=hotelCheckBox[1], onvalue="Four Seasons Hotel", offvalue="").place(x=100,y=140)
Checkbutton(master, text='JW Marriott', variable=hotelCheckBox[2], onvalue="JW Marriott Hotel", offvalue="").place(x=200,y=140)
Checkbutton(master, text='Mandarin Oriental', variable=hotelCheckBox[3], onvalue="Mandarin Oriental", offvalue="").place(x=300,y=140)
Checkbutton(master, text='Marina Bay Sands', variable=hotelCheckBox[4], onvalue="Marina Bay Sands Hotel", offvalue="").place(x=430,y=140)
Checkbutton(master, text='Pan Pacific', variable=hotelCheckBox[5], onvalue="Pan Pacific Hotel", offvalue="").place(x=0,y=160)
Checkbutton(master, text='Ritz Carlton', variable=hotelCheckBox[6], onvalue="Ritz-Carlton Hotel", offvalue="").place(x=100,y=160)
Checkbutton(master, text='Shangri-La', variable=hotelCheckBox[7], onvalue="Shangri-La Singapore", offvalue="").place(x=200,y=160)
Checkbutton(master, text='The Fullerton', variable=hotelCheckBox[8], onvalue="The Fullerton Hotel", offvalue="").place(x=300,y=160)

label = tk.Label(text='Enter keyword:')
label.place(x=10, y=201)
input = tk.Label() 
entry = tk.Entry()
entry.place(x=100, y=203)
entry.bind('<Return>', lambda _: keywords()) 

Button(master, text='Keyword search',command=keywords).place(x=110, y=230)
Button(master, text='Reviews', command=combined).place(x=250, y=203)
Button(master, text='Wordmap', command=wordmap).place(x=320, y=203) 
Button(master, text="Chart",command=chart).place(x=400,y=203)
Button(master, text="Clear all", command=clear).place(x=440, y=270)
Button(master, text='Quit', command=master.quit).place(x=500,y=270) 

mainloop()