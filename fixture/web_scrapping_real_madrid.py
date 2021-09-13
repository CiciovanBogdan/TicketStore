import random
import bs4
import requests
import xlsxwriter

url = "https://www.madrid-football-tickets.com/REAL-MADRID-FOOTBALL-TICKETS"

result = requests.get(url)
print(result)
soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('div', class_='container category_list-container')

context = {'data': []}

for case in cases:
    data = {}
    db_title = case.find('h4', class_='category_list-title')
    title = db_title.text.replace('\n', '')
    db_description = case.find('div', class_='category_list-info')
    description = db_description.text.replace('\n', '')
    if not title:
        data['title'] = 'No data available'
    else:
        data['title'] = title[8:]
    if not description:
        data['description'] = 'No data available'
    else:
        data['description'] = description[4:14]

    context['data'].append(data)

workbook = xlsxwriter.Workbook('RealMadrid.xlsx')
worksheet = workbook.add_worksheet('Fixture')

row = 0
col = 0

for date in context['data']:
    worksheet.write(row, col, date['title'])
    worksheet.write(row, col + 1, date['description'])
    worksheet.write(row, col + 2, f'{random.randint(35, 60)}')
    row += 1

workbook.close()

# django-crontab
