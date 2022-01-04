import sqlite3
import xlrd

all_dates = xlrd.open_workbook('../fixture/RealMadrid.xlsx')

sheet = all_dates.sheet_by_name('Fixture')

database = sqlite3.connect('../db.sqlite3')

cursor = database.cursor()
cursor.execute("DELETE FROM hospitality_availabledate")

for row in range(0, sheet.nrows):
    date = sheet.cell(row, 1).value

    query = f"INSERT INTO hospitality_availabledate(date)" \
            f" VALUES('{date}')"

    cursor.execute(query)

cursor.close()
database.commit()
database.close()
