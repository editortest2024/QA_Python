import pymysql
import pymysql.cursors

from main_config_base import host,port,user,password,db_name

def exec_sql_create_view ():
    create_view_query = '''CREATE VIEW good_ice_tea AS
                    SELECT id, category_id, name, count, price
                    FROM `good`
                    WHERE name LIKE "%Айс Ти%"'''
    cursor.execute(create_view_query)  
    print('View created')

def exec_sql_drop_view ():
    create_view_query = 'DROP VIEW good_ice_tea'
    cursor.execute(create_view_query)  
    print('View dropped')


def exec_sql_find_table ():
    check_table = 'SHOW TABLES LIKE "good"'
    cursor.execute(check_table)
    result = cursor.fetchone()
    if result:
        print('good')
    else:
        print('not good')

def exec_sql_insert_record ():
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

def exec_sql_update_record ():
    insert_into_q = 'UPDATE `good` SET `count` = 35 WHERE `name` ="new_good";'
    cursor.execute(insert_into_q)
    connection.commit()
    print('record update')

    check_query = 'SELECT * FROM `good` WHERE name = "new_good" AND `count` = 35;'
    cursor.execute(check_query)
    result = cursor.fetchone()
    if result:
        print('good')
    else:
        print('not good')

def exec_sql_delete_record ():
    insert_into_q = 'DELETE FROM `good` WHERE `name` ="new_good";'
    cursor.execute(insert_into_q)
    connection.commit()
    print('record del')

    check_query = 'SELECT * FROM `good` WHERE name = "new_good";'
    cursor.execute(check_query)
    result = cursor.fetchone()
    if not result:
        print('good')
    else:
        print('not good')

try:
    connection = pymysql.connect(
    host=host,
    port=port,
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
            exec_sql_create_view ()
            exec_sql_drop_view ()
            exec_sql_find_table ()
            exec_sql_insert_record ()
            exec_sql_update_record ()
            exec_sql_delete_record ()

    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)
