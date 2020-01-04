import csv

def print_output(MASSAGE_DATA_DICT):
    #print(f'MASSAGE_DATA_DICT {MASSAGE_DATA_DICT}')
    print(f'\t Total Schools: {MASSAGE_DATA_DICT["TOTAL_SCHOOL"]}')
    print (f'\t Schools by State:')
    for state_name, school_count in MASSAGE_DATA_DICT["SCHOOLS_BY_STATE"].items() : print (f'\t\t {state_name} : {school_count}')

    print(f'\t Schools by Metro-Centric Locale:')
    for mlocale, school_count in MASSAGE_DATA_DICT["SCHOOLS_BY_MLOCALE"].items() : print (f'\t\t {mlocale} : {school_count}')
    city_name_of_max_school_count = (max(MASSAGE_DATA_DICT['CITY_SCHOOL_COUNT'].keys(), key=(lambda key: MASSAGE_DATA_DICT['CITY_SCHOOL_COUNT'][key])))
    print (f'City with Most Schools: {city_name_of_max_school_count } ({MASSAGE_DATA_DICT["CITY_SCHOOL_COUNT"][city_name_of_max_school_count]})')

#def print_counts():
with open('school_data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    MASSAGE_DATA_DICT = {
        'TOTAL_SCHOOL': 0,
        'SCHOOLS_BY_STATE': {},
        'SCHOOLS_BY_MLOCALE': {},
        'CITY_SCHOOL_COUNT': {}
    }
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        # for dict_key, row_value in row.items():
        #     print (dict_key)
        #     print (row_value)
        #print(f'\t{row["SCHNAM05"]} works in the {row["LCITY05"]} department, and was born in {row["LSTATE05"]}.')
        line_count += 1
        MASSAGE_DATA_DICT['SCHOOLS_BY_STATE'][row["LSTATE05"]] = MASSAGE_DATA_DICT['SCHOOLS_BY_STATE'].get(row['LSTATE05'], 0) + 1
        MASSAGE_DATA_DICT['SCHOOLS_BY_MLOCALE'][row['MLOCALE']] = MASSAGE_DATA_DICT['SCHOOLS_BY_MLOCALE'].get(row['MLOCALE'], 0) + 1
        MASSAGE_DATA_DICT['CITY_SCHOOL_COUNT'][row['LCITY05']] = MASSAGE_DATA_DICT['CITY_SCHOOL_COUNT'].get(
            row['LCITY05'], 0) + 1

        MASSAGE_DATA_DICT['TOTAL_SCHOOL'] += 1
        # if line_count > 500:
        #     break
    print_output(MASSAGE_DATA_DICT)
    print(f'Processed {line_count} lines.')

