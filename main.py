from function import *

#Call loadReviewList from function.py

# {"good":['inside all good reviews'],
# "bad":['inside all bad or none reviews'],
# "score":['the score that the customer give'],
# "location":['hotel name']}
reviews = loadReviewList()

print(reviews['bad'])
#total len of the list of review
print(len(reviews['score']))

#Total data (16,524) as 100% for good and bad review.

#TODO: Filter the good reviews list ('find got any negetive comment, no comment like bots')
#TODO: Filter the bad reviews list ('Remove the value with none,nil and etc')
#TODO: using the (len of 16524)-(the filter list) to get the total percentage of the hotel
#TODO: example hotel location: MBS (get all the good reviews)/(total review of MBS) to get the avgrage score
#TODO: using pandas to generate by the list and make a chart to show the graphic visual