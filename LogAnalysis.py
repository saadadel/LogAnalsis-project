#!/usr/bin/env python3
import psycopg2

dataf = open("logAnalysisData")


connection_info = dataf.readline()
conn = psycopg2.connect(connection_info)
cur = conn.cursor()

articles_select = dataf.readline()
cur.execute(articles_select)
top_articles = cur.fetchall()
file = open("projectFile.txt", "w")
top_articles_head = dataf.readline()
file.write(top_articles_head)
file.write('\n')
file.write('\n')
for x in range(1, 4):
    file.write(top_articles[x][0].rstrip('\n'))
    file.write(" _____ views: ".rstrip('\n'))
    file.write(str(top_articles[x][1]))
    file.write('\n')
file.write('\n')
file.write('\n')

authors_select = dataf.readline()
cur.execute(authors_select)
top_authors = cur.fetchall()
top_authors_head = dataf.readline()
file.write(top_authors_head)
file.write('\n')
file.write('\n')
for x in range(0, 4):
    file.write(top_authors[x][0].rstrip('\n'))
    file.write(" _____ views: ".rstrip('\n'))
    file.write(str(top_authors[x][1]))
    file.write('\n')
file.write('\n')
file.write('\n')

error_select = dataf.readline()
cur.execute(error_select)
error_days = cur.fetchall()
error_head = dataf.readline()
file.write(error_head)
file.write('\n')
file.write('\n')
i = 0
while(int(error_days[i][0] * 100) > 0):
    file.write(str(error_days[i][1]).rstrip('\n'))
    file.write(' __ ')
    file.write(str(int(error_days[i][0] * 100)))
    file.write('% \n')
    i += 1

file.close()
conn.close()

