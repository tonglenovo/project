import tkinter as tk
from function import *
from tkinter import *
from tkinter import messagebox
from pandasgui import show

master = tk.Tk()
master.title('Hotel Selection: Reviews')
master.geometry("550x300")
master.iconbitmap("art/logo1.ico")

# finalReviews = finalList()
reviewsList = loadReviewsList()
hotelCheckBox = []
starCheckBox = []
cleaningSelection = []

def rating(): #This is to check which variables are ticked(True), then Select the data
   ratingChoice = []
   for rating in starCheckBox:
      value = rating.get()
      if value:
         ratingChoice.append(int(value))
   return ratingChoice

def hotel(): #This is to check which variables are ticked(True), then select the data based on input
   hotelChoice = []
   for hotel in hotelCheckBox:
         value = hotel.get()
         if value:
            hotelChoice.append(value)
   return hotelChoice

def cleanOption():
   cleanChoice = []
   for filtering in cleaningSelection:
      value = filtering.get()
      if value:
         cleanChoice.append(value)
   return cleanChoice

def dataCleaning():
   dataCleanList = {}
   cleanChoiceOption = cleanOption()
   print(cleanChoiceOption)
   if (len(cleanChoiceOption)==0):
      print("Is empty")
      dataCleanList = reviewsList
   else:
      print("Not empty")
   for clean in cleanChoiceOption:
      if(clean=='1'):
         if(len(dataCleanList) == 0):
            dataCleanList = filterEmptyList(reviewsList,False)
         else:
            dataCleanList = filterEmptyList(dataCleanList,False)
      elif(clean=='2'):
         print("Trigger")
         if(len(dataCleanList) == 0):
            dataCleanList = languageDetect(reviewsList)
         else:
            dataCleanList = languageDetect(dataCleanList)
   return dataCleanList

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

def wordmap():
   finalReviews = dataCleaning()
   if (checkEmpty()):
      hotelChoice = hotel()
      ratingChoice = rating()
      wordCloud(finalReviews, hotelChoice,ratingChoice)

def combined():
   finalReviews = dataCleaning()
   hotelChoice = hotel()
   ratingChoice = rating()
   result = reviewsByHotelAndRate(finalReviews,hotelChoice,ratingChoice)
   if(checkEmpty()):
         dataFrame = pd.DataFrame.from_dict(result)
         #print(dataFrame)
         show(dataFrame)
         master.geometry("550x300")

def keywords():
   finalReviews = dataCleaning()
   keyword = entry.get() #make the entry a variable
   if(checkEmpty()):
      keyword = keyword.strip()
      print(len(keyword))
      if (len(keyword) == 0):
         messagebox.showerror('Error','Please input keyword')
      else:
         hotelChoice = hotel()
         ratingChoice = rating()
         result = reviewsByHotelAndRate(finalReviews,hotelChoice,ratingChoice)
         searchResult = searchByKeyword(result,keyword.lower())
         dataFrame = pd.DataFrame.from_dict(searchResult)
         show(dataFrame)
         master.geometry("550x200")

def chart():
   finalReviews = dataCleaning()
   print(len(finalReviews['reviews']))
   keyword = entry.get()
   if(checkEmpty()):
      
      hotelChoice = hotel()
      ratingChoice = rating()
      displayChart(finalReviews,hotelChoice,ratingChoice,keyword)

def clear():
   for rating in starCheckBox:
      rating.set(0)
   for hotel in hotelCheckBox:
      hotel.set(0)
   for filtering in cleaningSelection:
      filtering.set(0)
   
   entry.delete('0', END)

# def selectAllHotel():
#    for i in hotelCheckBox:
#       i.set('1')
# #This section is for the ratings
# Label(master, text="Select the rating(s) you wish to see").grid(row=0)

# Label(master, text="Select the Hotel(s)").place(x=0,y=60)
# for i in range(9):
#     option = StringVar(value="")
#     hotelCheckBox.append(option)
# Checkbutton(master, text='Fort Canning', variable=hotelCheckBox[0], onvalue="Hotel Fort Canning", offvalue="").place(x=0,y=80)
# Checkbutton(master, text='Four Seasons', variable=hotelCheckBox[1], onvalue="Four Seasons Hotel", offvalue="").place(x=100,y=80)
# Checkbutton(master, text='JW Marriott', variable=hotelCheckBox[2], onvalue="JW Marriott Hotel", offvalue="").place(x=200,y=80)
# Checkbutton(master, text='Mandarin Oriental', variable=hotelCheckBox[3], onvalue="Mandarin Oriental", offvalue="").place(x=300,y=80)
# Checkbutton(master, text='Marina Bay Sands', variable=hotelCheckBox[4], onvalue="Marina Bay Sands Hotel", offvalue="").place(x=430,y=80)
# Checkbutton(master, text='Pan Pacific', variable=hotelCheckBox[5], onvalue="Pan Pacific Hotel", offvalue="").place(x=0,y=100)
# Checkbutton(master, text='Ritz Carlton', variable=hotelCheckBox[6], onvalue="Ritz-Carlton Hotel", offvalue="").place(x=100,y=100)
# Checkbutton(master, text='Shangri-La', variable=hotelCheckBox[7], onvalue="Shangri-La Singapore", offvalue="").place(x=200,y=100)
# Checkbutton(master, text='The Fullerton', variable=hotelCheckBox[8], onvalue="The Fullerton Hotel", offvalue="").place(x=300,y=100)

# Label(master, text="Select data cleaning").place(x=0,y=140)
# for i in range(3):
#     option = StringVar(value="")
#     cleaningSelection.append(option)
# Checkbutton(master, text='Empty', variable=cleaningSelection[0], onvalue="1", offvalue="").place(x=0,y=160)
# Checkbutton(master, text='Special Characther', variable=cleaningSelection[1], onvalue="2", offvalue="").place(x=100,y=160)
# Checkbutton(master, text='Contain negative keyword', variable=cleaningSelection[2], onvalue="3", offvalue="").place(x=250,y=160)


# label = tk.Label(text='Enter keyword:')
# label.place(x=10, y=201)
# input = tk.Label() #Entry field
# entry = tk.Entry()
# entry.place(x=100, y=203)
# entry.bind('<Return>', lambda _: keywords()) ##So that the enter key will perform the keyword search

# Button(master, text='Keyword search',command=keywords).place(x=110, y=230)#calls upon function var_states
# Button(master, text='Reviews', command=combined).place(x=250, y=203)#calls upon function var_states
# Button(master, text='Wordmap', command=wordmap).place(x=320, y=203) #calls upon function var_states
# Button(master, text="Chart",command=chart).place(x=400,y=203)#calls upon function var_states
# Button(master, text="Clear all", command=clear).place(x=440, y=270)
# Button(master, text='Quit', command=master.quit).place(x=500,y=270) #Quit the application

#This section is for the ratings
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
    hotelCheckBox.append(option)#y=160
Checkbutton(master, text='Fort Canning', variable=hotelCheckBox[0], onvalue="Hotel Fort Canning", offvalue="").place(x=0,y=140)
Checkbutton(master, text='Four Seasons', variable=hotelCheckBox[1], onvalue="Four Seasons Hotel", offvalue="").place(x=100,y=140)
Checkbutton(master, text='JW Marriott', variable=hotelCheckBox[2], onvalue="JW Marriott Hotel", offvalue="").place(x=200,y=140)
Checkbutton(master, text='Mandarin Oriental', variable=hotelCheckBox[3], onvalue="Mandarin Oriental", offvalue="").place(x=300,y=140)
Checkbutton(master, text='Marina Bay Sands', variable=hotelCheckBox[4], onvalue="Marina Bay Sands Hotel", offvalue="").place(x=430,y=140)
Checkbutton(master, text='Pan Pacific', variable=hotelCheckBox[5], onvalue="Pan Pacific Hotel", offvalue="").place(x=0,y=160)
Checkbutton(master, text='Ritz Carlton', variable=hotelCheckBox[6], onvalue="Ritz-Carlton Hotel", offvalue="").place(x=100,y=160)
Checkbutton(master, text='Shangri-La', variable=hotelCheckBox[7], onvalue="Shangri-La Singapore", offvalue="").place(x=200,y=160)
Checkbutton(master, text='The Fullerton', variable=hotelCheckBox[8], onvalue="The Fullerton Hotel", offvalue="").place(x=300,y=160)

#Button(master, text='Select all Hotel(s)', command=selectAllHotel).place(x=0,y=190) #Quit the application

label = tk.Label(text='Enter keyword:')
label.place(x=10, y=201)
input = tk.Label() #Entry field
entry = tk.Entry()
entry.place(x=100, y=203)
entry.bind('<Return>', lambda _: keywords()) ##So that the enter key will perform the keyword search

Button(master, text='Keyword search',command=keywords).place(x=110, y=230)#calls upon function var_states
Button(master, text='Reviews', command=combined).place(x=250, y=203)#calls upon function var_states
Button(master, text='Wordmap', command=wordmap).place(x=320, y=203) #calls upon function var_states
Button(master, text="Chart",command=chart).place(x=400,y=203)#calls upon function var_states
Button(master, text="Clear all", command=clear).place(x=440, y=270)
Button(master, text='Quit', command=master.quit).place(x=500,y=270) #Quit the application
mainloop()