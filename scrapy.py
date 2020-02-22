from bs4 import BeautifulSoup
import requests
import re
import json


# Source to scrape from
source = requests.get('https://results.smu.edu.in/smit/results_grade_view.php?exam=45&subject=10933').text

soup = BeautifulSoup(source, 'html.parser').text

# To store scraped data
data = []

#splitting the result in different lines
results = soup.splitlines()

#scraping elements from individual line
for result in results :
    if re.search("^20*", result) :
        r_list = result.split()
        data.append({
        	'reg_no':r_list[0],
        	'internal':r_list[1],
        	'external':r_list[2],
        	'total':r_list[3],
        	'grade':r_list[4]
        	})



# saving the data inside a json file
with open('result.json', 'w') as json_file:
    json.dump(data, json_file)
