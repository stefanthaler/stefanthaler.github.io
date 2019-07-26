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
data_sources = [
    loadfrom_csv("2017_freedom_index"),
    loadfrom_csv("2018_corruption_perception_index"),
    loadfrom_csv("2017_un_ihdi"),
    loadfrom_csv("2015_2016_homicide_rate"),
    loadfrom_csv("2018_ease_of_doing_business"),
    loadfrom_csv("2019_press_freedom_index"),
    loadfrom_csv("2018_pension_index"),
    loadfrom_csv("2018_healthcare_index"),
    loadfrom_csv("2000_who_health_ranking"),
    loadfrom_csv("2017_internet_speed"),
    loadfrom_csv("2019_average_percipitaiton"),
    loadfrom_csv("2019_average_temperatures"),
    loadfrom_csv("2018_corporate_tax_rates"),
    loadfrom_csv("2019_employee_social_contribution"),
    loadfrom_csv("2019_employer_social_contribution"),
    loadfrom_csv("2019_individual_tax_rates"),
    loadfrom_csv("2019_inflation_rate"),
    loadfrom_csv("2019_vat"),

]



merged = []

merged.append( ["Country"] + list(countries_and_aliases.keys()) )

for data_source in data_sources:
    columns = data_source[0][1:]
    content = data_source[1][:,1:]
    countries_in_source = data_source[1][:,0]
    #print(columns)
    #print(content)
    #print(content.shape)
    for i,col in enumerate(columns):
        row = [col] # name of the column

        # add data column
        for country in countries_and_aliases.keys():
            country_and_aliases = [country] + countries_and_aliases[country]
            country_in_source = False
            country_index = -1
            for r, source_country in enumerate(countries_in_source):
                sc = source_country.strip("#* ")
                #print(sc, country_and_aliases)
                #print(sc in country_and_aliases)
                if sc in country_and_aliases:
                    country_in_source=True
                    country_index=r
                    break

            if country_in_source:
                row.append(content[country_index,i].strip())
            else:
                row.append("-")
        merged.append(row)

merged_t = (np.array(merged).transpose())

import csv
with open('merged.csv', 'w', newline='') as csvfile:
    merged_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    merged_writer.writerow(list(merged_t[0,:])) # header
    for row in merged_t[1:,:]: # other rows
        merged_writer.writerow(list(row))

def has_value(elem):
    return elem and not elem=="-"

def row_fits_filter(row):

    # more than half of fields are empty
    empty_elements = 0
    for elem in row:
        if not has_value(elem):
            empty_elements+=1
    if empty_elements>len(row)*0.5:
        return False

    # Freedom
    if has_value(row[1]) and row[1] not in ["Free"]:
        return False

    # IHDI
    if has_value(row[7]) and  float(row[7])<=0.70:
        return False

    # Income Gini
    if has_value(row[19]) and (float(row[19])>=35.0 ):
        return False

    # Intentional Homicide Rate ( average EU 1, average high income 2)
    if has_value(row[20]) and float(row[20])>=3.0:
        return False

    return True

import csv
with open('merged_filtered.csv', 'w', newline='') as csvfile:
    merged_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    merged_writer.writerow(list(merged_t[0,:])) # header
    for row in merged_t[1:,:]: # other rows
        if row_fits_filter(row):
            merged_writer.writerow(list(row))
