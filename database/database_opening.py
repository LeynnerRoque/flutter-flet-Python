import mysql.connector

import pymysql


conection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='*****',
    database='database',
    autocommit=True
)

credenciaisBanco = mysql.connector.connect(
        host='localhost',
        user='root',
        password='roque1989',
        database='appjobs',
        auth_plugin='mysql_native_password'
    )


def credencias():
    return conection



def operator_db():
    return conection.cursor()

