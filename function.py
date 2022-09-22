import json

#dict to sperate good and bad review
reviews = {"good":[],"bad":[],"score":[],"location":[]}

def openJSONFile(filename):
    jsonFile = open(filename,'r',encoding="utf8")
    data = jsonFile.read()
    return data

def loadJSON(filename):
    obj = json.loads(openJSONFile(filename))
    return obj

# a is the list name
# b is reviews['good']
# c is reviews['bad']
# d is location['']
# e is string of the location
# f is reviews['score']

def loopReview(a,b,c,d,e,f):
    for i in range(0, len(a)):
        b.append(a[i]['positive'])
        c.append(a[i]['negative'])
        f.append(a[i]['score'])
        d.append(e)

def loadReviewList():
    mbs_review = loadJSON('json/mbs.json')
    pan_review = loadJSON('json/pan.json')
    mandarin_oriental = loadJSON('json/mandarin_oriental.json')
    hotel_fort_canning = loadJSON('json/hotel_fort_canning.json')
    jw_marriott_hotel = loadJSON('json/jw_marriott_hotel.json')
    shangri_la = loadJSON('json/shangri_la.json')
    the_fullerton_hotel = loadJSON('json/the_fullerton_hotel.json')
    the_ritz_carlton = loadJSON('json/the_ritz_carlton.json')

    loopReview(mbs_review[0]['userReviews'],reviews['good'],reviews['bad'],reviews['location'],'Marina Bay Sands Hotel',reviews['score'])
    loopReview(pan_review[0]['userReviews'],reviews['good'],reviews['bad'],reviews['location'],'Pan Pacific Hotel',reviews['score'])
    loopReview(mandarin_oriental[0]['userReviews'],reviews['good'],reviews['bad'],reviews['location'],'Mandarin Oriental',reviews['score'])
    loopReview(hotel_fort_canning[0]['userReviews'],reviews['good'],reviews['bad'],reviews['location'],'Hotel Fort Canning',reviews['score'])
    loopReview(jw_marriott_hotel[0]['userReviews'],reviews['good'],reviews['bad'],reviews['location'],'JW Marriott Hotel',reviews['score'])
    loopReview(shangri_la[0]['userReviews'],reviews['good'],reviews['bad'],reviews['location'],'Shangri-La Singapore',reviews['score'])
    loopReview(the_fullerton_hotel[0]['userReviews'],reviews['good'],reviews['bad'],reviews['location'],'The Fullerton Hotel',reviews['score'])
    loopReview(the_ritz_carlton[0]['userReviews'],reviews['good'],reviews['bad'],reviews['location'],'Ritz-Carlton Hotel',reviews['score'])
    return reviews