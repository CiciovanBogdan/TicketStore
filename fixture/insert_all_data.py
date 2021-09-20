import sqlite3
import xlrd

all_fixtures = xlrd.open_workbook('RealMadrid.xlsx')
all_fixtures_city = xlrd.open_workbook('ManCity.xlsx')
all_fixtures_united = xlrd.open_workbook('ManUnited.xlsx')
all_fixtures_barcelona = xlrd.open_workbook('Barcelona.xlsx')

sheet = all_fixtures.sheet_by_name('Fixture')
sheet_city = all_fixtures_city.sheet_by_name('Fixture')
sheet_united = all_fixtures_united.sheet_by_name('Fixture')
sheet_barcelona = all_fixtures_barcelona.sheet_by_name('Fixture')

database = sqlite3.connect('../db.sqlite3')

cursor = database.cursor()
cursor.execute(f"DELETE FROM fixture_fixture;")

for row in range(0, sheet.nrows):
    title_man_city = sheet_city.cell(row, 0).value
    match_info_man_city = sheet_city.cell(row, 1).value
    title_real_madrid = sheet.cell(row, 0).value
    match_info_real_madrid = sheet.cell(row, 1).value
    title_man_united = sheet_united.cell(row, 0).value
    match_info_man_united = sheet_united.cell(row, 1).value
    title_barcelona = sheet_barcelona.cell(row, 0).value
    match_info_barcelona = sheet_barcelona.cell(row, 1).value
    price = sheet_barcelona.cell(row, 2).value
    cursor.execute(
        f"INSERT INTO fixture_fixture(title_man_city,match_info_man_city,title_real_madrid,match_info_real_madrid,title_man_united,match_info_man_united,title_barcelona,match_info_barcelona,price)"
        f"VALUES('{title_man_city}','{match_info_man_city}','{title_real_madrid}','{match_info_real_madrid}','{title_man_united}','{match_info_man_united}','{title_barcelona}','{match_info_barcelona}','{price}')")

cursor.close()
database.commit()
database.close()
