import random

import bs4
import requests
import xlsxwriter

url = "https://tickets.mancity.com/en-GB/categories/Men's%20Tickets"

result = requests.get(url)

soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('div', class_='dataItem item_background item_data_background')

context = {'data': []}

for case in cases:
    data = {}
    db_title = case.find('span', class_='small_text_d name')
    title = db_title.text.replace('\n', '')
    db_description = case.find('div', class_='small_text_a description')
    description = db_description.text.replace('\n', '')
    if not title:
        data['title'] = 'No data available'
    else:
        data['title'] = title[21:]
    if not description:
        data['description'] = 'No data available'
    else:
        data['description'] = description[21:]

    context['data'].append(data)

workbook = xlsxwriter.Workbook('ManCity.xlsx')
worksheet = workbook.add_worksheet('Fixtures')

row = 0
col = 0

for date in context['data']:
    worksheet.write(row, col, date['title'])
    worksheet.write(row, col + 1, date['description'])
    worksheet.write(row, col + 2, f'{random.randint(35, 60)}')
    row += 1

workbook.close()

# django-crontab
