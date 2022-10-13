import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
from wordcloud import WordCloud,STOPWORDS
import PIL.Image
from collections import Counter
import re
from nltk.corpus import stopwords

commonword = set(stopwords.words('english'))
hotel_name = ['Pan Pacific Hotel','Marina Bay Sands Hotel','Mandarin Oriental','Hotel Fort Canning','JW Marriott Hotel','Shangri-La Singapore','The Fullerton Hotel','Ritz-Carlton Hotel','Four Seasons Hotel']
reviews = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
checkingEmpty = ['none','na','n/a','nil','-','nothing']
badKeyword = ['bad','dirty','no','not','empty','boring','raining','small','unusual','slanted',"don't",'dislike','unfair','unfriendly','rude','terrible','overpriced','awful','overcrowded','crowded','expensive']

# {'MBS':{'reviews':[],'score:'[]}, 'Pan':{'reviews':[]}}

#This function readCSV file and add to review dict list.

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
            a = float(col['Rating'])
            reviews['score'].append(round(a,2))
            reviews['title'].append(col['Review title'])
            if(len(date) == 0):
                reviews['date'].append('')
            else:
                reviews['date'].append(date[1])
            reviews['country'].append('')
            reviews['room'].append('')
            reviews['travellerType'].append(col['traveller_type'])
        return reviews

#This function will readCSV, load all data into reviews dict and return the dict list that all is appended.
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

#This function will remove all the special character from other country such as jp, ko, ga, spina and etc.
def removeSpecialCharacter(list):
    removeSpecialCharacterList = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    for i in range(0,len(list['reviews'])):
        if(list['reviews'][i].isascii()):
            removeSpecialCharacterList['reviews'].append(list['reviews'][i])
            removeSpecialCharacterList['score'].append(list['score'][i])
            removeSpecialCharacterList['hotel'].append(list['hotel'][i])
            removeSpecialCharacterList['title'].append(list['title'][i])
            removeSpecialCharacterList['date'].append(list['date'][i])
            removeSpecialCharacterList['country'].append(list['country'][i])
            removeSpecialCharacterList['room'].append(list['room'][i])
            removeSpecialCharacterList['travellerType'].append(list['travellerType'][i])
    return removeSpecialCharacterList

# This function will remove all the empty string, no comment, nil and ETC
#state True is getEmpty data, state False will get data that clear empty
def filterEmptyList(combineList,state):
    filterEmptyList = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    afterFilterEmptyList = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    for i in range(0,len(combineList['reviews'])):
        a = combineList['reviews'][i].lower()
        if any(word in a for word in checkingEmpty) or (len(a) == 1):
            filterEmptyList['reviews'].append(combineList['reviews'][i])
            filterEmptyList['score'].append(combineList['score'][i])
            filterEmptyList['hotel'].append(combineList['hotel'][i])
            filterEmptyList['title'].append(combineList['title'][i])
            filterEmptyList['date'].append(combineList['date'][i])
            filterEmptyList['country'].append(combineList['country'][i])
            filterEmptyList['room'].append(combineList['room'][i])
            filterEmptyList['travellerType'].append(combineList['travellerType'][i])
        else:
            afterFilterEmptyList['reviews'].append(combineList['reviews'][i])
            afterFilterEmptyList['score'].append(combineList['score'][i])
            afterFilterEmptyList['hotel'].append(combineList['hotel'][i])
            afterFilterEmptyList['title'].append(combineList['title'][i])
            afterFilterEmptyList['date'].append(combineList['date'][i])
            afterFilterEmptyList['country'].append(combineList['country'][i])
            afterFilterEmptyList['room'].append(combineList['room'][i])
            afterFilterEmptyList['travellerType'].append(combineList['travellerType'][i])
    if state == True:
        return filterEmptyList
    else:
        return afterFilterEmptyList

# This function will count each hotel have how many reviews.
#{'Marina Bay Sands Hotel': 976, 'Pan Pacific Hotel': 320}
def countList(list):
    dfEmptyList = {}
    for i in range(0,len(list['hotel'])):
        for j in hotel_name:
            if(list['hotel'][i] == j):
                if(j not in dfEmptyList):
                    dfEmptyList[j]=1
                else:
                    dfEmptyList[j]+=1
    return dfEmptyList

#This function will remove the negative keyword base on the team disscusion.
def havingBadWordList(list, badWord):
    containBadKeyword = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    sortBadKeywordOut = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    for i in range(0,len(list['reviews'])):
        j = list['reviews'][i].lower()
        if any(word in j for word in badKeyword):
        # if j in badKeyword:
            containBadKeyword['reviews'].append(list['reviews'][i])
            containBadKeyword['score'].append(list['score'][i])
            containBadKeyword['hotel'].append(list['hotel'][i])
            containBadKeyword['title'].append(list['title'][i])
            containBadKeyword['date'].append(list['date'][i])
            containBadKeyword['country'].append(list['country'][i])
            containBadKeyword['room'].append(list['room'][i])
            containBadKeyword['travellerType'].append(list['travellerType'][i])
        else:
            sortBadKeywordOut['reviews'].append(list['reviews'][i])
            sortBadKeywordOut['score'].append(list['score'][i])
            sortBadKeywordOut['hotel'].append(list['hotel'][i])
            sortBadKeywordOut['title'].append(list['title'][i])
            sortBadKeywordOut['date'].append(list['date'][i])
            sortBadKeywordOut['country'].append(list['country'][i])
            sortBadKeywordOut['room'].append(list['room'][i])
            sortBadKeywordOut['travellerType'].append(list['travellerType'][i])
    if badWord == True:
        return containBadKeyword
    else:
        return sortBadKeywordOut

# This function will return dict of 1* review, 2* review and so on.
def number_of_star(list,num):
    reviews_one = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    reviews_two = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    reviews_three = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    reviews_four = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    reviews_five = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    
    for i in range(0, len(list['score'])):
        a = round(list['score'][i],2)
        if a < 2:
            reviews_one['reviews'].append(list['reviews'][i])
            reviews_one['score'].append(list['score'][i])
            reviews_one['hotel'].append(list['hotel'][i])
            reviews_one['title'].append(list['title'][i])
            reviews_one['date'].append(list['date'][i])
            reviews_one['country'].append(list['country'][i])
            reviews_one['room'].append(list['room'][i])
            reviews_one['travellerType'].append(list['travellerType'][i])
        elif a < 3:
            reviews_two['reviews'].append(list['reviews'][i])
            reviews_two['score'].append(list['score'][i])
            reviews_two['hotel'].append(list['hotel'][i])
            reviews_two['title'].append(list['title'][i])
            reviews_two['date'].append(list['date'][i])
            reviews_two['country'].append(list['country'][i])
            reviews_two['room'].append(list['room'][i])
            reviews_two['travellerType'].append(list['travellerType'][i])
        elif a < 4:
            reviews_three['reviews'].append(list['reviews'][i])
            reviews_three['score'].append(list['score'][i])
            reviews_three['hotel'].append(list['hotel'][i])
            reviews_three['title'].append(list['title'][i])
            reviews_three['date'].append(list['date'][i])
            reviews_three['country'].append(list['country'][i])
            reviews_three['room'].append(list['room'][i])
            reviews_three['travellerType'].append(list['travellerType'][i])
        elif a < 4.6:
            reviews_four['reviews'].append(list['reviews'][i])
            reviews_four['score'].append(list['score'][i])
            reviews_four['hotel'].append(list['hotel'][i])
            reviews_four['title'].append(list['title'][i])
            reviews_four['date'].append(list['date'][i])
            reviews_four['country'].append(list['country'][i])
            reviews_four['room'].append(list['room'][i])
            reviews_four['travellerType'].append(list['travellerType'][i])
        elif a < 6:
            reviews_five['reviews'].append(list['reviews'][i])
            reviews_five['score'].append(list['score'][i])
            reviews_five['hotel'].append(list['hotel'][i])
            reviews_five['title'].append(list['title'][i])
            reviews_five['date'].append(list['date'][i])
            reviews_five['country'].append(list['country'][i])
            reviews_five['room'].append(list['room'][i])
            reviews_five['travellerType'].append(list['travellerType'][i])
    if num == 1:
        return reviews_one
    if num == 2:
        return reviews_two
    if num == 3:
        return reviews_three
    if num == 4:
        return reviews_four
    else:
        return reviews_five

# This function will return a dict that finish filtering data cleaning
def finalList():
    getReviews = loadReviewsList()
    removeSpecial = removeSpecialCharacter(getReviews)
    getEmpty = filterEmptyList(removeSpecial, True)
    newList = filterEmptyList(removeSpecial,False)
    filterBad = havingBadWordList(newList, True)
    afterFilterBad = havingBadWordList(newList, False)

    # print("Total: " + str(len(getReviews['reviews'])))
    # print("Remove Special: " + str(len(removeSpecial['reviews'])))
    # print("Total Empty: List: " + str(len(getEmpty['reviews'])))
    # print("After Remove Empty Reviews: " + str(len(newList['reviews'])))
    # print("Bad Reviews: " + str(len(filterBad['reviews'])))
    # print("After Remove Bad Reviews: " + str(len(afterFilterBad['reviews'])))
    # print("CountList: " + str(countList(afterFilterBad)))

    # emptyOneStar = number_of_star(getEmpty,1)
    # emptyTwoStar = number_of_star(getEmpty,2)
    # emptyThreeStar = number_of_star(getEmpty,3)
    # emptyFourStar = number_of_star(getEmpty,4)
    # emptyFiveStar = number_of_star(getEmpty,5)

    # notEmptyOneStar = number_of_star(newList,1)
    # notEmptyTwoStar = number_of_star(newList,2)
    # notEmptyThreeStar = number_of_star(newList,3)
    # notEmptyFourStar = number_of_star(newList,4)
    # notEmptyFiveStar = number_of_star(newList,5)

    return afterFilterBad

# This function will return dict of the hotel that the GUI had selected.
def getHotelChoice(listName,hotelName):
    # print(hotelName)
    getHotel = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    for i in range(0,len(listName['hotel'])):
        for j in range(0,len(hotelName)):
            if(listName['hotel'][i] == hotelName[j]):
                getHotel['reviews'].append(listName['reviews'][i])
                getHotel['score'].append(listName['score'][i])
                getHotel['hotel'].append(listName['hotel'][i])
                getHotel['date'].append(listName['date'][i])
                getHotel['country'].append(listName['country'][i])
                getHotel['room'].append(listName['room'][i])
                getHotel['title'].append(listName['title'][i])
                getHotel['travellerType'].append(listName['travellerType'][i])
    return getHotel

# This function will getHotelChoice first then find the Rating and return the result as a new dict
def reviewsByHotelAndRate(listName,hotelName,rate):
    gethotelList = getHotelChoice(listName,hotelName)
    rateReview = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    # print(rate)
    for i in rate:
        a = number_of_star(gethotelList,i)
        for j in range(0,len(a['score'])):
            rateReview['reviews'].append(a['reviews'][j])
            rateReview['score'].append(a['score'][j])
            rateReview['hotel'].append(a['hotel'][j])
            rateReview['date'].append(a['date'][j])
            rateReview['country'].append(a['country'][j])
            rateReview['room'].append(a['room'][j])
            rateReview['title'].append(a['title'][j])
            rateReview['travellerType'].append(a['travellerType'][j])
    return rateReview

# This function will get Hotel List that is selected and filter base on the keyword and return a dict for Pandas DataFrame purpose
def searchByKeyword(listName,keyword):
    getHotel = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    for i in range(0,len(listName['reviews'])):
        if(keyword in listName['reviews'][i].lower()):
            getHotel['reviews'].append(listName['reviews'][i])
            getHotel['score'].append(listName['score'][i])
            getHotel['hotel'].append(listName['hotel'][i])
            getHotel['date'].append(listName['date'][i])
            getHotel['country'].append(listName['country'][i])
            getHotel['room'].append(listName['room'][i])
            getHotel['title'].append(listName['title'][i])
            getHotel['travellerType'].append(listName['travellerType'][i])
    return getHotel

#This function will get GUI selection and return a chart to display in GUI
def displayChart(listName,hotelName,rate,keyword=''):
    print(keyword)
    gethotelList = getHotelChoice(listName,hotelName)
    getkeywordList = searchByKeyword(gethotelList, keyword)
    d={}
    title =[]
    for i in rate:
        a = number_of_star(getkeywordList,i)
        b = countList(a)
        s = str(i)+" Star"
        d[s] = b
    
    for i in d.keys():
        for j in d[i].keys():
            if j not in title:
                title.append(j)
    print(d)
    title = ['\n'.join(wrap(l,12)) for l in title]
    
    df = pd.DataFrame.from_dict(d)
    print(df)
    size=np.arange(len(hotelName))
    size1=np.arange(len(hotelName))
    w=0.1
    test =[]
    #df.to_csv('result/df.csv', encoding='utf-8-sig',index=False)
    if(len(rate) == 1):
        s = str(rate[0])+" Star"
        test.append(s)
        plt.figure(figsize=(15,5))
        plt.bar(size,df[s],width=w)
        plt.xticks(size,title)
        plt.legend(test,loc=len(rate))
        plt.show()
    if(len(rate) > 1):
        # plt.figure(figsize=(15,2))
        plt.figure(figsize=(15,5))
        for i in range(0,len(rate)):
            s = str(rate[i])+" Star"
            test.append(s)
            if i==0:
                plt.bar(size,df[s],width=w)
            else:
                plt.bar(size1,df[s],width=w)
            size1= size1+w
        
        plt.xticks(ticks=size,labels=title) 
        plt.legend(test,loc='upper right')
        plt.show()

#This Function will base on GUI selection and return a word cloud chart.

def random_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):
    hue = random_state.randint(0,255)
    saturation = 50
    lightness = 40
    return "hsl({}, {}%, {}%)".format(hue, saturation, lightness)
    
def wordCloud(listName,hotelName,rate):
    intRate = [int(i) for i in rate]
    word = []
    for b in intRate:
        a = number_of_star(listName,b)
        for i in range(0,len(a['hotel'])):
            for j in range(0,len(hotelName)):
                if a['hotel'][i] == hotelName[j]:
                    b = a['reviews'][i].lower().split()
                    for k in b:
                        word.append(k)
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
                          collocations=True,
                          min_word_length=4,
                          color_func=random_color_func,
                          collocation_threshold=3).generate(newtext)

    text1_dict = {k: v for k, v in
                  sorted(wordcloud.process_text(newtext).items(), reverse=True, key=lambda item: item[1])}

    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilInear')
    plt.axis('off')
    plt.show()
 