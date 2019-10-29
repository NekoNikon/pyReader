import mysql
conn = psycopg2.connect(dbname='auth', user='root', password='spadec', host='192.168.10.247')
cursor = conn.cursor()