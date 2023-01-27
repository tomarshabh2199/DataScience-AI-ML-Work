import psycopg2
import psycopg2.extras


hostname='localhost'
database='demo'
username='postgres'
pwd='123'
port_id=5432
conn=None:
cur=None:

try:
    conn=psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id)

    cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute('DROP TABLE IF EXISTS employee')

    create_script=''' CREATE TABLE IF NOT EXISTS employee(
                         id int PRIMARY KEY,
                         name varchar(40) NOT NULL,
                         salary int,
                         dept_id varchar(30))'''


    insert_script='INSERT INTO EMPLOYEE (id,name,salary,dept_id)
                   Values(%s,%s,%s,%s)'

    inser_values=[(1,'James',12000,'D1'),(2,'James',13000,'D3'),(3,'James',14000,'D3')]
    for record in insert_values:
        cur.execute(insert_script,record)

    update_script='UPDATE employee SET salary=salary + (salary*0.5)'
    cur.exceute(update_script)


    delete_script='DELETE FROM employee Where name=%s'
    delete_record=('James',)
    cur.execute(delete_script,delete_record)
      
    cur.execute('SELECT * FROM EMPLOYEE')
     
    for record in cur.fetchall():
        print(record['name'],record['salary'])

    
    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:
       cur.close()
    if conn is not None:
       conn.close()
