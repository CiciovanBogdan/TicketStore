import bs4
import requests
import xlsxwriter

url = 'https://www.manutd.com/en/Executive-Club/hospitality-options'
result = requests.get(url)
print(result)

soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('div', class_='slick-slider carousal-list center slick-initialized')

context = {'data': []}

for case in cases:
    data = {}
    product_name = case.find('h2', class_='mu-item__title')
    if not product_name:
        data['product_name'] = 'Not available'
    else:
        data['product_name'] = product_name.text

    context['data'].append(data)

workbook = xlsxwriter.Workbook('HospitalityUnited.xlsx')
worksheet = workbook.add_worksheet('Sheet1')

row = 0
col = 0

for date in context['data']:
    worksheet.write(row, col, date['product_name'])
    worksheet.write(row, col + 1, 0)
    worksheet.write(row, col + 2,
                    'for more information visit https://www.manutd.com/en/Executive-Club/hospitality-options')
    row += 1

workbook.close()
