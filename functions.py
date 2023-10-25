import numpy as np
import util, math
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats


def get_era5_values_by_level(values, levels, season, type="mean"):
    era5_mean = []

    for level in range(len(levels)):
        current_values = []

        for time_step in range(852, 972):
            if season == "none":
                current_values.append(
                    util.get_average_or_single_value(values, time_step, level)
                )
            else:
                value = util.get_seasonal_value(values, time_step, level, season)
                if value:
                    current_values.append(value)

        if type == "mean":
            era5_mean.append(np.mean(current_values))
        elif type == "stddev":
            era5_mean.append(np.std(current_values))

    return era5_mean

def get_era5_values_for_level(level, temp, rel, start, end, season="none"):
    era5_temp_current, era5_rel_current = [], []
    for time_step in range(start, end):
        if season == "none":
            era5_temp_current.append(
                util.get_average_or_single_value(temp, time_step, level)
            )
            era5_rel_current.append(
                util.get_average_or_single_value(rel, time_step, level)
            )
        else:
            temp_value = util.get_seasonal_value(
                temp, time_step, level, season
            )
            rel_value = util.get_seasonal_value(
                rel, time_step, level, season
            )
            if temp_value:
                era5_temp_current.append(temp_value)
            if rel_value:
                era5_rel_current.append(rel_value)

    return era5_temp_current, era5_rel_current


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
                value = util.get_seasonal_value(values, time_step, level, season)
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
            values, level, climatology_by_level, season
        )

        years = np.arange(1940, 2023, 1).reshape(-1, 1)

        X = sm.add_constant(years)
        model = sm.OLS(anomalies_by_year, X)
        results = model.fit()

        pvalue_by_level.append(results.pvalues[1])

    return pvalue_by_level


def get_sounding_values_by_level(sondage_file, all_pressure_levels, type="mean"):
    temperature, rel_humidity = util.read_sounding_file(
        sondage_file, all_pressure_levels
    )

    temperature_by_level = []
    rel_humidity_by_level = []

    for pressure_level in all_pressure_levels:
        current_level_temperature = []
        current_level_rel_humidity = []

        for i in range(len(temperature)):
            if round(pressure_level) in temperature[i]:
                current_level_temperature.append(temperature[i][round(pressure_level)])

            if round(pressure_level) in rel_humidity[i]:
                current_level_rel_humidity.append(
                    rel_humidity[i][round(pressure_level)]
                )

        if type == "mean":
            if (len(current_level_temperature) > 0):
                temperature_by_level.append(np.mean(current_level_temperature))
            else:
                temperature_by_level.append(math.nan)

            if (len(current_level_rel_humidity) > 0):
                rel_humidity_by_level.append(np.mean(current_level_rel_humidity))
            else:
                rel_humidity_by_level.append(math.nan)

        elif type == "stddev":
            if (len(current_level_temperature) > 0):
                temperature_by_level.append(np.std(current_level_temperature))
            else:
                temperature_by_level.append(math.nan)

            if (len(current_level_rel_humidity) > 0):
                rel_humidity_by_level.append(np.std(current_level_rel_humidity))
            else:
                rel_humidity_by_level.append(math.nan)

        current_level_temperature = []
        current_level_rel_humidity = []

    return temperature_by_level, rel_humidity_by_level


def get_profile_comparison_ttest(sondage_file, temp, rel, levels, season):
    real_temp, real_rel = util.read_sounding_file(sondage_file, levels)
    temp_ttest, rel_ttest = [], []

    for current_level in range(len(levels)):
        real_temp_current, real_rel_current = [], []

        era5_temp_current, era5_rel_current = get_era5_values_for_level(current_level, temp, rel, 852, 972, season)

        for i in range(len(real_temp)):
            if round(levels[current_level]) in real_temp[i]:
                real_temp_current.append(real_temp[i][round(levels[current_level])])

            if round(levels[current_level]) in real_rel[i]:
                real_rel_current.append(real_rel[i][round(levels[current_level])])

        if len(real_temp_current) > 0:
            result = sm.stats.ttest_ind(real_temp_current, era5_temp_current)
            temp_ttest.append(result[1])
        else:
            temp_ttest.append(math.nan)

        if len(real_rel_current) > 0:
            result = sm.stats.ttest_ind(real_rel_current, era5_rel_current)
            rel_ttest.append(result[1])
        else:
            rel_ttest.append(math.nan)

    return temp_ttest, rel_ttest


def get_profile_comparison_ftest(sondage_file, temp, rel, levels, season):
    real_temp, real_rel = util.read_sounding_file(sondage_file, levels)
    temp_ftest, rel_ftest = [], []

    for current_level in range(len(levels)):
        real_temp_current, real_rel_current = [], []

        era5_temp_current, era5_rel_current = get_era5_values_for_level(current_level, temp, rel, 852, 972, season)

        for i in range(len(real_temp)):
            if round(levels[current_level]) in real_temp[i]:
                real_temp_current.append(real_temp[i][round(levels[current_level])])

            if round(levels[current_level]) in real_rel[i]:
                real_rel_current.append(real_rel[i][round(levels[current_level])])

        temp_ftest.append(util.ftest(real_temp_current, era5_temp_current))
        rel_ftest.append(util.ftest(real_rel_current, era5_rel_current))

    return temp_ftest, rel_ftest
