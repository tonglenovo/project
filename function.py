import csv
from textwrap import wrap
from turtle import width
from numpy import positive
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector
import numpy as np
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import PIL.Image


nlp = spacy.load('en_core_web_sm')
@Language.factory('language_detector')
def language_detector(nlp, name):
    return LanguageDetector()
nlp.add_pipe('language_detector', last=True)

hotel_name = ['Pan Pacific Hotel','Marina Bay Sands Hotel','Mandarin Oriental','Hotel Fort Canning','JW Marriott Hotel','Shangri-La Singapore','The Fullerton Hotel','Ritz-Carlton Hotel','Four Seasons Hotel']
reviews = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
test = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
badKeyword = ['bad','dirty','no','not','empty','boring','raining','small','unusual','slanted',"don't",'dislike','unfair','unfriendly','rude','terrible','overpriced','awful','overcrowded','crowded','expensive']
# {'MBS':{'reviews':[],'score:'[]}, 'Pan':{'reviews':[]}}
def readCSV(fileName,hotelName,state):
    file_name=open('csv/'+fileName+'.csv','r',encoding='utf-8', errors='ignore')
    file = csv.DictReader(file_name)
    if state == 1:
        for col in file:
            # doc = nlp(col['positive'])
            # detect_language = doc._.language
            # doc1 = nlp(col['negative'])
            # detect_language1 = doc1._.language
            # print(detect_language['language']=='en')
            # if(detect_language > 0.5 or detect_language1 > 0.5)
            if(col['positive'].isascii() and col['negative'].isascii()):
            #if(detect_language['language']=='en'):
                reviews['reviews'].append(col['positive'])
                reviews['reviews'].append(col['negative'])
                reviews['hotel'].append(hotelName)
                reviews['hotel'].append(hotelName)
                a = float(col['score'])/2
                reviews['score'].append(round(a,2))
                reviews['score'].append(1.0) 
                date = col['date'].split()
                reviews['date'].append(date[1])
                reviews['date'].append(date[1])
                reviews['country'].append(col['country'])
                reviews['country'].append(col['country'])
                reviews['room'].append(col['room'])
                reviews['room'].append(col['room'])
                reviews['title'].append(col['\ufefftitle'])
                reviews['title'].append(col['\ufefftitle'])
                reviews['travellerType'].append(col['travellerType'])
                reviews['travellerType'].append(col['travellerType'])
        return reviews
    else:
        for col in file:
            if(col['Review'].isascii()):
                t = col['date'].split()
                reviews['reviews'].append(col['Review'])
                reviews['hotel'].append(hotelName)
                a = float(col['Rating'])
                reviews['score'].append(round(a,2))
                reviews['title'].append(col['Review title'])
                if(len(t) == 0):
                    reviews['date'].append('')
                else:
                    reviews['date'].append(t[1])
                reviews['country'].append('')
                reviews['room'].append('')
                reviews['travellerType'].append(col['traveller_type'])
        return reviews
    
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

def filterEmptyList(combineList,state):
    filterEmptyList = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    afterFilterEmptyList = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    for i in range(0,len(combineList['reviews'])):
        a = combineList['reviews'][i].lower()
        if a == '' or a =='nil' or a =='none' or a =='n/a' or a =='na' or a =='-':
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

def test_function(list):
    a={}
    b=countList(list)
    a['hotel']=b
    
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

def findMostUsedWord(list):
    keyword={}
    common_word=['the','and','to','a','was','in','of','is','we','for','i','with','at']
    for i in list['reviews']:
        i = i.split()
        for j in i:
            j = j.lower()
            if j not in keyword:
                if j not in common_word:
                    keyword[j]=1
            else:
                keyword[j]+=1

    sort = sorted(keyword.items(),key=lambda keyword: keyword[1],  reverse=True)[:75]
    return sort

def showChartByHotel(listName,title):
    dfList = countList(listName)
    df = pd.DataFrame(list(dfList.items()),columns=['Hotel Name','Count'])
    print(df)
    plt.xticks(rotation=45)
    sns.barplot(data=df,x="Hotel Name",y="Count").set(title=title)
    # sns.countplot(data=df)
    plt.show()

def showKeywordChart(keywordList,title):
    df2 = pd.DataFrame(keywordList,columns=['Keyword','value'])
    plt.xticks(rotation=90)
    sns.barplot(data=df2,x="Keyword",y="value").set(title=title)
    plt.show()
    df2.to_csv('result/'+title+'.csv', encoding='utf-8-sig',index=False)

def dictToCsv(dict_list):
    reviews=[]
    score=[]
    hotel=[]
    date=[]
    country=[]
    room=[]
    title=[]
    travellerType = []

    for i in range(0,len(dict_list['hotel'])):
        reviews.append(dict_list['reviews'][i])
        score.append(dict_list['score'][i])
        hotel.append(dict_list['hotel'][i])
        date.append(dict_list['date'][i])
        country.append(dict_list['country'][i])
        room.append(dict_list['room'][i])
        title.append(dict_list['title'][i])
        travellerType.append(dict_list['travellerType'][i])
    allList = list(zip(reviews,score,hotel,date,country,room,title,travellerType))
    hr_df_1 = pd.DataFrame(allList, columns = ['reviews', 'score','hotel','date','country','room','title','travellerType'])
    # hr_df_1.to_csv('result/'+filename+'.csv', encoding='utf-8-sig',index=False)
    return hr_df_1

def getHotelChoice(listName,hotelName):
    print(hotelName)
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

def reviewsByHotelAndRate(listName,hotelName,Rate):
    gethotelList = getHotelChoice(listName,hotelName)
    rateReview = {'reviews':[], 'score':[],'hotel':[],'date':[],'country':[],'room':[],'title':[],'travellerType':[]}
    print(Rate)
    # for b in Rate:
    #     a = number_of_star(listName,b)
    #     for i in range(0,len(a['hotel'])):
    #         for j in range(0,len(hotelName)):
    #             if a['hotel'][i] == hotelName[j]:
    #                 getHotel['reviews'].append(listName['reviews'][i])
    #                 getHotel['score'].append(listName['score'][i])
    #                 getHotel['hotel'].append(listName['hotel'][i])
    #                 getHotel['date'].append(listName['date'][i])
    #                 getHotel['country'].append(listName['country'][i])
    #                 getHotel['room'].append(listName['room'][i])
    #                 getHotel['title'].append(listName['title'][i])
    #                 getHotel['travellerType'].append(listName['travellerType'][i])
    for i in Rate:
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

def sortByHotelName(listName,hotelName,rate,keyword):
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
        
    # for i in rate:
    #     a = number_of_star(getHotel,i)
    #     b = countList(a)
    #     s = str(i)+" Star"
    #     d[s] = b
    # for i in d:
    #     title.append(i)
    #     for k in d[i]:
    #         hotel.append(k)
    #     for j in d[i].values():
    #         total_count.append(j)
    # print(d)
    # print(title)
    # print(hotel)
    # print(total_count)
    # allList = list(zip(title,hotel,total_count))
    # hr_df_1 = pd.DataFrame(allList, columns = ['title','hotel','total_count'])
    # print(hr_df_1)


    # a = countList(getHotel)
    # print
    # b = number_of_star(getHotel,5)
    # c = countList(b)
    # print(c)
    
    # df = pd.DataFrame(list(a.items()),columns=['Hotel Name','Count'])
    # print(df)

def final():
    #load data from csv
    combinedReviews = loadReviewsList()
    # print('Final: ' + str(len(combinedReviews['reviews'])))

    #remove empty inside the data
    clearEmptyList = filterEmptyList(combinedReviews,False)

    #remove reviews that contain negative keyword
    sortBadKeywordOut = havingBadWordList(clearEmptyList,False)
    return sortBadKeywordOut

def wordCloud(listName,hotelName,Rate):
    intRate = [int(i) for i in Rate]
    word = []
    for b in intRate:
        a = number_of_star(listName,b)
        for i in range(0,len(a['hotel'])):
            for j in range(0,len(hotelName)):
                if a['hotel'][i] == hotelName[j]:
                    b = a['reviews'][i].lower().split()
                    for k in b:
                        word.append(k)

                    
    image_mask = np.array(PIL.Image.open("art/cloud.png"))
    tester =','.join(word)
    wc = WordCloud(stopwords=STOPWORDS,
    mask=image_mask,background_color="white",contour_color="black",contour_width=3,min_font_size=3).generate(tester)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()  

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
        