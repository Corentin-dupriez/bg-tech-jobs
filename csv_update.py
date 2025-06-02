import os
import csv

file_path = os.path.join(os.getcwd(), 'data' , 'cleaned_dataset.csv')

def find_last_id_and_date(file) -> tuple:
    with open(file_path, 'r') as csv_file:
        last_row = csv_file.readlines()[-1]
        last_id = last_row.split(',')[0]
        last_date = last_row.split(',')[1]
    return last_id, last_date

def get_new_row_number() -> int:
    return int(find_last_id_and_date(file_path)[0]) + 1

def check_if_date_exists(update_date: str) -> bool:
    if update_date == find_last_id_and_date(file_path)[1]:
        return True
    return False

def write_new_line(dict):
    if not check_if_date_exists(dict['date']):
        with open(file_path, 'a') as csv_file:
            new_row_number = get_new_row_number()
            data_to_write = {'rownum' : new_row_number, **dict}
            writer = csv.writer(csv_file)
            writer.writerow(data_to_write.values())
    else:
        print('No data to update, the file is up to date.')

