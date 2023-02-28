import psycopg2
import ReadFile

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
       Category varchar(3)
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

    select_employees = "select * from employee"

    cur.execute(select_employees)

    records = cur.fetchall()

    if(len(records) > 0):
        for row in records:
            emp_id = row[0]
            emp_name = row[1]
            emp_gender = row[2]
            emp_dept = row[3]
            emp_mobileNo = row[4]
            emp_Email = row[5]
            emp_sin = row[6]
            emp_Salary = row[7]

            # Generate Category based on logic.
            category = ''
            if emp_id % 2 == 0 :  # even
                if emp_gender == 'Male':
                    if emp_dept == 'Software Developer':
                        category = 'C1'
                    elif emp_dept == 'QA':
                        category = 'C2'
                    elif emp_dept == 'Sales':
                        category = 'C3'
                    elif emp_dept == 'Business Analyst':
                        category = 'C4'
                else:
                    if emp_dept == 'Software Developer':
                        category = 'C5'
                    elif emp_dept == 'QA':
                        category = 'C6'
                    elif emp_dept == 'Sales':
                        category = 'C7'
                    elif emp_dept == 'Business Analyst':
                        category = 'C8'
            else:
                if emp_gender == 'Male':
                    if emp_dept == 'Software Developer':
                        category = 'C9'
                    elif emp_dept == 'QA':
                        category = 'C10'
                    elif emp_dept == 'Sales':
                        category = 'C11'
                    elif emp_dept == 'Business Analyst':
                        category = 'C12'
                else:
                    if emp_dept == 'Software Developer':
                        category = 'C13'
                    elif emp_dept == 'QA':
                        category = 'C14'
                    elif emp_dept == 'Sales':
                        category = 'C15'
                    elif emp_dept == 'Business Analyst':
                        category = 'C16'                   
            
            # update category in row.
            update_statement = '''update employee set category='{0}' where employeeid={1}'''.format(category, emp_id)

            cur.execute(update_statement) 

    conn.commit()

except Exception as error:
    print(error)

finally:

    if cur is not None:
        cur.close()

    if conn is not None:
        conn.close()

