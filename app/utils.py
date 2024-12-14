# utils.py

import requests
import re

BLYNK_AUTH_TOKEN = 'HS4ecLdcxo7zVhkyzCUtpRF4kS8mE_hV'
#BLYNK_BASE_URL = 'http://blynk-cloud.com'

def get_blynk_data(pin):
    # Blynk API endpoint for reading pin data
    url = f"https://blynk.cloud/external/api/get?token=HS4ecLdcxo7zVhkyzCUtpRF4kS8mE_hV&pin={pin}"
    
    # Make a GET request to the Blynk server
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text.strip('[]').strip("'")
            
            print(f"Raw data from Blynk: {data}")  # Debugging line
            
            # If pin is V6 or V7, parse the data into a dictionary
            if pin in ['V6', 'V7']:
                
                data = data.replace(" ", "")
                # Find all letter-number pairs, e.g., [('F', '1'), ('H', '0'), ('IR', '1'), ('G', '89')]
                matches = re.findall(r'([A-Z0-9]+)(?::(\d+))?', data)
                # Convert to dictionary where key is the identifier and value is its number
                parsed_data = {key: value for key, value in matches}
                print(parsed_data)
                return parsed_data  # e.g., {'F': '1', 'H': '0', 'IR': '1', 'G': '89'}
               
            # For other pins, return normal comma-separated split
            return data.split(',')
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return None