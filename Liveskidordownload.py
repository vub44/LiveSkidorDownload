from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import csv

foldername = time.strftime("%d%m%y-%H%M%S")
print(foldername)
os.mkdir("./%s" % foldername)

global classname
global posname

url = input("URL: ")

driver = webdriver.Firefox()
driver.get(url)

time.sleep(1)


liclass = driver.find_elements(By.CLASS_NAME, "li-class")
for classes in liclass:
    classbutton = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/button")
    classbutton.click()
    classes.click()
    os.mkdir("./%s/%s" % (foldername, classbutton.text))
    lipos = driver.find_elements(By.CLASS_NAME, "li-pos")
    print(classbutton.text)
    for positions in lipos:
        posbutton = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/button")
        posbutton.click()
        positions.click()
        time.sleep(0.5)
        columnelements = driver.find_elements(By.XPATH, "//tr[@data-tab='head']/th")
        columns = len(columnelements)
        rowelements = driver.find_elements(By.XPATH, "//tr[@data-id]")
        rows = len(rowelements)
        f = open("./%s/%s/%s.csv" % (foldername, classbutton.text, posbutton.text), "x")
        headerlist = []
        print(posbutton.text)
        for x in range(columns):
            columnelementpos = columnelements[x]
            headerlist.append(columnelementpos.text)
        rowlist = []
        print(headerlist)
        f = open("./%s/%s/%s.csv" % (foldername, classbutton.text, posbutton.text), "a", newline='')
        writer = csv.writer(f)
        writer.writerow(headerlist)
        f.close()
        for i in range(rows):
            rowlist = []
            rowelementpos = rowelements[i]
            for j in range(columns):
                rowelementitems = rowelementpos.find_elements(By.TAG_NAME, "td")
                rowelementtest = rowelementitems[j]
                rowlist.append(rowelementtest.text)
            print(rowlist)
            f = open("./%s/%s/%s.csv" % (foldername, classbutton.text, posbutton.text), "a", newline='')
            writer = csv.writer(f)
            writer.writerow(rowlist)
            f.close()
