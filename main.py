from function import *

#load CSV data into list
#called the list in to a dict list
reviews = loadReviewsList()

print(len(reviews['hotel']))

#TODO: Filter the good reviews list ('find got any negetive comment, no comment like bots') and add to new list
#TODO: Filter the bad reviews list ('Remove the value with none,nil and etc') and add to new list
#TODO: get the percentage of each of the hotel after filtering
#TODO: get the avgrage score of each hotel after filtering
#TODO: using pandas to generate by the list and make a chart to show the graphic visual
#original vs filter good review percentage | original vs filter original vs filter good review percentage | original vs avg score percentage
