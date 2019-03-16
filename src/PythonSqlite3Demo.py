import sqlite3

conn = sqlite3.connect('DMAddins_SampleData.db');
cursor=conn.cursor();

#---------create table---------
sql='CREATE TABLE Forecasting( year_month INTINTEGER ,europe_amount REAL,north_america_amount REAL,pacific_amount REAL )';
cursor.execute(sql);

sql='CREATE TABLE PersonalData(id INTEGER,income REAL,home_owner BOOLEAN,name VARCHAR(64)) ';
r=cursor.execute(sql);


#---------insert data---------
sql='INSERT INTO Forecasting (year_month,europe_amount,north_america_amount,pacific_amount) VALUES (201903,1000,2000.2,-3000.3)'
cursor.execute(sql);

sql='INSERT INTO  PersonalData (id,income,home_owner,name) VALUES (88801,20000,1,\'John\') '
cursor.execute(sql);
sql='INSERT INTO  PersonalData (id,income,home_owner,name) VALUES (88802,15000,1,\'Tim\') '
cursor.execute(sql);

sql='INSERT INTO  PersonalData (id,income,home_owner,name) VALUES (88802,20000,0,\'Copper\') '
cursor.execute(sql);

sql='INSERT INTO  PersonalData (id,income,home_owner,name) VALUES (88803,30000,0,\'Kim\') '
cursor.execute(sql);

sql='INSERT INTO  PersonalData (id,income,home_owner,name) VALUES (66601,50000,1,\'Kevin\') '
cursor.execute(sql);



#---------query data (all)---------
sql=' SELECT * FROM PersonalData '

#commit 很重要,如果不写，数据不会插入到数据库
conn.commit();  
ret=cursor.execute(sql);


for row in ret:
   print ("ID = ", row[0])
   print ("INCOME = ", row[1])
   print ("HOME_OWNER = ", row[2])
   print ("NAME = ", row[3], "\n")


#---------query data(conditional)-----------
#select id number start with "8"
sql ='SELECT * FROM PersonalData WHERE id  LIKE \'8%\' '
ret=cursor.execute(sql);


print('whose data id number start with 8 is as follow:\n');
for row in ret:
   print ("ID = ", row[0])
   print ("INCOME = ", row[1])
   print ("HOME_OWNER = ", row[2])
   print ("NAME = ", row[3], "\n")

conn.close();
print ('Opened database successfully');


