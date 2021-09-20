import bs4
import requests
import xlsxwriter

url = "https://tickets.manutd.com/hospitality"

result = requests.get(url)
print(result)
soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('div', class_='dataItem item_background item_data_background')

context = {'data': []}

for case in cases:
    data = {}
    db_title = case.find('span', class_='small_text_d name')
    title = db_title.text.replace('\n', '').replace('- Hospitality', '')
    db_description = case.find('div', class_='small_text_a dates itemsDateRange')
    description = db_description.text.replace('\n', '').replace('Next up for you', '')
    if not title:
        data['title'] = 'No data available'
    else:
        data['title'] = title[21:]
    if not description:
        data['description'] = 'No data available'
    else:
        data['description'] = description

    context['data'].append(data)

workbook = xlsxwriter.Workbook('ManUnited.xlsx')
worksheet = workbook.add_worksheet('Fixture')

row = 0
col = 0

for date in context['data']:
    worksheet.write(row, col, date['title'])
    worksheet.write(row, col + 1, date['description'])
    row += 1

workbook.close()

# pt update/delete la feli
# class ReturnToRecipe():
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().get(request, *args, **kwargs)
#
#     def get_success_url(self):
#         return f"/add-ingredient/{self.object.recipre.id}/"
