from bs4 import BeautifulSoup
import requests

print("Wikisite Scraper - TCP and UDP port numbers")

r = requests.get('https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers')
if r.status_code == 200:
    print('\nFetching site: SUCCESS')
elif r.status_code == 301:
    print('\nFetching site: Permanent Redirection')
elif r.status_code == 302: 
    print('Fetching site: Temporary Redirection')
elif r.status_code == 404:
    print('Fetching Site: FAILED, Site Not Found')
elif r.status_code == 500: 
    print('Fetching Site: FAILED, Internal Server Error')

site = BeautifulSoup(r.text, 'lxml')

table = site.find("table", class_ = 'sortable')
row = table.find("tbody")

print(row.find('tr'))

#for data in row.find_all('tr'):
    
    #values = data.find_all('td')
    #print('Port: ' + str(values[0]))
