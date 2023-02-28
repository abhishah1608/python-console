import psycopg2
import ReadFile
import employee
hostname = "localhost"
u = "postgres"
db = "Employee"
pwd = "Abhi123@."
port_id = 5432

conn = None
cur = None

try:
    conn = psycopg2.connect(dbname = db, user = u, host = hostname, password = pwd, port = port_id)

    cur = conn.cursor()

    create_table = ''' CREATE TABLE IF NOT EXISTS employee (
       EmployeeID SERIAL Primary KEY, 
       Name Varchar(150),
       Gender Varchar(10),
       Department Varchar(30),
       MobileNo Varchar(15) NOT NULL,
       Email Varchar(250) NOT NULL,
       Sin_no varchar(20) NOT NULL,
       Salary int,
       Category varchar(1)
    ) '''

    csv_path = "C:\\Users\\Lenovo\\Desktop\\Capstone.csv"

    cur.execute(create_table)

    Data = ReadFile.load_csv(csv_path)


    for index,row in enumerate(Data):
        if index != 0:
            name, gender, dept, mobileNo, email, sin, salary = row[1], row[2],row[3], row[4], row[5], row[6], row[7]
            
            insert_query = '''insert into employee (Name,Gender,Department,MobileNo,Email,Sin_no,Salary) 
            values('{0}','{1}','{2}','{3}','{4}','{5}',{6})
            '''.format(str(name),gender,dept,mobileNo,email,sin,salary)   
            
            cur.execute(insert_query)
            

    conn.commit()

except Exception as error:
    print(error)

finally:

    if cur is not None:
        cur.close()

    if conn is not None:
        conn.close()