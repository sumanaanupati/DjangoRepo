import requests

def get_data_from_url():
    resp = requests.get(url='https://api.covid19api.com/summary')
    if resp.status_code == 200:
        print('Api response success')
        return resp.json()

if __name__ == "__main__":
    get_data_from_url()