import bs4
import requests
import xlsxwriter

url = 'https://hospitality.mancity.com/hospitality/hospitality-suites?_gl=1*14eiesj*_ga*MzUzMjQ4OTI5LjE2MzAzMDMzOTU' \
      '.*_ga_83D496C6PL*MTYzMTI3NDQ1OS4xOS4wLjE2MzEyNzQ0NjMuNTY. '
result = requests.get(url)

soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('div', class_='col-lg-6 col-md-7 col-sm-7 col-7')

context = {'data': []}

for case in cases:
    data = {}
    product_name = case.find('h3', class_='')
    product_price = case.find('strong', class_='')
    product_description = case.find('li', class_='')
    if not product_name:
        data['product_name'] = 'Not available'
    else:
        data['product_name'] = product_name.text.replace("'", "")
    if not product_price:
        data['product_price'] = 'Not available'
    else:
        data['product_price'] = product_price.text
    if not product_description:
        data['product_description'] = 'Not available'
    else:
        data['product_description'] = product_description.text

    context['data'].append(data)

workbook = xlsxwriter.Workbook('Hospitality.xlsx')
worksheet = workbook.add_worksheet('Sheet1')

row = 0
col = 0

for date in context['data']:
    worksheet.write(row, col, date['product_name'])
    worksheet.write(row, col + 1, date['product_price'])
    worksheet.write(row, col + 2, date['product_description'])
    row += 1

workbook.close()
