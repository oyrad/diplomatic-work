import numpy as np
import functions as fn
import datetime
import util
import matplotlib.pyplot as plt

suptitle_size = 20
title_size = 15
label_size = 14

start_year = 1940
end_year = 2023


def trend(temp, rel, spec, levels, title, season="none"):
    fig, ax = plt.subplots(1, 3, figsize=(20, 10))
    fig.suptitle(title, fontsize=suptitle_size)

    ax[0].semilogy(fn.get_trend(temp, levels, season), levels)
    ax[1].semilogy(fn.get_trend(rel, levels, season), levels)
    ax[2].semilogy(fn.get_trend(spec, levels, season), levels)

    ax[0].set_title("Temperatura", fontsize=title_size)
    ax[0].set_xlabel(r"Trend [$^{\circ}$ C / 10 god]", fontsize=label_size)

    ax[1].set_title("Relativna vlažnost", fontsize=title_size)
    ax[1].set_xlabel(r"Trend [$\%$ / 10 god]", fontsize=label_size)

    ax[2].set_title("Specifična vlažnost", fontsize=title_size)
    ax[2].set_xlabel(r"Trend [gkg$^{-1}$ / 10 god]", fontsize=label_size)

    ax[0].set_xlim(-1.75, 0.5)
    ax[1].set_xlim(-1, 1)
    ax[2].set_xlim(-0.05, 0.25)

    for i in range(3):
        ax[i].invert_yaxis()
        ax[i].axvline(0, color="#888", linestyle="dashed")
        ax[i].set_ylabel("Tlak [hPa]", fontsize=label_size)


def ttest(temp, rel, spec, levels, title, season="none"):
    fig, ax = plt.subplots(1, 3, figsize=(20, 10))
    fig.suptitle(title, fontsize=suptitle_size)

    ax[0].loglog(fn.get_ttest(temp, levels, season), levels)
    ax[1].loglog(fn.get_ttest(rel, levels, season), levels)
    ax[2].loglog(fn.get_ttest(spec, levels, season), levels)

    ax[0].set_title("Temperatura", fontsize=title_size)
    ax[1].set_title("Relativna vlažnost", fontsize=title_size)
    ax[2].set_title("Specifična vlažnost", fontsize=title_size)

    for i in range(3):
        ax[i].set_xlim(0, 1.2)
        ax[i].invert_yaxis()
        ax[i].axvline(0.05, color="black", label=r"$\alpha = 0.05$")
        ax[i].set_xlabel("p-vrijednost", fontsize=label_size)
        ax[i].set_ylabel("Tlak [hPa]", fontsize=label_size)
        ax[i].legend()


def hovmoeller(values, levels, cmap_levels, cmap_label, title, season="none"):
    fig, ax = plt.subplots(1, 1, figsize=(16, 8))

    date_list = []

    for year in range(start_year, end_year):
        date = datetime.date(year, 1, 1)
        date_list.append(date)

    x_values = np.arange(len(date_list))
    [X, Y] = np.meshgrid(x_values, levels)

    plt.gcf().autofmt_xdate()
    ax.invert_yaxis()

    tick_indices = np.arange(0, len(date_list), 5)
    ax.set_xticks(tick_indices)
    ax.set_xticklabels([date_list[i].strftime("%Y") for i in tick_indices])

    ax.set_title(title, fontsize=title_size)
    ax.set_xlabel("Godina", fontsize=label_size)
    ax.set_ylabel("Tlak [hPa]", fontsize=label_size)

    contour = ax.contourf(
        X,
        Y,
        fn.get_anomalies_by_year_and_level(values, levels, season),
        cmap=plt.get_cmap("RdBu").reversed(),
        levels=cmap_levels,
        extend="both",
    )

    fig.colorbar(contour, ticks=cmap_levels, label=cmap_label)


def profile_comparison():
    return

def comparison(era5_temp, era5_rel, real_temp, real_rel):
    era5_temp_mean = []
    era5_rel_mean = []
    for time_step in range(852, 972):
        current_temp = util.get_average_value(era5_temp, time_step, 30)
        current_rel = util.get_average_value(era5_rel, time_step, 30)
        era5_temp_mean.append(current_temp)
        era5_rel_mean.append(current_rel)

    date_list = []

    for year in range(2011, 2022):
        for month in range(1, 13):
            date = datetime.date(year, month, 1)
            date_list.append(date)

    x_values = np.arange(len(date_list) - 12)

    fig, ax = plt.subplots(2, 1, figsize=(22, 16))
    fig.suptitle("Usporedba stvarnih i ERA5 vrijednosti na 850 hPa, Zagreb, 2011. - 2020.", fontsize=suptitle_size)

    ax[0].plot(x_values, real_temp, label="Stvarna vrijednost")
    ax[0].plot(x_values, era5_temp_mean, label="ERA5")
    ax[0].legend()

    ax[1].plot(x_values, real_rel, label="Stvarna vrijednost")
    ax[1].plot(x_values, era5_rel_mean, label="ERA5")
    ax[1].legend()

    tick_indices = np.arange(0, len(date_list), 12)
    ax[0].set_xticks(tick_indices)
    ax[0].set_xticklabels([date_list[i].strftime("%Y") for i in tick_indices])
    ax[0].set_xlabel("Godina", fontsize=label_size)
    ax[0].set_ylabel(r"Temperatura [$^{\circ}$ C]", fontsize=label_size)
    ax[0].set_title("Temperatura", fontsize=title_size)

    ax[1].set_xticks(tick_indices)
    ax[1].set_xticklabels([date_list[i].strftime("%Y") for i in tick_indices])
    ax[1].set_xlabel("Godina", fontsize=label_size)
    ax[1].set_ylabel("Relativna vlažnost [%]", fontsize=label_size)
    ax[1].set_title("Relativna vlažnost", fontsize=title_size)


def profile_comparison(sondage_file, temp, rel, levels, title, season="none"):
    all_pressure_levels = np.linspace(10, 1000, 500)
    real_temp, real_rel = fn.get_sounding_values_by_level(sondage_file, all_pressure_levels)
    era5_temp = fn.get_mean_values_by_level(temp, levels, season)
    era5_rel = fn.get_mean_values_by_level(rel, levels, season)

    fig, ax = plt.subplots(1, 2, figsize=(20, 12))
    fig.suptitle(title, fontsize=suptitle_size)

    ax[0].plot(era5_temp, levels, label="ERA5")
    ax[0].plot(real_temp, all_pressure_levels, label="Stvarna vrijednost")
    ax[0].set_xlabel(r"Temperatura [$^{\circ}$ C]", fontsize=label_size)
    ax[0].set_ylabel("Tlak [hPa]", fontsize=label_size)
    ax[0].set_title("Temperatura", fontsize=title_size)
    ax[0].invert_yaxis()
    ax[0].legend()

    ax[1].plot(era5_rel, levels, label="ERA5")
    ax[1].plot(real_rel, all_pressure_levels, label="Stvarna vrijednost")
    ax[1].set_xlabel("Relativna vlažnost [%]", fontsize=label_size)
    ax[1].set_ylabel("Tlak [hPa]", fontsize=label_size)
    ax[1].set_title("Relativna vlažnost", fontsize=title_size)
    ax[1].invert_yaxis()
    ax[1].legend()