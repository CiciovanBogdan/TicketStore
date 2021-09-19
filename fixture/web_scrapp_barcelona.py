import random
import bs4
import requests
import xlsxwriter

url = "https://www.eventuria.ro/oferte/pachete-cazare-si-bilete-fc-barcelona"

result = requests.get(url)
print(result)
soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('div', class_='row qc-equal')

context = {'data': []}

for case in cases:
    data = {}
    title = case.find('p', class_='cs-offer-room-type-caption')
    description = case.find('p', class_='cs-offer-meal-type-caption')
    if not title:
        data['title'] = 'No data available'
    else:
        data['title'] = title.text[0: title.text.index('-')]
    if not description:
        data['description'] = 'No data available'
    else:
        data['description'] = description.text

    context['data'].append(data)

# mystring = "123⋯567"
# mystring[ 0 : mystring.index("⋯")]
#
# >> '123'

workbook = xlsxwriter.Workbook('Barcelona.xlsx')
worksheet = workbook.add_worksheet('Fixture-Barcelona')

row = 0
col = 0

for date in context['data']:
    worksheet.write(row, col, date['title'])
    worksheet.write(row, col + 1, date['description'])
    worksheet.write(row, col + 2, f'{random.randint(40, 65)}')
    row += 1

workbook.close()
