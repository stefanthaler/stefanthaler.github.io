import csv
import numpy as np
from countries import *
import re

def loadfrom_csv(filename, country_name_col_id=0):
    with open('data_sources/%s.csv'%filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        rows = []
        for row in readCSV:
            rows.append(row)

        header = rows[0]
        content = np.array(rows[1:])

        for c in content[:,country_name_col_id]:
            c =c.strip("#* ")

            if c.strip() in countries_and_aliases.keys():
                continue
            if c.strip() in all_country_aliases:
                continue
            print("'%s':['%s'],"%(c, c))

    return header, content

# load data
freedom_index = loadfrom_csv("2017_freedom_index");
corruption_perception_index = loadfrom_csv("2018_corruption_perception_index");
hdi = loadfrom_csv("2017_un_hdi");
homicide_rate = loadfrom_csv("2015_2016_homicide_rate");
ease_of_doing_business = loadfrom_csv("2018_ease_of_doing_business");
press_freedom = loadfrom_csv("2019_press_freedom_index")
pension_ranking = loadfrom_csv("2018_pension_index")
healthcare_ranking = loadfrom_csv("2018_healthcare_index")
# merge datasources
