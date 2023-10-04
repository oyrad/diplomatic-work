import numpy as np
import netCDF4 as nc
from sklearn.linear_model import LinearRegression

file = nc.Dataset('data/zg_temp_00.nc', 'r')
levels = file.variables["level"][:].data
file.close()


def get_climatology_by_level(values):
    climatology_by_level = []

    for level in range(len(levels)):
        level_total = []
        for time_step in range(len(values)):
            level_total.append(values[time_step][level][0][0])

        climatology_by_level.append(np.mean(level_total))

    return climatology_by_level


def get_trend(values):
    trend_by_level = []
    for level in range(len(levels)):

        averages_by_year = []
        sum = 0
        counter = 0

        for time_step in range(len(values)):
            sum += values[time_step][level][0][0]

            if (time_step < 12 and counter == 11 or time_step > 12 and counter == 12):
                averages_by_year.append(sum/12)
                sum = 0
                counter = 0
            counter += 1

        differences = []

        for year in range(len(averages_by_year) - 1):
            differences.append(
                averages_by_year[year + 1] - averages_by_year[year])

        trend_by_level.append(np.sum(differences))

    return trend_by_level


def get_averaged_differences(values):
    slopes = []
    climatology_by_level = get_climatology_by_level(values)

    for level in range(len(levels)):

        anomalies_by_year = []
        sum = 0
        counter = 0

        for time_step in range(len(values)):
            sum += values[time_step][level][0][0]

            if (time_step < 12 and counter == 11 or time_step > 12 and counter == 12):
                anomalies_by_year.append(sum/12 - climatology_by_level[level])
                sum = 0
                counter = 0

            counter += 1

        years = np.arange(1940, 2023, 1).reshape(-1, 1)

        model = LinearRegression().fit(years, anomalies_by_year)
        slopes.append(model.coef_)

    return slopes


def get_anomalies_by_year_and_level(values):

    climatology_by_level = get_climatology_by_level(values)
    anomalies_by_level = []

    for level in range(len(levels)):

        yearly_averages = []
        sum = 0
        counter = 0

        for time_step in range(len(values)):
            sum += values[time_step][level][0][0]
            if (time_step < 12 and counter == 11 or time_step > 12 and counter == 12):
                yearly_averages.append(sum/12 - climatology_by_level[level])
                sum = 0
                counter = 0
            counter += 1

        anomalies_by_level.append(yearly_averages)

    return anomalies_by_level
