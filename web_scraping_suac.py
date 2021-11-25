from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import requests
import ConexionDB 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import sqlite3

num = 23910
while num <= 24562:
    try:
        num2 = "0" * (6 - len(str(num))) + str(num)
        tramite = '0517-' + num2 + "/2018"
        print(tramite)
        driver = webdriver.Chrome(executable_path="C:\driverchrome\chromedriver_win32\chromedriver.exe")
        driver.get("https://consultasuac.cba.gov.ar/")
        time.sleep(5)

        try:
            mbox= driver.find_element_by_xpath('//*[@id="txtSearch"]')
            mbox.send_keys(tramite)
            driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
            time.sleep(5)
            page = driver.page_source
            soup = bs(page, 'lxml')
            #titulos = soup.find_all('dt')
            info = soup.find_all('dd')
            driver.find_element_by_xpath('//*[@id="tabDetailsSelector"]/li[2]/a').click()
            time.sleep(3)
            page = driver.page_source
            soup = bs(page, 'lxml')
            #hdr_titulos = soup.find_all('th')
            hdr_info = soup.find_all('td')
            driver.close()
        except NoSuchElementException:
            num += 1
            driver.close()
            continue

        consulta_sticker = (info[0].text,)
        conexion2 = ConexionDB.ConnectionDB2() 
        conexion2.DBHojadeRuta()
        respuesta = conexion2.consulta(consulta_sticker)
        if len(respuesta) > 0:
            print(f'el número de trámite {tramite} ya existe en la Base de Datos')
            num += 1
            continue


        datos = []
        for i in range(len(info)):
            datos.append(info[i].text)

        if len(info) == 16:
            conexion = ConexionDB.ConnectionDB() 
            conexion.DBSuac()
            conexion.carga_info(datos) 
        else:
            conexion = ConexionDB.ConnectionDB3() 
            conexion.DBSuac2()
            conexion.carga_info(datos) 

        try:
            datoshdr = []
            if len(hdr_info) > 5:
                cont = 0
                for i in range(int(len(hdr_info)/5)):
                    datoshdr.append(info[0].text)
                    for j in range(5):
                        datoshdr.append(hdr_info[j+cont].text)
                    conexion2 = ConexionDB.ConnectionDB2() 
                    conexion2.DBHojadeRuta()
                    conexion2.carga_hdr(datoshdr) 
                    datoshdr = []
                    cont += 5
            else:            
                for i in range(len(hdr_info)):
                    datoshdr.append(info[0].text)
                    datoshdr.append(hdr_info[i].text)
                    #print(hdr_info[i])
                    #print(len(hdr_info[i]))
                    conexion2 = ConexionDB.ConnectionDB2() 
                    conexion2.DBHojadeRuta()
                    conexion2.carga_hdr(datoshdr) 
            num += 1
        except sqlite3.ProgrammingError:
            num += 1
            continue

    except WebDriverException:
        continue