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

print(type(listDatabases))
for db in listDatabases:
     print(db[0])

# sqlCreateTable = """
#     CREATE TABLE IF NOT EXISTS Programmers(
#     id int not null primary key auto_increment,
#     full_name varchar(50) not null,
#     age int,
#     progLang varchar(50),
#     salary double
#     );
# """
# mycursor.execute(sqlCreateTable)
# #
# sqlInsert = """
# INSERT INTO mySQLLesson.Programmers(full_name, age, progLang, salary) VALUES
# ('Tim',27,'Python', 20000),('Maria', 23, 'C++', 40000);
# """
# #
# mycursor.execute(sqlInsert)
# mysqldb_info.commit()
#
# print('Success!')

# nameProg = input("Please input name for worker: ")
# age = int(input("Please input age: "))
# nameLang = input("Please input programming language: ")
# salaryProg = int(input("Please input salary: "))
#
# sqlInsert2 = f"INSERT INTO mySQLLesson.Programmers(full_name, age, progLang, salary) " \
#             f"VALUES ('{nameProg}', {age}, '{nameLang}', {salaryProg});"
#
# mycursor.execute(sqlInsert2)
# mysqldb_info.commit()

# progName = input("Please input programmer's name: ")
# newLang = input("Input new programming language: ")
#
# sqlUpdate = f"UPDATE Programmers " \
#             f"SET progLang = '{newLang}' " \
#             f"where full_name = '{progName}'"
#
# mycursor.execute(sqlUpdate)
# mysqldb_info.commit()
#
# print('Successfully updated!')

progName = input("Please input programming language: ")

sqlShow = f" Programmers" \
    f"for db in listDatabases:"
    where progLang = {progName}
     print(db)"
