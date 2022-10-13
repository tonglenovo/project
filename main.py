import tkinter as tk
from function import *
from tkinter import *
from tkinter import messagebox
from pandasgui import show

master = tk.Tk()
master.title('Hotel Selection: Reviews')
master.resizable(0, 0)
master.geometry("550x200")

finalReviews = finalList()
hotelCheckBox = []
starCheckBox = []

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
#    list2 = [var6.get(), var7.get(), var8.get(), var9.get(), var10.get(),var11.get(),var12.get(),var13.get(),var14.get()]
#    for i in list2:
#       if i == 1:
#          print('testing: make wordmap')
#       else:
#          print('Testing: no wordmap')
#    window2 = Toplevel()  # this creates the window
#    window2.title('Wordmap')
#    window2.geometry("400x100")
#    label2 = tk.Label(window2,text='Wordmap')
#    label2.place(x=10, y=10)
   if (checkEmpty()):
      hotelChoice = hotel()
      ratingChoice = rating()
      wordCloud(finalReviews, hotelChoice,ratingChoice)

def combined():
   # list2 = [var6.get(), var7.get(), var8.get(), var9.get(), var10.get(),var11.get(),var12.get(),var13.get(),var14.get()]
   # hotellist1 = []
   # for i in list2:
   #    if i == 1:
   #       hotellist1.append(1)
   #    else:
   #       hotellist1.append(0)

   # list1 = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]
   # ratinglist1 = []
   # for j in list1:
   #    if j ==1:
   #       ratinglist1.append(1)
   #    else:
   #       ratinglist1.append(0)

   # for i in hotellist1:
   #    if i ==1:
   #          for k in ratinglist1:
   #             if k ==1:
   #                print(i,k)
   #             else:
   #                print('Rating not Selected')
   #    else:
   #       print('Hotel Not Selected')

   # window1 = Toplevel()  # this creates the window
   # window1.title('Hotel Reviews')
   # window1.geometry("400x100")
   # label1 = tk.Label(window1, text='hotel reviews')  # window1 prevents overwriting into primary window
   # label1.place(x=10, y=10)
   keyword = entry.get() #make the entry a variable
   hotelChoice = hotel()
   ratingChoice = rating()
   result = reviewsByHotelAndRate(finalReviews,hotelChoice,ratingChoice)
   if(checkEmpty()):
         df = pd.DataFrame.from_dict(result)
         print(df)
         show(df)

def keywords():
   keyword = entry.get() #make the entry a variable
   if(checkEmpty()):
      if (keyword == ''):
         messagebox.showerror('Error','Please input keyword')
   
      else:
         hotelChoice = hotel()
         ratingChoice = rating()
         result = reviewsByHotelAndRate(finalReviews,hotelChoice,ratingChoice)
         searchResult = searchByKeyword(result,keyword.lower())
         df = pd.DataFrame.from_dict(searchResult)
         show(df)
      
   # keyword = entry.get() #make the entry a variable
   # window3 = Toplevel()  # this creates the window
   # window3.title('Keyword Map')
   # window3.geometry("400x100")
   # label3 = tk.Label(window3, text=keyword) #so whatever is entered will appear
   # label3.place(x=10, y=10)

def chart():
   # With keyword version
   keyword = entry.get() #make the entry a variable
   # if(checkEmpty()):
   #    hotelChoice = hotel()
   #    ratingChoice = rating()
    
   #          # print(value)
   #    sortByHotelName(finalReviews,hotelChoice,ratingChoice,keyword)
   if(checkEmpty()):
      hotelChoice = hotel()
      ratingChoice = rating()
      displayChart(finalReviews,hotelChoice,ratingChoice,keyword)



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

# var1 = IntVar()
# Checkbutton(master, text="5 Stars", variable=var1).place(x=0,y=20)
# var2 = IntVar()
# Checkbutton(master, text="4 Stars", variable=var2).place(x=100, y=20)
# var3 = IntVar()
# Checkbutton(master, text="3 Stars", variable=var3).place(x=200,y=20)
# var4 = IntVar()
# Checkbutton(master, text="2 Stars", variable=var4).place(x=300,y=20)
# var5 = IntVar()
# Checkbutton(master, text="1 Star", variable=var5).place(x=400,y=20)

Label(master, text="Select the Hotel(s)").place(x=0,y=60)
for i in range(9):
    option = StringVar(value="")
    hotelCheckBox.append(option)
Checkbutton(master, text='MBS', variable=hotelCheckBox[0], onvalue="Marina Bay Sands Hotel", offvalue="").place(x=0,y=80)
Checkbutton(master, text='Pan Pacific', variable=hotelCheckBox[1], onvalue="Pan Pacific Hotel", offvalue="").place(x=100,y=80)
Checkbutton(master, text='Mandarin Oriental', variable=hotelCheckBox[2], onvalue="Mandarin Oriental", offvalue="").place(x=200,y=80)
Checkbutton(master, text='Hotel Fort Canning', variable=hotelCheckBox[3], onvalue="Hotel Fort Canning", offvalue="").place(x=300,y=80)
Checkbutton(master, text='JW Marriott', variable=hotelCheckBox[4], onvalue="JW Marriott Hotel", offvalue="").place(x=430,y=80)
Checkbutton(master, text='Shangri-La', variable=hotelCheckBox[5], onvalue="Shangri-La Singapore", offvalue="").place(x=0,y=100)
Checkbutton(master, text='The Fullerton', variable=hotelCheckBox[6], onvalue="The Fullerton Hotel", offvalue="").place(x=100,y=100)
Checkbutton(master, text='Ritz Carlton', variable=hotelCheckBox[7], onvalue="Ritz-Carlton Hotel", offvalue="").place(x=200,y=100)
Checkbutton(master, text='Four Seasons', variable=hotelCheckBox[8], onvalue="Four Seasons Hotel", offvalue="").place(x=300,y=100)
# var6 = IntVar()
# Checkbutton(master, text="MBS", variable=var6).place(x=0,y=80)
# var7 = IntVar()
# Checkbutton(master, text="Pan Pacific", variable=var7).place(x=100, y=80)
# var8 = IntVar()
# Checkbutton(master, text="Mandarin Oriental", variable=var8).place(x=200,y=80)
# var9 = IntVar()
# Checkbutton(master, text="Hotel Fort Canning", variable=var9).place(x=300,y=80)
# var10 = IntVar()
# Checkbutton(master, text="JW Marriott", variable=var10).place(x=430,y=80)
# var11 = IntVar()
# Checkbutton(master, text="Shangri-La", variable=var11).place(x=0,y=100)
# var12 = IntVar()
# Checkbutton(master, text="The Fullerton", variable=var12).place(x=100,y=100)
# var13 = IntVar()
# Checkbutton(master, text="Ritz Carlton", variable=var13).place(x=200,y=100)
# var14 = IntVar()
# Checkbutton(master, text="Four Seasons", variable=var14).place(x=300,y=100)

label = tk.Label(text='Enter keyword:')
label.place(x=10, y=141)
input = tk.Label() #Entry field
entry = tk.Entry()
entry.place(x=100, y=143)
entry.bind('<Return>', lambda _: keywords()) ##So that the enter key will perform the keyword search

Button(master, text='Keyword search',command=keywords).place(x=110, y=170)#calls upon function var_states
Button(master, text='Reviews', command=combined).place(x=300, y=140)#calls upon function var_states
Button(master, text='Wordmap', command=wordmap).place(x=370, y=140) #calls upon function var_states
Button(master, text="Chart",command=chart).place(x=450,y=140)#calls upon function var_states
Button(master, text='Quit', command=master.quit).place(x=500,y=140) #Quit the application
mainloop()