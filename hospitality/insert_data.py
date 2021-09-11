import datetime
import sqlite3
import xlrd

hospitalitys = xlrd.open_workbook('Hospitality.xlsx')

sheet = hospitalitys.sheet_by_name('Sheet1')

database = sqlite3.connect('../db.sqlite3')

cursor = database.cursor()

for row in range(0, sheet.nrows):
    name = sheet.cell(row, 0).value
    price = sheet.cell(row, 1).value
    description = sheet.cell(row, 2).value
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    query = f"INSERT INTO hospitality_hospitality(name,price,description,created_at,updated_at)" \
            f"VALUES('{name}','{price}','{description}','{created_at}','{updated_at}')"

    cursor.execute(query)

cursor.close()
database.commit()
database.close()
