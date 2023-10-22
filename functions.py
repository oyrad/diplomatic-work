import numpy as np
import util, math
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats


def get_mean_values_by_level(values, levels, season):
    era5_mean = []

    for level in range(len(levels)):
        current_values = []

        for time_step in range(852, 972):
            if season == "none":
                current_values.append(util.get_average_or_single_value(values, time_step, level))
            else:
                value = util.get_seasonal_value(values, time_step, level, season)
                if value:
                    current_values.append(value)

        era5_mean.append(np.mean(current_values))

    return era5_mean


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


def get_anomalies_by_year(values, level, climatology_by_level, season):
    anomalies_by_year = []
    current_values = []

    for time_step in range(996):
        if season == "none":
            current_values.append(
                util.get_average_or_single_value(values, time_step, level)
            )
        else:
            value = util.get_seasonal_value(values, time_step, level, season)
            if value:
                current_values.append(value)

        if (season == "DJF" and time_step % 12 == 9) or (
            season != "DJF" and time_step % 12 == 11
        ):
            anomalies_by_year.append(
                np.mean(current_values) - climatology_by_level[level]
            )
            current_values = []

    return anomalies_by_year


def get_trend(values, levels, season):
    climatology_by_level = get_climatology_by_level(values, levels, season)
    trend_by_level = []

    for level in range(len(levels)):
        anomalies_by_year = get_anomalies_by_year(
            values, level, climatology_by_level, season
        )

        years = np.arange(1940, 2023, 1).reshape(-1, 1)
        model = LinearRegression().fit(years, anomalies_by_year)
        trend_by_level.append(model.coef_ * 10)

    return trend_by_level


def get_anomalies_by_year_and_level(values, levels, season):
    climatology_by_level = get_climatology_by_level(values, levels, season)
    anomalies_by_level = []

    for level in range(len(levels)):
        anomalies_by_level.append(
            get_anomalies_by_year(values, level, climatology_by_level, season)
        )

    return anomalies_by_level


def get_ttest(values, levels, season):
    climatology_by_level = get_climatology_by_level(values, levels, season)
    pvalue_by_level = []

    for level in range(len(levels)):
        anomalies_by_year = get_anomalies_by_year(
            values, level, climatology_by_level, season)

        years = np.arange(1940, 2023, 1).reshape(-1, 1)

        X = sm.add_constant(years)
        model = sm.OLS(anomalies_by_year, X)
        results = model.fit()

        pvalue_by_level.append(results.pvalues[1])

    return pvalue_by_level


def get_sounding_values_by_level(sondage_file, all_pressure_levels):
    temperature, rel_humidity = util.read_sounding_file(sondage_file, all_pressure_levels)
 
    temperature_by_level = []
    rel_humidity_by_level = []

    for pressure_level in all_pressure_levels:
        current_level_temperature = [] 
        current_level_rel_humidity = []

        for i in range(len(temperature)):
            if round(pressure_level) in temperature[i]:
                current_level_temperature.append(temperature[i][round(pressure_level)])

            if round(pressure_level) in rel_humidity[i]:
                current_level_rel_humidity.append(rel_humidity[i][round(pressure_level)])

        temperature_by_level.append(np.mean(current_level_temperature))
        rel_humidity_by_level.append(np.mean(current_level_rel_humidity))

        current_level_temperature = []
        current_level_rel_humidity = []

    return temperature_by_level, rel_humidity_by_level

def get_profile_comparison_ttest(sondage_file, temp, rel, levels, season):
    real_temp, real_rel = util.read_sounding_file(sondage_file, levels)
    temp_ttest, rel_ttest = [], []

    for current_level in range(len(levels)):
        real_temp_current, real_rel_current, era5_temp_current, era5_rel_current = [], [], [], [] 

        for time_step in range(852, 972):
            if season == "none":
                era5_temp_current.append(util.get_average_or_single_value(temp, time_step, current_level))
                era5_rel_current.append(util.get_average_or_single_value(rel, time_step, current_level))
            else:
                temp_value = util.get_seasonal_value(temp, time_step, current_level, season)
                rel_value = util.get_seasonal_value(rel, time_step, current_level, season)
                if temp_value:
                    era5_temp_current.append(temp_value)
                if rel_value:
                    era5_rel_current.append(rel_value)

        for i in range(len(real_temp)):
            if round(levels[current_level]) in real_temp[i]:
                real_temp_current.append(real_temp[i][round(levels[current_level])])

            if round(levels[current_level]) in real_rel[i]:
                real_rel_current.append(real_rel[i][round(levels[current_level])])

        if (len(real_temp_current) > 0):
            result = sm.stats.ttest_ind(real_temp_current, era5_temp_current)
            temp_ttest.append(result[1])

        if (len(real_rel_current) > 0):
            result = sm.stats.ttest_ind(real_rel_current, era5_rel_current)
            rel_ttest.append(result[1])

        real_temp_current, real_rel_current, era5_temp_current, era5_rel_current = [], [], [], []
    
    while len(temp_ttest) < len(levels):
        temp_ttest.insert(0, math.nan)

    while len(rel_ttest) < len(levels):
        rel_ttest.insert(0, math.nan)

    return temp_ttest, rel_ttest

    


