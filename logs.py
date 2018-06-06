#!/usr/bin/env python3
import psycopg2


DBNAME = "news"

def first_question():
    print("1. What are the most popular three articles of all time?")
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """SELECT articles.title, COUNT(*) as num
               FROM articles, log
               WHERE log.path = CONCAT('/article/', articles.slug)
                 AND log.status = '200 OK'
               GROUP BY articles.title
               ORDER BY num DESC
               LIMIT 3"""
    c.execute(query)
    data = c.fetchall()
    i = 0
    for i in data:
        title = i[0]
        view_num = i[1]
        print("*", title, "-", view_num, "views")


def second_question():
    print("2. Who are the most popular article authors of all time?")
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """SELECT name, COUNT(*) as num
               FROM articles, authors, log
               WHERE log.path = CONCAT('/article/', articles.slug)
                 AND authors.id = articles.author
               GROUP BY name
               ORDER BY num DESC"""
    c.execute(query)
    data = c.fetchall()
    i = 0
    for i in data:
        author = i[0]
        view_num = i[1]
        print("*", author, "-", view_num, "views")


def third_question():
    print("3. On which days did more than 1% of requests lead to errors?")
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """SELECT *
               FROM ( SELECT TO_CHAR(time, 'FMMonth DD, YYYY') AS day,
                             ROUND(
                                AVG( (status != '200 OK')::int * 100 ),
                             2) AS err_rate
                      FROM log
                      GROUP BY day ) AS daily_err_rate
               WHERE err_rate > 1
               """
    c.execute(query)
    data = c.fetchall()
    day = data[0][0]
    perc = str(data[0][1]) + "%"
    print("*", day, "-", perc, "errors")


first_question()
second_question()
third_question()
