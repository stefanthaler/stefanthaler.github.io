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
    loadfrom_csv("2016_healthexp_per_capita"),

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

    # HDI
    if has_value(row[6]) and  float(row[6])<=0.80:
        return False
    # IHDI
    if has_value(row[7]) and  float(row[7])<=0.70:
        return False

    # Quintile Ratio
    if has_value(row[17]) and (float(row[17])>=8.0 ):
        return False

    # Intentional Homicide Rate ( average EU 1, average high income 2)
    if has_value(row[20]) and float(row[20])>=3.0:
        return False

    return True



import csv

filtered_t = []

with open('merged_filtered.csv', 'w', newline='') as csvfile:
    merged_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    merged_writer.writerow(list(merged_t[0,:])) # header
    filtered_t.append(list(merged_t[0,:]))
    for row in merged_t[1:,:]: # other rows
        if row_fits_filter(row):
            merged_writer.writerow(list(row) )
            filtered_t.append(row)

scaled_t = np.array(filtered_t)

criteria = [ # high is good, so invert where high is bad
    ( 7,3.0, False),# IHDI high is good
    (19,1.0, True),# gini high is bad
    (21,3.0, True),# ease of doing business
    (22,0.5, True),# press freedom
    (23,2.0, False),# pension index
    (41,3.0, True),# corporate tax high is bad
    (44,3.0, True),# individual tax high is bad
    (45,0.5, True),# inflation rate is bad
    (48,0.5, True),# high VAT rate is bad
]



def sort_criteria(row):
    num_elem =0
    sum  = 0
    for crit in criteria:
        if has_value(row[crit[0]]):
            sum+=float(row[crit[0]])*crit[1]
            num_elem+=crit[1]

    return round(sum/float(num_elem),2)

for crit in criteria:
    c = crit[0]
    col =  scaled_t[1:,c]
    col_min = 1000000
    col_max = 0
    invert = crit[2]
    for e in col:
        if has_value(e):
            if float(e)<col_min:
                col_min=float(e)
            if float(e)>col_max:
                col_max=float(e)

    for i,e in enumerate(col):
        if has_value(e):
            new_e = round(100*(float(e)-col_min)/float(col_max-col_min),1) # scale between 0-100
            if invert:
                new_e = 100-new_e
            scaled_t[i+1,c]=new_e

sort_order = []
for row in scaled_t[1:,:]: # other rows
    sort_order.append(sort_criteria(row))

sort_order = -np.array(sort_order)
sorted_indizes = np.argsort(sort_order)


with open('scaled.csv', 'w', newline='') as csvfile:
    merged_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    merged_writer.writerow(list(scaled_t[0,:])+["Sort criteria"]) # header
    for row in scaled_t[1:,:][sorted_indizes]: # other rows, sorted
        merged_writer.writerow(list(row) + [sort_criteria(row)])
