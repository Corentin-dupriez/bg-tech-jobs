import datetime

import requests
from bs4 import BeautifulSoup

def request_to_dev_bg(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def find_categories(soup: BeautifulSoup) -> dict[str, str]:
    data = {'date': datetime.datetime.today().strftime('%Y-%m-%d')}

    categories = soup.find_all(class_='category-block')

    for category in categories:
        children = category.find_all(class_='child-term')
        category_info = category.find(class_='category-block-title-holder').find('a').text.split()
        data[''.join(category_info[0:-1])] = category_info[-1]
        for child in children:
            child_info = child.text.split()
            data[''.join(child_info[0:-1])] = child_info[-1]

    junior, management = soup.find_all(class_='title-count-wrap')
    junior = junior.text.split()[-1]
    management = management.text.split()[-1]
    data['Junior'] = junior
    data['ITManagement'] = management

    return data

def order_data(data: dict) -> dict[str, int]:
    return {
        'date': data['date'],
        'backenddevelopment': data['BackendDevelopment'],
        'java': data['Java'],
        'dotnet': data['.NET'],
        'php': data['PHP'],
        'ccplusplusembeded': data['C/C++/Embedded'],
        'python': data['Python'],
        'ruby': data['Ruby'],
        'go': data['Go'],
        'nodejs': data['Node.js'],
        'frontenddevelopment': data['FrontendDevelopment'],
        'js': data['JavaScript'],
        'react': data['React'],
        'angular': data['Angular'],
        'vue': data['Vue.js'],
        'fullstackdevelopment': data['FullstackDevelopment'],
        'pmandba': data['PM/BAandmore'],
        'qa': data['QualityAssurance'],
        'devops': data['DevOps'],
        'databaseengineer': data['DatabaseEngineer'],
        'cybersecurity': data['Cybersecurity'],
        'sysadmin': data['SysAdmin'],
        'datawarehouse': data['ETL/Datawarehouse'],
        'bigdata': data['BigData'],
        'datavisualization': data['BI/Datavisualization'],
        'mlandai': data['ML/AI/Datamodelling'],
        'ui_ux': data['UI/UX,Arts'],
        'technical_support': data['TechnicalSupport'],
        'mobile': data['MobileDevelopment'],
        'ios': data['iOS'],
        'android': data['Android'],
        'itmanagement': data['ITManagement'],
        'junior': data['Junior'],
    }
