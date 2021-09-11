import bs4
import requests

url = "https://tickets.mancity.com/en-GB/categories/Men's%20Tickets"

result = requests.get(url)

soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('div', class_='dataItem item_background item_data_background')

for case in cases:
    title = case.find('span', class_='small_text_d name')
    fara_n = title.text.replace('\n', '')
    print(fara_n[21:])
