from bs4 import BeautifulSoup
import requests

# Recieving the site's html
site_html = requests.get('https://www.csuchico.edu/cost.shtml')
if site_html.status_code != 200:
    print(f'Error has occureed, Status Code: {site_html.status_code}')
    exit()

# Creating beautiful Soup
soup = BeautifulSoup(site_html.text, 'lxml')

# Capture the data
underGrad = [0,0]
CredGrad  = [0,0]
Grad      = [0,0]

tuitionBody  = soup.find('div', class_ = 'table-scroll')
tuitionTable = tuitionBody.find('table')
tuitionData  = tuitionTable.find_all('td')

underGrad[0] = str(tuitionData[1]).split('<')[1].lstrip('td>')
underGrad[1] = str(tuitionData[2]).split('<')[1].lstrip('td>')
CredGrad[0]  = str(tuitionData[4]).split('<')[1].lstrip('td>')
CredGrad[1]  = str(tuitionData[5]).split('<')[1].lstrip('td>')
Grad[0]      = str(tuitionData[7]).split('<')[1].lstrip('td>')
Grad[1]      = str(tuitionData[8]).split('<')[1].lstrip('td>')

# Printing the Data
print('\tStudent Type' + '\t 0-6 units' + '\t 6.1+ units')
print('--------------------------------------------------')
print('\tUnderGradute\t', underGrad[0], '\t', underGrad[1])
print('\tCredential\t', CredGrad[0], '\t', CredGrad[1])
print('\tGrad\t\t', Grad[0], '\t', Grad[1])
