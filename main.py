from function import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Combine all review data # Total data 51128
combinedReviews = loadReviewsList()
print(len(combinedReviews['reviews']))

#Find out all empty list
emptyList = filterEmptyList(combinedReviews,True)
print(len(emptyList['reviews']))
dictToCsv(emptyList,'EmptyList')

empty_one_star = number_of_star(emptyList, 1)
empty_two_star = number_of_star(emptyList, 2)
empty_three_star = number_of_star(emptyList, 3)
empty_four_star = number_of_star(emptyList, 4)
empty_five_star = number_of_star(emptyList, 5)
dictToCsv(empty_one_star,'Review 1 star empty list')
dictToCsv(empty_two_star,'Review 2 star empty list')
dictToCsv(empty_three_star,'Review 3 star empty list')
dictToCsv(empty_four_star,'Review 4 star empty list')
dictToCsv(empty_five_star,'Review 5 star empty list')



#List without empty list
afterFilterEmptyList = filterEmptyList(combinedReviews,False)
print(len(afterFilterEmptyList['reviews']))
dictToCsv(afterFilterEmptyList,'afterFilterEmptyList')

#List that contain negative
containBadKeyword = havingBadWordList(afterFilterEmptyList,True)
print(len(containBadKeyword['reviews']))
dictToCsv(containBadKeyword,'containBadKeyword')

#List that without the negative
sortBadKeywordOut = havingBadWordList(afterFilterEmptyList,False)
print(len(sortBadKeywordOut['reviews']))
dictToCsv(sortBadKeywordOut,'sortBadKeywordOut')

# Add to list base on star
reviews_one = number_of_star(sortBadKeywordOut,1)
reviews_two = number_of_star(sortBadKeywordOut,2)
reviews_three = number_of_star(sortBadKeywordOut,3)
reviews_four = number_of_star(sortBadKeywordOut,4)
reviews_five = number_of_star(sortBadKeywordOut,5)
dictToCsv(reviews_one,'Review 1 star after sorting')
dictToCsv(reviews_two,'Review 2 star after sorting')
dictToCsv(reviews_three,'Review 3 star after sorting')
dictToCsv(reviews_four,'Review 4 star after sorting')
dictToCsv(reviews_five,'Review 5 star after sorting')
# print(len(reviews_one['score']))
# print(len(reviews_two['score']))
# print(len(reviews_three['score']))
# print(len(reviews_four['score']))
# print(len(reviews_five['score']))

# Most keyword is used on good review. (Up to 75 max)
keyword = findMostUsedWord(containBadKeyword)
print(keyword)
showKeywordChart(keyword,"Top 75 negative review keyword")

keyword1 = findMostUsedWord(sortBadKeywordOut)
print(keyword1)
showKeywordChart(keyword1,"Top 75 good review keyword")



# For pandas
# showChartByHotel(reviews_one,"Review 1*")
# showChartByHotel(reviews_two,"Review 2*")
# showChartByHotel(reviews_three,"Review 3*")
# showChartByHotel(reviews_four,"Review 4*")
# showChartByHotel(reviews_five,"Review 5*")


# plt.xticks(rotation=45)
# sns.barplot(data=df,x="Hotel Name",y="Count").set(title='Having negative keyword')
# # sns.countplot(data=df)
# plt.show()

# dfAfterFilterEmptyList = countList(afterFilterEmptyList)
# df1 = pd.DataFrame(list(dfAfterFilterEmptyList.items()),columns=['Hotel Name','Count'])
# print(df1)

# df2 = pd.DataFrame(keyword,columns=['Keyword','value'])
# print(df2.head())

# dfAfterFilterEmptyList = countList(reviews_one)
# df1 = pd.DataFrame(list(dfAfterFilterEmptyList.items()),columns=['Hotel Name','Count'])
# print(df1)
