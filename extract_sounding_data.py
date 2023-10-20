import requests
from requests.exceptions import RequestException

max_retries = 3

for year in range(2011, 2021):
    for month in range(1, 13):
        requests.packages.urllib3.disable_warnings()

        if month == 2:
            endDate = 2812
        elif month == 4 or month == 6 or month == 9 or month == 11:
            endDate = 3012
        else:
            endDate = 3112

        url = f"https://weather.uwyo.edu/cgi-bin/sounding?region=europe&TYPE=TEXT%3ALIST&YEAR={year}&MONTH={month}&FROM=0100&TO={endDate}&STNM=14240"

        response = requests.get(url, verify=False)

        for attempt in range(max_retries):
            try:
                response = requests.get(url, verify=False)

                if response.status_code == 200:
                    with open(
                        "data/soundings/zg.txt", "a", encoding="utf-8"
                    ) as txt_file:
                        txt_file.write(response.text)

                    print(f"Extracted sounding data for {month}/{year} to zg.txt.")
                    break
            except RequestException as e:
                print(
                    f"Failed to retrieve data for {month}/{year}. Attempt {attempt + 1}/{max_retries}"
                )
                if attempt == max_retries - 1:
                    print("Max retries reached. Moving on to the next month.")
                    break
