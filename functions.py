import numpy as np
from sklearn.linear_model import LinearRegression
import netCDF4 as nc


def load_data(file_path, variable):
    file = nc.Dataset(file_path, "r")
    values = file.variables[variable][:].data
    file.close()

    if variable == "t":
        return values - 273.15
    elif variable == "q":
        return values * 1000
    else:
        return values


def get_climatology_by_level(values, levels):
    climatology_by_level = []

    for level in range(len(levels)):
        level_total = []
        for time_step in range(len(values)):
            if (len(values) == 2):
                level_total.append(
                    (values[0][time_step][level][0][0] + values[1][time_step][level][0][0]) / 2)
            else:
                level_total.append(values[time_step][level][0][0])

        climatology_by_level.append(np.mean(level_total))

    return climatology_by_level


def get_trend(values, levels):
    slopes = []
    climatology_by_level = get_climatology_by_level(values, levels)

    for level in range(len(levels)):
        anomalies_by_year = []
        sum = 0
        counter = 0

        for time_step in range(996):
            if (len(values) == 2):
                sum = sum + ((values[0][time_step][level][0][0] +
                              values[1][time_step][level][0][0]) / 2)
            else:
                sum += values[time_step][level][0][0]

            if time_step < 12 and counter == 11 or time_step > 12 and counter == 12:
                anomalies_by_year.append(
                    sum / 12 - climatology_by_level[level])
                sum = 0
                counter = 0

            counter += 1

        years = np.arange(1940, 2023, 1).reshape(-1, 1)

        model = LinearRegression().fit(years, anomalies_by_year)
        slopes.append(model.coef_ * 10)

    return slopes


def get_anomalies_by_year_and_level(values, levels):
    climatology_by_level = get_climatology_by_level(values, levels)
    anomalies_by_level = []

    for level in range(len(levels)):
        yearly_averages = []
        sum = 0
        counter = 0

        for time_step in range(len(values)):
            sum += values[time_step][level][0][0]
            if time_step < 12 and counter == 11 or time_step > 12 and counter == 12:
                yearly_averages.append(sum / 12 - climatology_by_level[level])
                sum = 0
                counter = 0
            counter += 1

        anomalies_by_level.append(yearly_averages)

    return anomalies_by_level