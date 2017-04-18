import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.desired_capabilties import DesiredCapabilities

from bs4 import BeautifulSoup

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


def find_flights():
    url = "https://www.google.de/flights/#search;f=MUC,ZMU;t=LAS;d=2017-05-15;r=2017-05-28"
    driver = webdriver.PhantomJS()
    dcaps = dict(DesiredCapabilities.PHANTOMJS)
    dcaps["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")
    driver = webdriver.PhantomJS(desired_capabilities=dcaps,service_args=['--ignore-ssl-errors=true'])
    driver.implicitly_wait(5)
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, " span.OMOBOQD-u-b")))

    s = BeautifulSoup(driver.page_source, "lxml")
    best_price = s.findAll('span', 'OMOBOQD-mb-p')

    cities = s.findAll('span', 'OMOBOQD-mb-u')

    hlist = []
    fares = pd.DataFrame(hlist, columns=['price'])
    px = [for x in fares['price']]
    ff = pd.DataFrame(px, columns=['fare']).reset_index()

    X = StandardScaler().fit_transform(ff)
    db = DBSCAN(eps=5, min_samples=1).fit(X)