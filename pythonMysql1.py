import mysql.connector as mcon

mysqldb_info = mcon.connect(
    host = "localhost",
    user = "root",
    password = "mambetova123",
    database = "mySQLLesson"
)

print(mysqldb_info)

mycursor = mysqldb_info.cursor()

mycursor.execute("show databases;")

listDatabases = mycursor.fetchall()
#
print(type(listDatabases))
for db in listDatabases:
     print(db[0])
#
# sqlCreateTable = """
#     CREATE TABLE IF NOT EXISTS Djangolessons(
#     id int not null primary key auto_increment,
#     student_name varchar(100) not null,
#     age int,
#     country varchar(50)
#     );
# """
# # 3mycursor.execute(sqlCreateTable)
# #
# sqlInsert = """
# INSERT INTO mySQLLesson.Djangolessons(student_name,age,country) VALUES
# ('Tamara',25,'Poland'),('Maria', 28, 'Ukraine');
# """
#
# mycursor.execute(sqlInsert)
# mysqldb_info.commit()
#
# print('Success!')

nameStudent  = input("Please input name for student: ")
age = int(input("Please input age: "))
country = input("Please input country: ")

sqlInsert2 = f"INSERT INTO mySQLLesson.Djangolessons(student_name,age,country) " \
            f"VALUES ('{nameStudent}',{age}, '{country}');"

mycursor.execute(sqlInsert2)
mysqldb_info.commit()

# oldName = input("Please input old name: ")
# newName = input("Input new name for student: ")
#
# sqlUpdate = f"UPDATE Djangolessons " \
#             f"SET student_name = '{newName}' " \
#             f"where student_name = '{oldName}'"

# mycursor.execute(sqlUpdate)
# mysqldb_info.commit()
#
# print('Successfully updated!')








