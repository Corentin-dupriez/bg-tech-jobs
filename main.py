from scraper.scraper import request_to_dev_bg, find_categories, order_data
from update_csv_data.csv_update import write_new_line

def main():
    print('Starting scraping...')
    soup = request_to_dev_bg('https://dev.bg/?_gl=1*1w4zod2*_up*MQ..*_gs*MQ..&gclid=Cj0KCQjw2tHABhCiARIsANZzDWrzO32ZPkWR4quQZSgsf9XGyB6NFqlrDQEXgud5YLhoigvJPqdeB3IaAp44EALw_wcB&gbraid=0AAAAABttMT6wF3neoIVuruDltTy-Fh7cY')
    print('Finished scraping!')
    print('Updating dataset...')
    updated_data = find_categories(soup)
    ordered_data = order_data(updated_data)
    write_new_line(ordered_data)
    print('Done!')

if __name__ == '__main__':
    main()