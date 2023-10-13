import numpy as np
import util
from sklearn.linear_model import LinearRegression


def get_climatology_by_level(values, levels, season):
    climatology_by_level = []

    for level in range(len(levels)):
        current_values = []
        for time_step in range(996):
            if season == "none":
                current_values.append(
                    util.get_average_or_single_value(values, time_step, level)
                )
            else:
                value = util.get_seasonal_value(
                    values, time_step, level, season)
                if value:
                    current_values.append(value)

        climatology_by_level.append(np.mean(current_values))

    return climatology_by_level


def get_trend(values, levels, season="none"):
    climatology_by_level = get_climatology_by_level(values, levels, season)
    anomalies_by_level = []

    for level in range(len(levels)):
        anomalies_by_year = []
        current_values = []
        month = 1

        for time_step in range(996):
            if season == "none":
                current_values.append(
                    util.get_average_or_single_value(values, time_step, level)
                )
            else:
                value = util.get_seasonal_value(
                    values, time_step, level, season)
                if value:
                    current_values.append(value)

            if season == "DJF":
                if time_step < 12 and month == 10 or time_step > 12 and month == 12:
                    anomalies_by_year.append(
                        np.mean(current_values) - climatology_by_level[level]
                    )
                    current_values = []
                    month = 0
            else:
                if month == 12:
                    anomalies_by_year.append(
                        np.mean(current_values) - climatology_by_level[level]
                    )
                    current_values = []
                    month = 0

            month += 1

        years = np.arange(1940, 2023, 1).reshape(-1, 1)

        model = LinearRegression().fit(years, anomalies_by_year)
        anomalies_by_level.append(model.coef_ * 10)

    return anomalies_by_level


def get_anomalies_by_year_and_level(values, levels, season):
    climatology_by_level = get_climatology_by_level(values, levels, season)
    anomalies_by_level = []

    for level in range(len(levels)):
        anomalies_by_year = []
        current_values = []
        month = 1

        for time_step in range(996):
            if season == "none":
                current_values.append(
                    util.get_average_or_single_value(values, time_step, level)
                )
            else:
                value = util.get_seasonal_value(
                    values, time_step, level, season)
                if value:
                    current_values.append(value)

            if season == "DJF":
                if time_step < 12 and month == 10 or time_step > 12 and month == 12:
                    anomalies_by_year.append(
                        np.mean(current_values) - climatology_by_level[level]
                    )
                    current_values = []
                    month = 0
            else:
                if month == 12:
                    anomalies_by_year.append(
                        np.mean(current_values) - climatology_by_level[level]
                    )
                    current_values = []
                    month = 0

            month += 1

        anomalies_by_level.append(anomalies_by_year)

    return anomalies_by_level
