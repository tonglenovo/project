from function import *

#Call loadReviewList from function.py
reviews = loadReviewList()

print(reviews['bad'])
#total len of the list of review
print(len(reviews['score']))

#Total data (16,524) as 100% for good and bad review.