import csv

MIN_POPULATION=50000

COUNTRIES = ["Austria","Slovenia","Croatia", "German",
 "Switzerland","Liechtenstein", "Slovakia", "Czechia","Romania",
 "Italy", "Norway", "Sweden", "New Zealand", "Canada", "Belgium", "Netherlands",
 "Luxembourg", "Ireland","United Kingdom"
 ]


def filter_cities():
    with open('worldcities.csv',encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        rows = []
        for i,row in enumerate(readCSV):
            if i==0:
                rows.append(row)
                continue
            if len(row)<3:
                continue
            if row[1] not in COUNTRIES:
                continue
            print(row)
            if row[2]=='':
                rows.append(row)
                continue

            if int(row[2])>MIN_POPULATION:
                rows.append(row)


    with open('filtered_cities.csv', 'w', newline='',encoding='utf-8') as csvfile:
        filtered_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in rows: # other rows, sorted
            filtered_writer.writerow(row)

filter_cities()
