#!/usr/bin/env python3
import psycopg2


# Questions
question_1 = "\n1. What are the most popular three articles of all time?"
question_2 = "\n2. Who are the most popular article authors of all time?"
question_3 = "\n3. On which days did more than 1% of requests lead to errors?"

# Queries
query_1 = """SELECT articles.title, COUNT(*) as num
             FROM articles, log
             WHERE log.path = CONCAT('/article/', articles.slug)
               AND log.status = '200 OK'
             GROUP BY articles.title
             ORDER BY num DESC
             LIMIT 3"""
query_2 = """SELECT name, COUNT(*) as num
             FROM articles, authors, log
             WHERE log.path = CONCAT('/article/', articles.slug)
               AND authors.id = articles.author
             GROUP BY name
             ORDER BY num DESC"""
query_3 = """SELECT *
             FROM ( SELECT TO_CHAR(time, 'FMMonth DD, YYYY')
                             AS day,
                           ROUND( AVG((status != '200 OK')::int * 100), 2)
                             AS err_rate
                    FROM log
                    GROUP BY day ) AS daily_err_rate
             WHERE err_rate > 1"""

DBNAME = "news"


def get_results(question, query):
    # Print the question
    print(question)

    # Connect to database and get result with provided query
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    data = c.fetchall()

    # Print results for question 1 & 2 on a similar pattern
    if query == query_1 or query == query_2:
        for i in data:
            title_or_author = i[0]
            view_num = i[1]
            print("*", title_or_author, "-", view_num, "views")
    else:
        day = data[0][0]
        perc = str(data[0][1]) + "%"
        print("*", day, "-", perc, "errors\n")


get_results(question_1, query_1)
get_results(question_2, query_2)
get_results(question_3, query_3)
