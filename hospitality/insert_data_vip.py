import sqlite3
import xlrd

hospitalitys_real = xlrd.open_workbook('HospitalityReal.xlsx')
hospitalitys_united = xlrd.open_workbook('HospitalityUnited.xlsx')

sheet_real = hospitalitys_real.sheet_by_name('Sheet1')
sheet_united = hospitalitys_united.sheet_by_name('Sheet1')

database = sqlite3.connect('../db.sqlite3')

cursor = database.cursor()
cursor.execute('DELETE FROM hospitality_hospitalityvip')

for row in range(0, sheet_united.nrows):
    name_real = sheet_real.cell(row, 0).value
    description_real = sheet_real.cell(row, 1).value
    name_united = sheet_united.cell(row, 0).value
    description_united = sheet_united.cell(row, 1).value

    query = f"INSERT INTO hospitality_hospitalityvip(name_real,description_real,name_united,description_united)" \
            f"VALUES('{name_real}','{description_real}','{name_united}','{description_united}')"

    cursor.execute(query)

cursor.close()
database.commit()
database.close()
