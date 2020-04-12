from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import requests

URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


covidMain = soup.find(class_ = 'content-inner')

# mainHighlights contains coronaVirus count(total, recovered and death)
mainHighlights = covidMain.find_all('div', id = 'maincounter-wrap')

for mainHighlight in mainHighlights:
    """
    [title]: title of the mainHighlight
    [value]: value of the title
    """
    title = mainHighlight.find('h1')
    value = mainHighlight.find(class_ ='maincounter-number')
    if None in (title, value):
        continue
    else:
        print(title.text.strip())
        print(value.text.strip())
    
print('----')



# Checking World table
covidMainRows = soup.find(class_ = 'tab-content', id='nav-tabContent')
# find table
# find all tr inside that table
tables = covidMainRows.find('table', id= 'main_table_countries_today')
rows = tables.find_all('tr')


# now access each element of rows
for row in rows:
    country = row.find('a', class_ = 'mt_a')
    total_case = row.find(style = 'font-weight: bold; text-align:right')
    new_case = row.find(style = 'font-weight: bold; text-align:right;background-color:#FFEEAA;')
    total_death = row.find(style = 'font-weight: bold; text-align:right;')
    new_death = row.find(style = 'font-weight: bold; text-align:right;background-color:red; color:white;')
    active_cases = row.find(style = 'text-align:right;font-weight:bold;')
    # total recovered problem 
    # total_recovered = total_case - total_death - active_cases

    # if None in (country, total_case, new_case, total_death, new_death, total_recovered, active_cases):
    # # if (country, total_case, new_case, total_death, new_death, total_recovered, active_cases )is None:
    #     continue
    # else:
    #     print(f'country : {country.text.strip()}')
    #     print(f'total case : {total_case.text.strip()}')
    #     print(f'new case : {new_case.text.strip()}')
    #     print(f'total death : {total_death.text.strip()}')
    #     print(f'new death : {new_death.text.strip()}')
    #     print(f'total recovered : {total_recovered.text.strip()}')
    #     print(f'active cases : {active_cases.text.strip()}')

    if country is None:
        continue
    else:
        print(f'country : {country.text.strip()} /', end ='')

    if total_case is None:
        print(f'total case : 0')
    else:
        print(f'total case : {total_case.text.strip()} / ' , end ='')

    if new_case is None:
        print(f'new case : 0')
    else:
        print(f'new case : {new_case.text.strip()} / ' , end ='')
    
    if total_death is None:
        print(f'total death: 0')
    else:
        print(f'total death: {total_death.text.strip()} / ' , end ='')
    
    if new_death is None:
        print(f'new death : 0')
    else:
        print(f'new death : {new_death.text.strip()} / ' , end ='')
    
    if active_cases is None:
        print(f'active cases : 0')
    else:
        print(f'active cases : {active_cases.text.strip()} / ' , end ='')
    
    
    # print(f'total recovered: {total_recovered.text.strip()} / ' , end ='')
    print('---')
    
    






