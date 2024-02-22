import numpy as np
import matplotlib
import functions as fn
import datetime, util
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

suptitle_size = 20
title_size = 15
tick_size = 15
label_size = 20
legend_size = "xx-large"

start_year = 1940
end_year = 2023

line_color = "#111"
test_line_color = "#888"

pressure_ticks = [1000, 700, 500, 300, 200, 100, 70, 50, 30, 20, 10, 7, 5, 3, 2, 1]

def trend(temp, rel, spec, levels, title, season="none"):
    fig, ax = plt.subplots(1, 3, figsize=(20, 10))
    plt.subplots_adjust(left=0.055, right=0.975, bottom=0.085, top=0.975, wspace=0.275)
    #fig.suptitle(title, fontsize=suptitle_size)

    ax[0].semilogy(fn.get_trend(temp, levels, season), levels, color=line_color)
    ax[1].semilogy(fn.get_trend(rel, levels, season), levels, color=line_color)
    ax[2].semilogy(fn.get_trend(spec, levels, season), levels, color=line_color)

    #ax[0].set_title("Temperatura", fontsize=title_size)
    ax[0].set_xlabel(r"Trend [$^{\circ}$C / 10 god]", fontsize=label_size)

    #ax[1].set_title("Relativna vlažnost", fontsize=title_size)
    ax[1].set_xlabel(r"Trend [$\%$ / 10 god]", fontsize=label_size)

    #ax[2].set_title("Specifična vlažnost", fontsize=title_size)
    ax[2].set_xlabel(r"Trend [gkg$^{-1}$ / 10 god]", fontsize=label_size)

    for axis in ax:
        axis.tick_params(axis='both', labelsize=tick_size)

    ax[0].set_xlim(-1.75, 0.5)
    ax[1].set_xlim(-1, 1)
    ax[2].set_xlim(-0.05, 0.25)

    ax[1].set_xticks([-1, -0.5, 0, 0.5, 1])

    for i in range(3):
        ax[i].invert_yaxis()
        ax[i].set_yticks(pressure_ticks)
        ax[i].get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        ax[i].axvline(0, color="#888", linestyle="dashed")
        ax[i].set_ylabel("Tlak [hPa]", fontsize=label_size)


def ttest(temp, rel, spec, levels, title, season="none"):
    fig, ax = plt.subplots(1, 3, figsize=(20, 10))
    plt.subplots_adjust(left=0.055, right=0.975, bottom=0.085, top=0.975, wspace=0.275)
    #fig.suptitle(title, fontsize=suptitle_size)

    ax[0].loglog(fn.get_ttest(temp, levels, season), levels, color=line_color)
    ax[1].loglog(fn.get_ttest(rel, levels, season), levels, color=line_color)
    ax[2].loglog(fn.get_ttest(spec, levels, season), levels, color=line_color)

    for axis in ax:
        axis.tick_params(axis='both', labelsize=tick_size)

    #ax[0].set_title("Temperatura", fontsize=title_size)
    #ax[1].set_title("Relativna vlažnost", fontsize=title_size)
    #ax[2].set_title("Specifična vlažnost", fontsize=title_size)

    for i in range(3):
        ax[i].set_xlim(right=1.2)
        ax[i].invert_yaxis()
        ax[i].set_yticks(pressure_ticks)
        ax[i].get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        ax[i].axvline(0.05, color=test_line_color, label=r"$\alpha = 0.05$")
        ax[i].set_xlabel("p-vrijednost", fontsize=label_size)
        ax[i].set_ylabel("Tlak [hPa]", fontsize=label_size)
        ax[i].legend(fontsize=legend_size)


def hovmoeller(values, levels, cmap_levels, cmap_label, title, season="none"):
    fig, ax = plt.subplots(1, 1, figsize=(16, 8))
    plt.subplots_adjust(left=0.06, right=1.07, bottom=0.8, top=0.97, hspace=0.5)

    date_list = []

    for year in range(start_year, end_year):
        date = datetime.date(year, 1, 1)
        date_list.append(date)

    x_values = np.arange(len(date_list))
    [X, Y] = np.meshgrid(x_values, levels)

    plt.gcf().autofmt_xdate()
    ax.invert_yaxis()
    ax.set_yscale("log")

    plt.xticks(fontsize=tick_size)
    plt.yticks(fontsize=tick_size)

    tick_indices = np.arange(0, len(date_list), 5)
    ax.set_xticks(tick_indices)
    ax.set_xticklabels([date_list[i].strftime("%Y") for i in tick_indices])

    ax.axhline(250, color="#777", linestyle="dashed")

    #ax.set_title(title, fontsize=title_size)
    ax.set_xlabel("Godina", fontsize=label_size)
    ax.set_ylabel("Tlak [hPa]", fontsize=label_size)
    ax.set_yticks(pressure_ticks)
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

    contour = ax.contourf(
        X,
        Y,
        fn.get_anomalies_by_year_and_level(values, levels, season),
        cmap=plt.get_cmap("RdBu").reversed(),
        levels=cmap_levels,
        extend="both",
    )

    cbar = fig.colorbar(contour, ticks=cmap_levels, format=FormatStrFormatter('%g'))
    cbar.ax.tick_params(axis='y', labelsize=tick_size)
    cbar.set_label(cmap_label, size=label_size)

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
    #fig.suptitle(
    #    "Usporedba stvarnih i ERA5 vrijednosti na 850 hPa, Zagreb, 2011. - 2020.",
    #    fontsize=suptitle_size,
    #)

    ax[0].plot(x_values, real_temp, label="Radiosondaža")
    ax[0].plot(x_values, era5_temp_mean, label="ERA5")
    ax[0].legend(fontsize=legend_size)

    ax[1].plot(x_values, real_rel, label="Radiosondaža")
    ax[1].plot(x_values, era5_rel_mean, label="ERA5")
    ax[1].legend(fontsize=legend_size)

    tick_indices = np.arange(0, len(date_list), 12)
    ax[0].set_xticks(tick_indices)
    ax[0].set_xticklabels([date_list[i].strftime("%Y") for i in tick_indices])
    ax[0].set_xlabel("Godina", fontsize=label_size)
    ax[0].set_ylabel(r"Temperatura [$^{\circ}$C]", fontsize=label_size)
    #ax[0].set_title("Temperatura", fontsize=title_size)

    ax[1].set_xticks(tick_indices)
    ax[1].set_xticklabels([date_list[i].strftime("%Y") for i in tick_indices])
    ax[1].set_xlabel("Godina", fontsize=label_size)
    ax[1].set_ylabel("Relativna vlažnost [%]", fontsize=label_size)
    #ax[1].set_title("Relativna vlažnost", fontsize=title_size)


def profile_comparison(sondage_file, temp, rel, levels, title, season="none"):
    real_temp, real_rel = fn.get_sounding_values_by_level(
        sondage_file, all_pressure_levels=levels
    )
    era5_temp = fn.get_era5_values_by_level(temp, levels, season)
    era5_rel = fn.get_era5_values_by_level(rel, levels, season)

    fig, ax = plt.subplots(1, 2, figsize=(20, 12))
    plt.subplots_adjust(left=0.055, right=0.975, bottom=0.085, top=0.975, wspace=0.275)

    for axis in ax:
        axis.tick_params(axis='both', labelsize=tick_size)

    ax[0].set_xlim(-70, 25)
    ax[1].set_xlim(-3, 90)

    ax[0].semilogy(era5_temp, levels, label="ERA5")
    ax[0].semilogy(real_temp, levels, label="Radiosondaža")
    ax[0].set_xlabel(r"Temperatura [$^{\circ}$C]", fontsize=label_size)

    ax[1].semilogy(era5_rel, levels, label="ERA5")
    ax[1].semilogy(real_rel, levels, label="Radiosondaža")
    ax[1].set_xlabel("Relativna vlažnost [%]", fontsize=label_size)

    for i in range(2):
        ax[i].set_ylabel("Tlak [hPa]", fontsize=label_size)
        ax[i].invert_yaxis()
        ax[i].set_yticks(pressure_ticks)
        ax[i].get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        ax[i].legend(fontsize=legend_size)


def profile_comparison_ttest(sondage_file, temp, rel, levels, title, season="none"):
    temp_pvalues, rel_pvalues = fn.get_profile_comparison_ttest(
        sondage_file, temp, rel, levels, season
    )

    fig, ax = plt.subplots(1, 2, figsize=(20, 12))
    plt.subplots_adjust(left=0.055, right=0.975, bottom=0.085, top=0.975, wspace=0.275)

    for axis in ax:
        axis.tick_params(axis='both', labelsize=tick_size)

    ax[0].loglog(temp_pvalues, levels, color=line_color)
    ax[1].loglog(rel_pvalues, levels, color=line_color)

    #ax[0].set_title("Temperatura", fontsize=title_size)
    #ax[1].set_title("Relativna vlažnost", fontsize=title_size)

    for i in range(2):
        ax[i].set_ylabel("Tlak [hPa]", fontsize=label_size)
        ax[i].set_xlabel("p-vrijednost", fontsize=label_size)
        ax[i].axvline(0.05, color=test_line_color, label=r"$\alpha = 0.05$")
        ax[i].set_ylim(bottom=0.7)
        ax[i].invert_yaxis()
        ax[i].set_yticks(pressure_ticks)
        ax[i].get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        ax[i].legend(fontsize=legend_size)


def profile_comparison_stddev(sondage_file, temp, rel, levels, title, season="none"):
    real_temp, real_rel = fn.get_sounding_values_by_level(
        sondage_file, all_pressure_levels=levels, type="stddev"
    )
    era5_temp = fn.get_era5_values_by_level(temp, levels, season, type="stddev")
    era5_rel = fn.get_era5_values_by_level(rel, levels, season, type="stddev")

    fig, ax = plt.subplots(1, 2, figsize=(20, 12))
    plt.subplots_adjust(left=0.055, right=0.975, bottom=0.085, top=0.975, wspace=0.275)
    #fig.suptitle(title, fontsize=suptitle_size)

    for axis in ax:
        axis.tick_params(axis='both', labelsize=tick_size)

    ax[0].set_xlim(-3, 10)
    ax[1].set_xlim(-3, 35)

    ax[0].semilogy(era5_temp, levels, label="ERA5")
    ax[0].semilogy(real_temp, levels, label="Radiosondaža")
    ax[0].set_xlabel(r"Temperatura [$^{\circ}$C]", fontsize=label_size)

    ax[1].semilogy(era5_rel, levels, label="ERA5")
    ax[1].semilogy(real_rel, levels, label="Radiosondaža")
    ax[1].set_xlabel("Relativna vlažnost [%]", fontsize=label_size)

    for i in range(2):
        ax[i].set_ylabel("Tlak [hPa]", fontsize=label_size)
        ax[i].invert_yaxis()
        ax[i].set_yticks(pressure_ticks)
        ax[i].get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        ax[i].legend(fontsize=legend_size)


def profile_comparison_ftest(sondage_file, temp, rel, levels, title, season="none"):
    temp_pvalues, rel_pvalues = fn.get_profile_comparison_ftest(
        sondage_file, temp, rel, levels, season
    )

    fig, ax = plt.subplots(1, 2, figsize=(20, 12))
    plt.subplots_adjust(left=0.055, right=0.975, bottom=0.085, top=0.975, wspace=0.275)

    ax[0].loglog(temp_pvalues, levels, color=line_color)
    ax[1].loglog(rel_pvalues, levels, color=line_color)

    for axis in ax:
        axis.tick_params(axis='both', labelsize=tick_size)

    #ax[0].set_title("Temperatura", fontsize=title_size)
    #ax[1].set_title("Relativna vlažnost", fontsize=title_size)

    for i in range(2):
        ax[i].set_ylabel("Tlak [hPa]", fontsize=label_size)
        ax[i].set_xlabel("p-vrijednost", fontsize=label_size)
        ax[i].axvline(0.05, color=test_line_color, label=r"$\alpha = 0.05$")
        ax[i].set_ylim(bottom=0.7)
        ax[i].invert_yaxis()
        ax[i].set_yticks(pressure_ticks)
        ax[i].get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        ax[i].legend(fontsize=legend_size)

import seaborn as sns

def sounding_data_availability(sondage_file, title, city):
    monthly_data = fn.get_sounding_data_availability(sondage_file, city)
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))

    data_matrix = np.transpose(np.reshape(monthly_data, (10, 12)))

    sns.heatmap(data_matrix, cmap='BuGn', annot=True, fmt=".1f", xticklabels=np.arange(2011, 2021), yticklabels=np.arange(1, 13))

    plt.xticks(fontsize=tick_size)
    plt.yticks(fontsize=tick_size)

    ax.set_ylabel("Mjesec", fontsize=label_size)
    ax.set_xlabel("Godina", fontsize=label_size)
    #ax.set_title(title, fontsize=title_size)