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
            cursor.execute('SHOW TABLES LIKE "good_category";')
            result = cursor.fetchone()
            if not result:
               print('does not exist')
            else:
                print('exists')
           
            count_nulls_q = '''
            SELECT
                SUM(CASE WHEN id IS NULL THEN 1 ELSE 0 END) +
                SUM(CASE WHEN parent_id IS NULL THEN 1 ELSE 0 END) +
                SUM(CASE WHEN name IS NULL THEN 1 ELSE 0 END) AS null_count
            FROM `good_category`;
            '''


            cursor.execute(count_nulls_q)  
            null_counts = cursor.fetchone()


            print(f'{null_counts["null_count"]}')




            create_view = '''
                CREATE VIEW null_count_in_g_g AS
                SELECT
                    SUM(CASE WHEN id IS NULL THEN 1 ELSE 0 END)  +
                    SUM(CASE WHEN parent_id IS NULL THEN 1 ELSE 0 END)+
                    SUM(CASE WHEN name IS NULL THEN 1 ELSE 0 END) AS null_count
                FROM `good_category`;
            '''
            cursor.execute(create_view)
            connection.commit()
            print('created')






    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)
