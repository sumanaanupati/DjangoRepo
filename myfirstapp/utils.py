import requests

def get_data_from_url():
    resp = requests.get(url='https://api.covid19api.com/summary')
    if resp.status_code == 200:
        print('Api response success')
        return resp.json()

def get_country_data(country_name):
    resp = requests.get(url='https://api.covid19api.com/total/country/'+country_name)
    if resp.status_code == 200:
        print('Api response success')
        return resp.json()