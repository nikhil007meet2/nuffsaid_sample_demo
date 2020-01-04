import csv, re, datetime

def search_school():
    with open('school_data.csv', mode='r') as csv_file:
        re_pattern = r'\b\w+\b'
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:

            line_count += 1
            words = re.findall(re_pattern, row["SCHNAM05"] + row['LCITY05'] + row['LSTATE05'])
            #_gen = (itertools.permutations(words, i + 1) for i in range(len(words)))
            #all_permutations_gen = itertools.chain(*_gen)
            #yield set(' '.join(i) for i in all_permutations_gen)
            yield {'word': set(words), 'line_count': line_count, 'rec': row["SCHNAM05"] + ', ' + row['LCITY05'] + ', ' + row['LSTATE05']}
            row.clear()
            # print (all_permutations)
            # if line_count > 3:
            #     break

name = ""

while name!= "exit":
    name = input("What is your search or please enter 'exit' to end search? ")
    count = 1
    lst = []
    if name == "exit":
        print ("Thank you for visting us!")
        break
    start_dtst = datetime.datetime.now()
    f = search_school()
    for process_rec in f:
        search_node = process_rec['word'].intersection(name.upper().split(' '))
        if len(search_node) > 0:
            lst.append({'search_word': search_node, 'row': process_rec['rec']})
            count += 1
    final_search_result = sorted(lst, key= lambda x:x['search_word'], reverse=True)[:3]
    end_dtst = datetime.datetime.now()
    for idx, result in enumerate(final_search_result):
        print(f'\t\t {idx+1}. {result["row"]}')
    print('Searched in - ' + str((end_dtst - start_dtst).microseconds) + ' (micro second)')

