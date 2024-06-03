import pymysql
import pymysql.cursors
from main_config_base_old import host,user,password,db_name


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
           insert_into_q = 'INSERT INTO `good` (`id`,`category_id`,`name`,`count`,`price`) VALUES (null,1,"new_good",10,100);'
           cursor.execute(insert_into_q)
           connection.commit()
           print('new record')


           check_query = 'SELECT * FROM `good` WHERE name = "new_good";'
           cursor.execute(check_query)
           result = cursor.fetchone()
           if result:
               print('good')
           else:
               print('not good')





    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)


