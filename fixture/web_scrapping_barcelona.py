import random
import bs4
import requests
import xlsxwriter

url = "https://www.barcelona.com/barcelona_tickets/fc_barcelona_football_tickets"

result = requests.get(url)
print(result)
soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('div', class_='eventLine container clearfix')

context = {'data': []}

for case in cases:
    data = {}
    title = case.find('a', class_='')
    description = case.find('div', class_='date')
    if not title:
        data['title'] = 'No data available'
    else:
        data['title'] = title.text
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
worksheet = workbook.add_worksheet('Fixture')

row = 0
col = 0

for date in context['data']:
    worksheet.write(row, col, date['title'])
    worksheet.write(row, col + 1, date['description'])
    worksheet.write(row, col + 2, f'{random.randint(50, 90)}')
    row += 1

workbook.close()
