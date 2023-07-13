import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

#write to csv file
fields = ['Name','Link']
filename = "Individual_OSBL.csv"
#filename = "Individual_COOP.csv"

driver = webdriver.Firefox()
driver.get("http://www.habitation.gouv.qc.ca/repertoire.html")

#by default, the webpage shows COOP, to select OSBL, then unquote the following code
driver.find_element(By.ID, "tx_shqrepertoire[typeorganisme][2]").click()

#change the display item on one page to be 1000, then click search
element_search = driver.find_element(By.NAME, "tx_shqrepertoire[search]")
element_select = driver.find_element(By.XPATH,'//*[@id="resultperpage"]/option[1]')
driver.execute_script("arguments[0].setAttribute('value', '1000')", element_select)
driver.find_element(By.XPATH,'//*[@id="resultperpage"]/option[1]').click()
element_search.click()


resultSet = driver.find_element(By.XPATH, "/html/body/div[1]/section[4]/div[1]/div[3]/div/ul")
options = resultSet.find_elements(By.TAG_NAME, "li")

Individual_COOP = []

#get all the coop name and url for coops
for option in options:
    name_of_coop = option.text.replace(" Voir les détails", "")
    option_expand = option.find_element(By.TAG_NAME, "a")
    tmp_list = [name_of_coop, option_expand.get_attribute("href")]
    if "\n" not in tmp_list[0]:
        Individual_COOP.append(tmp_list)

#print(Individual_COOP) -  write to csv file
#print(len(Individual_COOP)) - 706

#write to csv file
with open(filename, 'w', encoding='UTF-8',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(Individual_COOP)
csvfile.close()




