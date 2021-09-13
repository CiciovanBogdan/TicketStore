import bs4
import requests
import xlsxwriter

url = 'https://www.realmadrid.com/area-vip/temporada-vip'
result = requests.get(url)

soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('li', class_='area')

context = {'data': []}

for case in cases:
    data = {}
    product_name = case.find('h3', class_='')
    product_description = case.find('p', class_='')
    if not product_name:
        data['product_name'] = 'Not available'
    else:
        data['product_name'] = product_name.text
    if not product_description:
        data['product_description'] = 'Not available'
    else:
        data['product_description'] = product_description.text

    context['data'].append(data)

workbook = xlsxwriter.Workbook('HospitalityReal.xlsx')
worksheet = workbook.add_worksheet('Sheet1')

row = 0
col = 0

for date in context['data']:
    worksheet.write(row, col, date['product_name'])
    worksheet.write(row, col + 1, date['product_description'])
    row += 1

workbook.close()
