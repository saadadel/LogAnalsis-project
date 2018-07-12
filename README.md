# Log Analysis
View the top viewed articles, top authors, and the days that had mor than 1% of page requests lead to error. in **NEWS** database

## Requirments
having python 3 for downloading [Python](https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz)
and **NEWS** database with **POSTGRSQL**
## Download
` git clone *the repo link*` 

## Running
Open your command prompot and type
```
cd *path to your file location*
Python3 LogAnalysis.py
```
## PSQL Views
sortedarticles:
```
create view sortedarticles as
SELECT replace(substr(log.path, 10), '-'::text, ' '::text) AS replace, 
    count(log.id) AS count
FROM log
GROUP BY log.path
ORDER BY (count(log.id)) DESC;
```
joinall:
```
create view joinall as
SELECT a.author,
    t.name,
    a.title,
    s.replace AS path,
    s.count AS views
FROM articles a
     JOIN sortedarticles s ON lower(a.title) ~~ lower(concat(s.replace, '%'))
     JOIN authors t ON a.author = t.id
WHERE s.replace <> ''::text;
```
statusok:
```
create view statusok as
SELECT count(log.status) AS ok,
    log."time"::date AS "time"
FROM log
WHERE log.status = '200 OK'::text
GROUP BY (log."time"::date);
```
statusnotfound:
```
create view statusnotfound as
SELECT count(log.status) AS ok,
    log."time"::date AS "time"
FROM log
WHERE log.status = '404 NOT FOUND'::text
GROUP BY (log."time"::date);

```
