import psycopg2
import ReadFile
import base64
# import os

hostname = "localhost"
u = "postgres"
db = "Employee"
pwd = "Abhi123@."
port_id = 5432

conn = None
cur = None

def convertToBinaryData(empId):
    filename = 'C:\\Users\\Lenovo\\Downloads\\db\\' + str(empId) + '.bmp'
    # Convert digital data to binary format.
    with open(filename, 'rb') as file:
        binaryData = base64.b64encode(file.read())
    return binaryData

# def deleteAllBmpFiles():
#     for i in range(1, 208):
#         filen = 'C:\\Users\\Lenovo\\Desktop\\' + str(i) + '.bmp'
#         try:
#             os.remove(filen)
#         except:
#             pass
#         finally:
#             pass

try:
    # deleteAllBmpFiles()

    conn = psycopg2.connect(dbname = db, user = u, host = hostname, password = pwd, port = port_id)

    cur = conn.cursor()

    create_table = ''' CREATE TABLE IF NOT EXISTS employee (
       EmployeeID SERIAL Primary KEY, 
       Name Varchar(150),
       Gender Varchar(10),
       Job_Title Varchar(30),
       MobileNo Varchar(500) NOT NULL,
       Email Varchar(1000) NOT NULL,
       Sin_no varchar(500) NOT NULL,
       Working_Year int Not NULL,
       Salary_Usd int,
       experience_level Varchar(5),
       employment_type Varchar(5),
       remote_ratio int,
       employee_residence Varchar(5),
       Company_size Varchar(5),
       Category varchar(3),
       fingerprint bytea
    ) '''

    csv_path = "C:\\Users\\Lenovo\\Desktop\\details_emp.csv"

    cur.execute(create_table)

    Data = ReadFile.load_csv(csv_path)

    
    for index,row in enumerate(Data):
        if index != 0:
            name, gender, job_title, mobileNo, email, sin, working_year,salary,experience,employment_type,remote_ratio,employee_residence,Company_size = row[1], row[2],row[3], row[4], row[5], row[6], row[7],row[8],row[9], row[10], row[11], row[12], row[13]
            
            insert_query = '''insert into employee (Name,Gender,Job_Title,MobileNo,Email,Sin_no,Working_Year,Salary_Usd,experience_level,employment_type,remote_ratio,employee_residence,Company_size) 
            values('{0}','{1}','{2}','{3}','{4}','{5}',{6},{7},'{8}','{9}','{10}','{11}','{12}')
            '''.format(name,gender,job_title,mobileNo,email,sin,working_year,salary,experience,employment_type,remote_ratio,employee_residence,Company_size)   
            
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
            emp_working_year = row[7]
            emp_Salary = row[8]
            emp_experience_level = row[9]
            emp_employment_type = row[10]
            emp_remote_ratio = row[11]
            emp_employee_residence = row[12]
            emp_Company_size = row[13]

            #binary = base64.b64decode(row[5])
            # Generate Category based on logic.
            # if(emp_id == 127):
            #     filep = 'C:\\Users\\Lenovo\\Desktop\\' + str(emp_id) + '.bmp'
            #     with open(filep,"wb") as f:
            #         f.write(binary)

            category = ''
            if emp_id % 2 == 0 :  # even
                if emp_gender == 'Male':
                    if emp_dept == 'Big Data Engineer':
                        category = 'C1'
                    elif emp_dept == 'Data Analyst':
                        category = 'C2'
                    elif emp_dept == 'Data Scientist':
                        category = 'C3'
                    elif emp_dept == 'Data Architect':
                        category = 'C4'
                else:
                    if emp_dept == 'Big Data Engineer':
                        category = 'C5'
                    elif emp_dept == 'Data Analyst':
                        category = 'C6'
                    elif emp_dept == 'Data Scientist':
                        category = 'C7'
                    elif emp_dept == 'Data Architect':
                        category = 'C8'
            else:
                if emp_gender == 'Male':
                    if emp_dept == 'Big Data Engineer':
                        category = 'C9'
                    elif emp_dept == 'Data Analyst':
                        category = 'C10'
                    elif emp_dept == 'Data Scientist':
                        category = 'C11'
                    elif emp_dept == 'Data Architect':
                        category = 'C12'
                else:
                    if emp_dept == 'Big Data Engineer':
                        category = 'C13'
                    elif emp_dept == 'Data Analyst':
                        category = 'C14'
                    elif emp_dept == 'Data Scientist':
                        category = 'C15'
                    elif emp_dept == 'Data Architect':
                        category = 'C16'                   
            
            # update category in row.
            update_statement = '''update employee set category='{0}' where employeeid={1}'''.format(category, emp_id)

            cur.execute(update_statement)
            
            # convert fingerprint to byte Array.  
            fingerprint = convertToBinaryData(emp_id)

            # print(fingerprint)

            update_statement = '''update employee set fingerprint=%s where employeeid=%s'''

            
            cur.execute(update_statement,(fingerprint, emp_id))
            
    conn.commit()
except Exception as error:
    print(error)

finally:

    if cur is not None:
        cur.close()

    if conn is not None:
        conn.close()

