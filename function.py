import csv

a={'good':[],'bad':[],'score':[],'hotel':[]}
hotel_name = ['Pan Pacific Hotel','Marina Bay Sands Hotel','Mandarin Oriental','Hotel Fort Canning','JW Marriott Hotel','Shangri-La Singapore','The Fullerton Hotel','Ritz-Carlton Hotel']

def loadCSVTolist(fileName, hotelName):
    fileName = 'csv/'+fileName+'.csv'
    with open(fileName,newline='', encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        next(reader, None)  # skip the headers
        for i in reader:
            a['good'].append(i[2])
            a['bad'].append(i[3])
            score = round(float(i[1])/2,2)
            a['score'].append(score)
            a['hotel'].append(hotelName)
    return a

#first argv is csv file name, 
#second argv is hotel name that you are going to store into the list.
def loadReviewsList():
    loadCSVTolist("pan","Pan Pacific Hotel")
    loadCSVTolist("mbs","Marina Bay Sands Hotel")
    loadCSVTolist("mandarin_oriental","Mandarin Oriental")
    loadCSVTolist("hotel_fort_canning","Hotel Fort Canning")
    loadCSVTolist("jw_marriott_hotel","JW Marriott Hotel")
    loadCSVTolist("shangri_la","Shangri-La Singapore")
    loadCSVTolist("the_fullerton_hotel","The Fullerton Hotel")
    loadCSVTolist("the_ritz_carlton","Ritz-Carlton Hotel")
    return a