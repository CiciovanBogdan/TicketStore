import sqlite3
import xlrd

hospitalitys_city = xlrd.open_workbook('HospitalityCity.xlsx')
hospitalitys_barcelona = xlrd.open_workbook('HospBarcelona.xlsx')

sheet_city = hospitalitys_city.sheet_by_name('Sheet1')
sheet_barcelona = hospitalitys_barcelona.sheet_by_name('Sheet1')

database = sqlite3.connect('../db.sqlite3')

cursor = database.cursor()
cursor.execute('DELETE FROM hospitality_hospitalitypayed')

for row in range(0, sheet_barcelona.nrows):
    name_city = sheet_city.cell(row, 0).value
    price_city = sheet_city.cell(row, 1).value
    description_city = sheet_city.cell(row, 2).value
    name_barcelona = sheet_barcelona.cell(row, 0).value
    description_barcelona = sheet_barcelona.cell(row, 1).value
    price_barcelona = sheet_barcelona.cell(row, 2).value

    query = f"INSERT INTO hospitality_hospitalitypayed(name_city,price_city,description_city,name_barcelona,price_barcelona,description_barcelona)" \
            f"VALUES('{name_city}','{price_city}','{description_city}','{name_barcelona}','{price_barcelona}','{description_barcelona}')"

    cursor.execute(query)

cursor.close()
database.commit()
database.close()
