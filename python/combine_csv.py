from true_type import get_type

#def read_multiple_csv(files, key_header):
def read_multiple_csv(files, key_header):
    """
    takes a list of filesnames and a key_header string to merge the files. 
    Can merge if there are different columns in the files, different records in
    the files. 
    Assumption - all the files should have the column named key_header
    example : files = ['grades.csv', 'previous_grades.csv']
    key_header = 'email'
    merged_data = read_multiple_csv(files, key_header)
    """
    data = {}
    # files = ['assignments.csv', 'discuss.csv', 'questions.csv']
    # key_header = 'email'

    for filename in files:
        file_generator = open(filename)
        headers = file_generator.next().split(',')
        headers = [h.strip() for h in headers]

        for line in file_generator:
            splits = line.split(',')
            inner_dict = {}
            for k,header in enumerate(headers):
                #assumes header is a string. probably it is
                if header is not '':
                    inner_dict[header] = int(splits[k]) if get_type(splits[k]) is int else splits[k]
            data_key = inner_dict.pop(key_header)

            try:
                z = data[data_key].copy()
            except KeyError:
                z = {}
            z.update(inner_dict)
            data[data_key] = z
    return data
            
def write_combined_csv(data, file_name='combined.csv'):
    import csv
    headers = ['email']
    headers.extend(data[data.keys()[0]].keys())
    with open(file_name) as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(headers)
        for email in data.keys():
            line = [email]
            line.extend(data[email])
            writer.writerow(line)
            


