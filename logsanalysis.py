import psycopg2

DBNAME = "news"

query_1 = """select * from article_views limit 3;"""

query_2 = """select name, sum(article_views.views) as views
            from article_authors, article_views
            where article_authors.title = article_views.title
            group by name
            order by views desc;"""


query_3 = """select errorlogs.date, round(100.0*errorcount/logcount,2) as percent
            from logs, errorlogs
            where logs.date = errorlogs.date
            and errorcount > logcount/100;"""


def connect_db(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


#finding the top three 

def top_three(query):
    results = connect_db(query)
    print('Displaying the most popular articles of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")


#finding the top three 


def top_authors(query):
    results = connect_db(query)
    print('the most popular authors of all time: \n ')
    for i in results:
        print(str(i[0]) + '    ' + str(i[1]) + ' views')
        
#getting the errors 


def errors(query):
    results = connect_db(query)
    print('The days when more than 1% of requests lead to error:\n')
    for i in results:
        print(str(i[0]) + '   ' + str(i[1]) + ' %' + ' errors')
        

#Print my results 

print(top_three(query_1))
print(top_authors(query_2))
print(errors(query_3))
