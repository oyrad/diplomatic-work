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


def read_sounding_file(sondage_file):
    with open(sondage_file, 'r') as file:
        pressure = []
        temperature = []
        relative_humidity = []
        specific_humidity = []

        for _ in range(5):
            next(file)

        current_date_pressure = []
        current_date_temperature = []
        current_date_relative_humidity = []
        current_date_specific_humidity = []

        for line in file:

            columns = line.split()
            if (columns[0] == "PRES" or columns[0] == "Description"):
                pressure.append(current_date_pressure)
                temperature.append(current_date_temperature)
                relative_humidity.append(current_date_relative_humidity)
                specific_humidity.append(current_date_specific_humidity)

                current_date_pressure = []
                current_date_temperature = []
                current_date_relative_humidity = []
                current_date_specific_humidity = []

                continue

            if (columns[0] == "hPa"):
                continue

            if len(columns) >= 10:
                current_date_pressure.append(float(columns[0]))
                current_date_temperature.append(float(columns[2]))
                current_date_relative_humidity.append(int(columns[4]))
                current_date_specific_humidity.append(float(columns[5]))

    return pressure, temperature, relative_humidity, specific_humidity


def get_average_value(values, time_step, level):
    values_00, values_12 = values
    return ((values_00[time_step][level][0][0] + values_12[time_step][level][0][0]) / 2)


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
