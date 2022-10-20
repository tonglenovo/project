"""
pip install textwrap
pip install pandas
pip install matplotlib
pip install numpy
pip install wordcloud
pip install collections
pip install re
pip install nltk
pip install emoji
pip install langdetect
pip install pandasgui
pip install tkinter
python -m nltk.downloader stopwords
"""
import csv
from textwrap import wrap
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud,STOPWORDS
from collections import Counter
import re
from nltk.corpus import stopwords
from langdetect import  detect_langs
import emoji

commonword = set(stopwords.words('english'))
hotel_name = ['Pan Pacific Hotel','Marina Bay Sands Hotel','Mandarin Oriental','Hotel Fort Canning','JW Marriott Hotel','Shangri-La Singapore','The Fullerton Hotel','Ritz-Carlton Hotel','Four Seasons Hotel']
reviews = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
checkingEmpty = ['none','na','n/a','nil','-','nothing']
badKeyword = ['bad','dirty','no','not','empty','boring','raining','small','unusual','slanted',"don't",'dislike','unfair','unfriendly','rude','terrible','overpriced','awful','overcrowded','crowded','expensive']

"""
This function readCSV file and add to review dictionary list.
fileName: the file name of the CSV
hotelName: the hotelName that going to set on the review dictionary list to know the data is from which hotel
state: since they are 2 different data format of CSV so it is better I use state to determind the CSV is from Yi Tong or Ivriah.
"""
def readCSV(fileName,hotelName,state):
    file_name=open('csv/'+fileName+'.csv','r',encoding='utf-8', errors='ignore')
    file = csv.DictReader(file_name)
    if state == 1:
        for col in file:
            reviewText = col['positive'] +" "+ col['negative']
            reviews['reviews'].append(reviewText)
            reviews['hotel'].append(hotelName)
            score = float(col['score'])/2
            reviews['score'].append(int(round(score,2)))
            date = col['date'].split()
            reviews['date'].append(date[1])
            reviews['country'].append(col['country'])
            reviews['room'].append(col['room'])
            reviews['title'].append(col['\ufefftitle'])
            reviews['travellerType'].append(col['travellerType'])
        return reviews
    else:
        for col in file:
            date = col['date'].split()
            reviews['reviews'].append(col['Review'])
            reviews['hotel'].append(hotelName)
            rating = float(col['Rating'])
            reviews['score'].append(int(round(rating,2)))
            reviews['title'].append(col['Review title'])
            if(len(date) == 0):
                reviews['date'].append('')
            else:
                reviews['date'].append(date[1])
            reviews['country'].append('')
            reviews['room'].append('')
            reviews['travellerType'].append(col['traveller_type'])
        return reviews

"""
This function will readCSV, load all data into reviews dict and 
return the dict list that all is appended.
"""
def loadReviewsList():
    # Yi Tong data crawlers
    readCSV('mbs','Marina Bay Sands Hotel',1)
    readCSV('pan','Pan Pacific Hotel',1)
    readCSV('mandarin_oriental','Mandarin Oriental',1)
    readCSV('hotel_fort_canning','Hotel Fort Canning',1)
    readCSV('jw_marriott_hotel','JW Marriott Hotel',1)
    readCSV('shangri_la','Shangri-La Singapore',1)
    readCSV('the_fullerton_hotel','The Fullerton Hotel',1)
    readCSV('the_ritz_carlton','Ritz-Carlton Hotel',1)
    # Ivriah data crawlers 
    readCSV('Marina_Bay_Sands_hotel_reviews','Marina Bay Sands Hotel',0)
    readCSV('Pan_Pacific_Singapore_hotel_reviews','Pan Pacific Hotel',0)
    readCSV('Mandarin_Oriental_Singapore_hotel_reviews','Mandarin Oriental',0)
    readCSV('Hotel_Fort_Canning_hotel_reviews','Hotel Fort Canning',0)
    readCSV('JW_Marriott_Hotel_Singapore_South_Beach_hotel_reviews','JW Marriott Hotel',0)
    readCSV('Shangri_La_Singapore_hotel_reviews','Shangri-La Singapore',0)
    readCSV('The_Fullerton_Bay_Hotel_Singapore_hotel_reviews','The Fullerton Hotel',0)
    readCSV('The_Ritz_Carlton_Millenia_Singapore_hotel_reviews','Ritz-Carlton Hotel',0)
    readCSV('Four_Seasons_Hotel_Singapore_hotel_reviews','Four Seasons Hotel',0)
    return reviews

"""
This function will remove all the empty string, no comment, nil and ETC
state True is getEmpty data, state False will get data that clear empty
combineList: The list that user want to filter empty list or take out the empty list.
state: True will return data with empty value, False will return data with take out the empty list.
"""
def filterEmptyList(combineList,state):
    filterEmptyList = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    afterFilterEmptyList = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    for reviewsIndex in range(0,len(combineList['reviews'])):
        lowCaseList = combineList['reviews'][reviewsIndex].lower()
        if any(word in lowCaseList for word in checkingEmpty) or (len(lowCaseList) == 1):
            filterEmptyList['reviews'].append(combineList['reviews'][reviewsIndex])
            filterEmptyList['score'].append(combineList['score'][reviewsIndex])
            filterEmptyList['hotel'].append(combineList['hotel'][reviewsIndex])
            filterEmptyList['title'].append(combineList['title'][reviewsIndex])
            filterEmptyList['date'].append(combineList['date'][reviewsIndex])
            filterEmptyList['country'].append(combineList['country'][reviewsIndex])
            filterEmptyList['room'].append(combineList['room'][reviewsIndex])
            filterEmptyList['travellerType'].append(combineList['travellerType'][reviewsIndex])
        else:
            afterFilterEmptyList['reviews'].append(combineList['reviews'][reviewsIndex])
            afterFilterEmptyList['score'].append(combineList['score'][reviewsIndex])
            afterFilterEmptyList['hotel'].append(combineList['hotel'][reviewsIndex])
            afterFilterEmptyList['title'].append(combineList['title'][reviewsIndex])
            afterFilterEmptyList['date'].append(combineList['date'][reviewsIndex])
            afterFilterEmptyList['country'].append(combineList['country'][reviewsIndex])
            afterFilterEmptyList['room'].append(combineList['room'][reviewsIndex])
            afterFilterEmptyList['travellerType'].append(combineList['travellerType'][reviewsIndex])
    if state == True:
        return filterEmptyList
    else:
        return afterFilterEmptyList

"""
This function will count each hotel have how many reviews.
Example: {'Marina Bay Sands Hotel': 976, 'Pan Pacific Hotel': 320}
list: the list that user want to count
"""
def countList(list):
    dfEmptyList = {}
    for hotelIndex in range(0,len(list['hotel'])):
        for hotelNameIndex in hotel_name:
            if(list['hotel'][hotelIndex] == hotelNameIndex):
                if(hotelNameIndex not in dfEmptyList):
                    dfEmptyList[hotelNameIndex]=1
                else:
                    dfEmptyList[hotelNameIndex]+=1
    return dfEmptyList


"""
This function will return dictionary list of 1* review, 2* review and so on.
list: the list that want to separate to 1*,2* reviews
num: the rating that user want.
"""
def number_of_star(list,num):
    reviews_list = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    
    for scoreIndex in range(0,len(list['score'])):
        roundedScore = int(list['score'][scoreIndex])
        if num == 1:
            if(roundedScore<num+1):
                reviews_list['reviews'].append(list['reviews'][scoreIndex])
                reviews_list['score'].append(list['score'][scoreIndex])
                reviews_list['hotel'].append(list['hotel'][scoreIndex])
                reviews_list['title'].append(list['title'][scoreIndex])
                reviews_list['date'].append(list['date'][scoreIndex])
                reviews_list['country'].append(list['country'][scoreIndex])
                reviews_list['room'].append(list['room'][scoreIndex])
                reviews_list['travellerType'].append(list['travellerType'][scoreIndex])
        elif roundedScore == num:
            reviews_list['reviews'].append(list['reviews'][scoreIndex])
            reviews_list['score'].append(list['score'][scoreIndex])
            reviews_list['hotel'].append(list['hotel'][scoreIndex])
            reviews_list['title'].append(list['title'][scoreIndex])
            reviews_list['date'].append(list['date'][scoreIndex])
            reviews_list['country'].append(list['country'][scoreIndex])
            reviews_list['room'].append(list['room'][scoreIndex])
            reviews_list['travellerType'].append(list['travellerType'][scoreIndex])
    return reviews_list

"""
This function will return dictionary list of the hotel that the GUI had selected.
listName: the list that wish to be filter base on the hotel name
hotelName: hotel selected by GUI
"""
def getHotelChoice(listName,hotelName):
    getHotel = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    for hotelIndex in range(0,len(listName['hotel'])):
        for hotelNameIndex in range(0,len(hotelName)):
            if(listName['hotel'][hotelIndex] == hotelName[hotelNameIndex]):
                getHotel['reviews'].append(listName['reviews'][hotelIndex])
                getHotel['score'].append(listName['score'][hotelIndex])
                getHotel['hotel'].append(listName['hotel'][hotelIndex])
                getHotel['date'].append(listName['date'][hotelIndex])
                getHotel['country'].append(listName['country'][hotelIndex])
                getHotel['room'].append(listName['room'][hotelIndex])
                getHotel['title'].append(listName['title'][hotelIndex])
                getHotel['travellerType'].append(listName['travellerType'][hotelIndex])
    return getHotel

"""
This function will getHotelChoice() first then find the rating and 
return the result as a new dictionary list
"""
def reviewsByHotelAndRate(listName,hotelName,rate):
    gethotelList = getHotelChoice(listName,hotelName)
    rateReview = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    for rating in rate:
        ratingList = number_of_star(gethotelList,rating)
        for scoreIndex in range(0,len(ratingList['score'])):
            rateReview['reviews'].append(ratingList['reviews'][scoreIndex])
            rateReview['score'].append(ratingList['score'][scoreIndex])
            rateReview['hotel'].append(ratingList['hotel'][scoreIndex])
            rateReview['date'].append(ratingList['date'][scoreIndex])
            rateReview['country'].append(ratingList['country'][scoreIndex])
            rateReview['room'].append(ratingList['room'][scoreIndex])
            rateReview['title'].append(ratingList['title'][scoreIndex])
            rateReview['travellerType'].append(ratingList['travellerType'][scoreIndex])
    return rateReview

"""
This function will get a list and filter by keyword and return the result of the keyword 
in a new dictionry list
listName: list that want to be filter by keyword
keyword: user input the keyword that wish to be filter
"""
def searchByKeyword(listName,keyword):
    getHotel = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    for reviewsIndex in range(0,len(listName['reviews'])):
        if(keyword in listName['reviews'][reviewsIndex].lower()):
            getHotel['reviews'].append(listName['reviews'][reviewsIndex])
            getHotel['score'].append(listName['score'][reviewsIndex])
            getHotel['hotel'].append(listName['hotel'][reviewsIndex])
            getHotel['date'].append(listName['date'][reviewsIndex])
            getHotel['country'].append(listName['country'][reviewsIndex])
            getHotel['room'].append(listName['room'][reviewsIndex])
            getHotel['title'].append(listName['title'][reviewsIndex])
            getHotel['travellerType'].append(listName['travellerType'][reviewsIndex])
    return getHotel

"""
This function will get the selected hotel and rating, keyword is optional
and will return a display of the chart.
"""
def displayChart(listName,hotelName,rate,keyword=''):
    keyword = keyword.strip()
    keyword = keyword.lower()
    gethotelList = getHotelChoice(listName,hotelName)
    getkeywordList = searchByKeyword(gethotelList, keyword)
    countStarList={}
    title =[]
    for rating in rate:
        ratingList = number_of_star(getkeywordList,rating)
        countingList = countList(ratingList)
        star = str(rating)+" Star"
        countStarList[star] = countingList
    
    for key in countStarList.keys():
        for hotel in countStarList[key].keys():
            if hotel not in title:
                title.append(hotel)

    title = ['\n'.join(wrap(length,12)) for length in title]
    dataFrame = pd.DataFrame.from_dict(countStarList)

    size=np.arange(len(hotelName))
    size1=np.arange(len(hotelName))
    width_bar=0.1
    legandList =[]

    if(len(rate) == 1):
        star = str(rate[0])+" Star"
        legandList.append(star)
        plt.figure("Chart")
        if(len(keyword)!=0):
            chartTitle = "Keyword: "+keyword
            plt.title(chartTitle)
        plt.bar(size,dataFrame[star],width=width_bar)
        plt.xticks(size,title)
        plt.legend(legandList,loc=len(rate))
        plt.show()
    if(len(rate) > 1):
        plt.figure("Chart")
        for rating in range(0,len(rate)):
            star = str(rate[rating])+" Star"
            legandList.append(star)
            if rating==0:
                plt.bar(size,dataFrame[star],width=width_bar)
            else:
                plt.bar(size1,dataFrame[star],width=width_bar)
            size1= size1+width_bar
        
        if(len(keyword)!=0):
            chartTitle = "Keyword: "+keyword
            plt.title(chartTitle)
        plt.figure("Chart")
        plt.xticks(ticks=size,labels=title) 
        plt.legend(legandList,loc='upper right')
        plt.show()

"""
This function will return color with bright color
"""
def random_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):
    hue = random_state.randint(0,255)
    saturation = 50
    lightness = 40
    return "hsl({}, {}%, {}%)".format(hue, saturation, lightness)

"""
This function will get the selected hotel and rating
and will return a display of the wordmap.
"""
def wordCloud(listName,hotelName,rate):
    intRate = [int(rating) for rating in rate]
    word = []
    for intIndex in intRate:
        ratingList = number_of_star(listName,intIndex)
        for hotelIndex in range(0,len(ratingList['hotel'])):
            for hotelNameIndex in range(0,len(hotelName)):
                if ratingList['hotel'][hotelIndex] == hotelName[hotelNameIndex]:
                    intIndex = ratingList['reviews'][hotelIndex].lower().split()
                    for rated in intIndex:
                        word.append(rated)
    topcount = 50
    filtertext = filter(lambda w: not w in commonword, word)
    newtext = ""
    newlist = []
    for word in filtertext:
        res = re.sub(r'[^\w\s]', '', word)
        newlist.append(res)
    counter = Counter(newlist)
    most_common_list = []
    for c in counter.most_common(int(topcount)):
        most_common_list.append(c[0])
    newtext += " ".join(most_common_list) + " "
    # create the wordcloud object
    wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white',
                          collocations=False,
                          min_word_length=4,
                          color_func=random_color_func,
                          collocation_threshold=3).generate(newtext)

    text1_dict = {k: v for k, v in
                  sorted(wordcloud.process_text(newtext).items(), reverse=True, key=lambda item: item[1])}

    plt.figure("Wordmap")
    plt.imshow(wordcloud, interpolation='bilInear')
    plt.axis('off')    
    plt.show()

"""
This function is to detect all the language and add only english into new dictionary list
*NOTE* that language detect will took awhile to load for checking
"""
def languageDetect(list):
    clearEmpty = filterEmptyList(list,False)
    langList = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    for reviewIndex in range(0,len(clearEmpty['reviews'])):
        emojiToEnglish = emoji.demojize(clearEmpty['reviews'][reviewIndex])
        langDetect = str(detect_langs(emojiToEnglish)[0]).split(":")
        if(langDetect[0] == 'en' and float(langDetect[1]) >= 0.5):
            langList['reviews'].append(clearEmpty['reviews'][reviewIndex])
            langList['score'].append(clearEmpty['score'][reviewIndex])
            langList['hotel'].append(clearEmpty['hotel'][reviewIndex])
            langList['date'].append(clearEmpty['date'][reviewIndex])
            langList['country'].append(clearEmpty['country'][reviewIndex])
            langList['room'].append(clearEmpty['room'][reviewIndex])
            langList['title'].append(clearEmpty['title'][reviewIndex])
            langList['travellerType'].append(clearEmpty['travellerType'][reviewIndex])
    return langList