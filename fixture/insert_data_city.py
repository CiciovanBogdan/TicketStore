import sqlite3
import xlrd

all_fixtures = xlrd.open_workbook('ManCity.xlsx')

sheet = all_fixtures.sheet_by_name('Fixtures')

database = sqlite3.connect('../db.sqlite3')

cursor = database.cursor()

for row in range(0, sheet.nrows):
    title = sheet.cell(row, 0).value
    description = sheet.cell(row, 1).value
    price = sheet.cell(row, 2).value
    cursor.execute(
        f"INSERT INTO fixture_fixturemancity(title,description,price) VALUES('{title}','{description}','{price}')")

cursor.close()
database.commit()
database.close()
