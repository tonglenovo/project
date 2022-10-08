from function import*
import sqlite3

conn = sqlite3.connect('test_database')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS reviews (reviews,score,hotel,date,country,room,title,travellerType)')
conn.commit()

combinedReviews = loadReviewsList()
clearEmptyList = filterEmptyList(combinedReviews,False)
sortBadKeywordOut = havingBadWordList(clearEmptyList,False)
sql = dictToCsv(sortBadKeywordOut)

sql.to_sql('reviews', conn, if_exists='replace', index = False)

c.execute('''  
SELECT reviews FROM reviews WHERE hotel='Shangri-La Singapore'
          ''')

for row in c.fetchall():
    print (row)
