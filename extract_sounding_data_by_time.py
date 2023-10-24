import requests
from requests.exceptions import RequestException
import numpy as np

max_retries = 3

for year in range(2020, 2021):
    for month in range(4, 13):
        if month == 2:
            dates = np.arange(1, 29)
        elif month == 4 or month == 6 or month == 9 or month == 11:
            dates = np.arange(1, 31)
        else:
            dates = np.arange(1, 32)

        requests.packages.urllib3.disable_warnings()

        for date in dates:
            url = f"https://weather.uwyo.edu/cgi-bin/sounding?region=europe&TYPE=TEXT%3ALIST&YEAR={year}&MONTH={month}&FROM={date}12&TO={date}12&STNM=14240"

            response = requests.get(url, verify=False)

            for attempt in range(max_retries):
                try:
                    response = requests.get(url, verify=False)

                    if response.status_code == 200:
                        with open(
                            f"data/soundings/zg_12.txt", "a", encoding="utf-8"
                        ) as txt_file:
                            txt_file.write(response.text)

                        print(
                            f"Extracted sounding data for {date}/{month}/{year} to zg_12.txt."
                        )

                        if month == 6 or month == 7 or month == 8:
                            with open(
                                f"data/soundings/zg_12_JJA.txt", "a", encoding="utf-8"
                            ) as txt_file:
                                txt_file.write(response.text)

                            print(
                                f"Extracted sounding data for {date}/{month}/{year} to zg_12_JJA.txt."
                            )

                        if month == 12 or month == 1 or month == 2:
                            with open(
                                f"data/soundings/zg_12_DJF.txt", "a", encoding="utf-8"
                            ) as txt_file:
                                txt_file.write(response.text)

                            print(
                                f"Extracted sounding data for {date}/{month}/{year} to zg_12_DJF.txt."
                            )

                        break
                except RequestException as e:
                    print(
                        f"Failed to retrieve data for {date}/{month}/{year}. Attempt {attempt + 1}/{max_retries}"
                    )
                    if attempt == max_retries - 1:
                        print("Max retries reached. Moving on to the next month.")
                        break

            url = f"https://weather.uwyo.edu/cgi-bin/sounding?region=europe&TYPE=TEXT%3ALIST&YEAR={year}&MONTH={month}&FROM={date}00&TO={date}00&STNM=14430"

            response = requests.get(url, verify=False)

            for attempt in range(max_retries):
                try:
                    response = requests.get(url, verify=False)

                    if response.status_code == 200:
                        with open(
                            f"data/soundings/zd_00.txt", "a", encoding="utf-8"
                        ) as txt_file:
                            txt_file.write(response.text)

                        print(
                            f"Extracted sounding data for {date}/{month}/{year} to zd_00.txt."
                        )

                        if month == 6 or month == 7 or month == 8:
                            with open(
                                f"data/soundings/zd_00_JJA.txt", "a", encoding="utf-8"
                            ) as txt_file:
                                txt_file.write(response.text)

                            print(
                                f"Extracted sounding data for {date}/{month}/{year} to zd_00_JJA.txt."
                            )

                        if month == 12 or month == 1 or month == 2:
                            with open(
                                f"data/soundings/zd_00_DJF.txt", "a", encoding="utf-8"
                            ) as txt_file:
                                txt_file.write(response.text)

                            print(
                                f"Extracted sounding data for {date}/{month}/{year} to zd_00_DJF.txt."
                            )

                        break
                except RequestException as e:
                    print(
                        f"Failed to retrieve data for {date}/{month}/{year}. Attempt {attempt + 1}/{max_retries}"
                    )
                    if attempt == max_retries - 1:
                        print("Max retries reached. Moving on to the next month.")
                        break

            url = f"https://weather.uwyo.edu/cgi-bin/sounding?region=europe&TYPE=TEXT%3ALIST&YEAR={year}&MONTH={month}&FROM={date}12&TO={date}12&STNM=14430"

            response = requests.get(url, verify=False)

            for attempt in range(max_retries):
                try:
                    response = requests.get(url, verify=False)

                    if response.status_code == 200:
                        with open(
                            f"data/soundings/zd_12.txt", "a", encoding="utf-8"
                        ) as txt_file:
                            txt_file.write(response.text)

                        print(
                            f"Extracted sounding data for {date}/{month}/{year} to zd_12.txt."
                        )

                        if month == 6 or month == 7 or month == 8:
                            with open(
                                f"data/soundings/zd_12_JJA.txt", "a", encoding="utf-8"
                            ) as txt_file:
                                txt_file.write(response.text)

                            print(
                                f"Extracted sounding data for {date}/{month}/{year} to zd_12_JJA.txt."
                            )

                        if month == 12 or month == 1 or month == 2:
                            with open(
                                f"data/soundings/zd_12_DJF.txt", "a", encoding="utf-8"
                            ) as txt_file:
                                txt_file.write(response.text)

                            print(
                                f"Extracted sounding data for {date}/{month}/{year} to zd_12_DJF.txt."
                            )

                        break
                except RequestException as e:
                    print(
                        f"Failed to retrieve data for {date}/{month}/{year}. Attempt {attempt + 1}/{max_retries}"
                    )
                    if attempt == max_retries - 1:
                        print("Max retries reached. Moving on to the next month.")
                        break
