import netCDF4 as nc


def load_data(file_path, variable):
    file = nc.Dataset(file_path, "r")
    values = file.variables[variable][:].data
    file.close()

    if variable == "t":
        return values - 273.15
    elif variable == "q":
        return values * 1000

    return values


def get_average_value(values, time_step, level):
    return (values[0][time_step][level][0][0] + values[1][time_step][level][0][0]) / 2


def get_average_or_single_value(values, time_step, level):
    if len(values) == 2:
        return get_average_value(values, time_step, level)

    return values[time_step][level][0][0]


def get_seasonal_value(values, time_step, level, season):
    if (
        season == "JJA"
        and (time_step % 12 == 5 or time_step % 12 == 6 or time_step % 12 == 7)
    ) or (
        season == "DJF"
        and (time_step % 12 == 11 or time_step % 12 == 0 or time_step % 12 == 1)
    ):
        return get_average_or_single_value(values, time_step, level)

    return 0
