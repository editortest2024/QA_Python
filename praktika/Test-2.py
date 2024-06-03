import pymysql
import random
import pymysql.cursors

from main_config_base import host,port,user,password,db_name

def create_team_table ():
    q = '''CREATE TABLE team (
        id int primary key not null AUTO_INCREMENT,
        name varchar(255) not null,
        part_num int not null,
        CONSTRAINT CHK_part_num CHECK (part_num > 0 AND part_num < 11),
        CONSTRAINT UC_name UNIQUE (name)
    )'''
    cursor.execute(q)
    connection.commit()
    print('Table `team` created successfully!')

def fill_team_table ():
    f_w = ['Star', 'Golden', 'Power', 'Angry', 'Mighty']
    s_w = ['dragons', 'dogs', 'cats', 'eagles', 'lions']
    names = set()
    while len(names) < 11:
        names.add(random.choice(f_w) + ' ' + random.choice(s_w))
    
    for n in names:
        q = f"insert into team (name, part_num) values ('{n}', {random.randint(1, 11)});"
        cursor.execute(q)
    connection.commit()

def print_teams (n: int = 5):
    q = f"select name, part_num from team where part_num > {n};"
    cursor.execute(q)
    rows = cursor.fetchall()
    if not len(rows):
        print (f'No teams with {n} and more participants!')
    else:
        for i in rows:
            print(i)

def create_AB_user_view():
    q = '''create view user_AB_18 AS
                    SELECT id, name, email, password, reg_date FROM `user`
                    WHERE (`name` LIKE "А%" or `name` LIKE "Б%") 
                    and YEAR(reg_date) = 2018;'''
    cursor.execute(q)  
    connection.commit()
    print('View user_AB_18 created!')
    q = 'select id from user_AB_18 limit 1;'
    cursor.execute(q)
    if not cursor.fetchone():
        print('No user fit for user_AB_18 view!')

def create_good_NO_IceTee_view():
    q = '''create view good_NO_IceTee AS
                    SELECT id, category_id, name, count, price
                    FROM `good`
                    WHERE name not LIKE "%АЙС ТИ%";'''
    cursor.execute(q)  
    print('View good_NO_IceTee created!')
    connection.commit()
    q = 'select * from good_NO_IceTee limit 20'
    cursor.execute(q)
    rows = cursor.fetchall()
    for r in rows:
        r['name'] += " изменено"
        r['count'] += 5
        r['price'] += 10
        q = f"update good_NO_IceTee set name = '{r['name']}', count = {r['count']}, price = {r['price']} where id = {r['id']};"
        cursor.execute(q)
        print(r)
    connection.commit()

try:
    connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
    )
    print('Succsessful connection')
    print('#' * 30)
    try:
        with connection.cursor() as cursor:
            create_team_table ()            
            fill_team_table ()
            print_teams ()
            create_AB_user_view()
            create_good_NO_IceTee_view()

    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)
