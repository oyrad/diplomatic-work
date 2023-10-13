import numpy as np
import functions as fn
import datetime
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

    for i in range(3):
        ax[i].invert_yaxis()
        ax[i].axvline(0, color="#888", linestyle="dashed")
        ax[i].set_ylabel("Tlak [hPa]", fontsize=label_size)


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
