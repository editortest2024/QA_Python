import pymysql
import pymysql.cursors
from main_config_base import host,user,password,db_name


try:
    connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
    )
    print('succsess')
    print('#' * 30)
    try:
        with connection.cursor() as cursor:
            #тут пишем запросы
            cursor.execute('SHOW TABLES LIKE "user";')
            result = cursor.fetchone()
            if not result:
                print('not ex')
            else:
                print('ex')


                fid_gmail_users_q = """
                    SELECT * FROM user
                    WHERE email LIKE '%gmail.com'
                    AND reg_date BETWEEN '2017-01-02' AND '2017-09-30';
                """
                cursor.execute(fid_gmail_users_q)
                gmail_us = cursor.fetchall()


                for i in gmail_us[:10]:
                    print(i)


                create_view = """
                CREATE VIEW gmail_users_2017 AS
                SELECT *
                FROM user
                WHERE email LIKE '%gmail.com'
                AND reg_date BETWEEN '2017-01-02' AND '2017-09-30';
                """


                cursor.execute(create_view)
                connection.commit()
                print('created 2017')






    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)




