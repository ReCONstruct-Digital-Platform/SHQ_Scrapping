import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

opts = webdriver.FirefoxOptions()
opts.add_argument('--headless')

df=pd.read_csv("Individual_COOP.csv")
specific_column=df["Link"].tolist()

n=1
final_tmp = []
for url in specific_column:
    driver = webdriver.Firefox(options=opts)
    driver.get(url)

    element_table1 = driver.find_element(By.CLASS_NAME, "adresse")
    str_element_table1 = element_table1.text
    split_with_space = element_table1.text.split("\n")
    split_with_space = split_with_space[1:]
    spl_word = ' :'
    tmp_list_1 =[]
    for ele in split_with_space:
        tmp_list_1.append(ele.split(spl_word, 1))
    headers_1, values_1 = zip(*((x[0], x[1:]) for x in tmp_list_1))
    flat_list_final_1 = [item for sublist in values_1 for item in sublist]

    element_table2 = driver.find_element(By.CLASS_NAME, "nblogement")
    split_with_space_2 = element_table2.text.split("\n")
    split_with_space_2_final_2 = split_with_space_2[5:][0].split(" ")[2:]
    flat_list_final_1.extend(split_with_space_2_final_2)
    final_tmp.append(flat_list_final_1)
    n +=1
    if n ==10:
        break

#write to csv file
fields = ['Adresse', 'Code postal', 'Téléphone', 'Téléphone sans frais', 'Télécopieur', 'Courriel', 'Site Internet', 'Total: PSL', 'Total: HLM', 'Total: Total']
#filename = "Individual_OSBL.csv"
filename = "new.csv"

#write to csv file
with open(filename, 'w', encoding='UTF-8',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(final_tmp)
csvfile.close()