import graph, util
import matplotlib.pyplot as plt

levels = [
    1,
    2,
    3,
    5,
    7,
    10,
    20,
    30,
    50,
    70,
    100,
    125,
    150,
    175,
    200,
    225,
    250,
    300,
    350,
    400,
    450,
    500,
    550,
    600,
    650,
    700,
    750,
    775,
    800,
    825,
    850,
    875,
    900,
    925,
    950,
    975,
    1000,
]

hovmoeller_temp_levels = [-3, -2, -1, -0.5, -0.25, 0.25, 0.5, 1, 2, 3]
hovmoeller_rel_levels = [-10, -8, -6, -4, -2, -1, 1, 2, 4, 6, 8, 10]
hovmoeller_spec_levels = [-1, -0.8, -0.6, -0.4, -0.2, -0.1, 0.1, 0.2, 0.4, 0.6, 0.8, 1]

zg_temp_00, zg_temp_12 = util.load_data("data/era5/zg_temp_00.nc", "t"), util.load_data(
    "data/era5/zg_temp_12.nc", "t"
)
zg_rel_00, zg_rel_12 = util.load_data("data/era5/zg_rel_00.nc", "r"), util.load_data(
    "data/era5/zg_rel_12.nc", "r"
)
zg_spec_00, zg_spec_12 = util.load_data("data/era5/zg_spec_00.nc", "q"), util.load_data(
    "data/era5/zg_spec_12.nc", "q"
)

zd_temp_00, zd_temp_12 = util.load_data("data/era5/zd_temp_00.nc", "t"), util.load_data(
    "data/era5/zd_temp_12.nc", "t"
)
zd_rel_00, zd_rel_12 = util.load_data("data/era5/zd_rel_00.nc", "r"), util.load_data(
    "data/era5/zd_rel_12.nc", "r"
)
zd_spec_00, zd_spec_12 = util.load_data("data/era5/zd_spec_00.nc", "q"), util.load_data(
    "data/era5/zd_spec_12.nc", "q"
)

def savefig(path):
    plt.savefig(path, facecolor="white", transparent=False)


def trend():
    graph.trend(
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        [zg_spec_00, zg_spec_12],
        levels,
        "Trend, Zagreb, 1940. - 2022.",
    )
    savefig("images/trend/zg/trend_zg_mean.png")

    graph.trend(
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        [zg_spec_00, zg_spec_12],
        levels,
        "Trend, Zagreb, 1940. - 2022. JJA",
        season="JJA",
    )
    savefig("images/trend/zg/trend_zg_mean_JJA.png")

    graph.trend(
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        [zg_spec_00, zg_spec_12],
        levels,
        "Trend Zagreb, 1940. - 2022. DJF",
        season="DJF",
    )
    savefig("images/trend/zg/trend_zg_mean_DJF.png")

    graph.trend(
        zg_temp_00, zg_rel_00, zg_spec_00, levels, "Trend, Zagreb 00 UTC, 1940. - 2022."
    )
    plt.savefig("images/trend/zg/trend_zg_00.png", facecolor="white", transparent=False)

    graph.trend(
        zg_temp_00,
        zg_rel_00,
        zg_spec_00,
        levels,
        "Trend, Zagreb 00 UTC, 1940. - 2022. JJA",
        season="JJA",
    )
    savefig("images/trend/zg/trend_zg_00_JJA.png")

    graph.trend(
        zg_temp_00,
        zg_rel_00,
        zg_spec_00,
        levels,
        "Trend, Zagreb 00 UTC, 1940. - 2022. DJF",
        season="DJF",
    )
    savefig("images/trend/zg/trend_zg_00_DJF.png")

    graph.trend(
        zg_temp_12, zg_rel_12, zg_spec_12, levels, "Trend, Zagreb 12 UTC, 1940. - 2022."
    )
    savefig("images/trend/zg/trend_zg_12.png")

    graph.trend(
        zg_temp_12,
        zg_rel_12,
        zg_spec_12,
        levels,
        "Trend, Zagreb 12 UTC, 1940. - 2022. JJA",
        season="JJA",
    )
    savefig("images/trend/zg/trend_zg_12_JJA.png")

    graph.trend(
        zg_temp_12,
        zg_rel_12,
        zg_spec_12,
        levels,
        "Trend, Zagreb 12 UTC, 1940. - 2022. DJF",
        season="DJF",
    )
    savefig("images/trend/zg/trend_zg_12_DJF.png")

    graph.trend(
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        [zd_spec_00, zd_spec_12],
        levels,
        "Trend Zadar, 1940. - 2022.",
    )
    savefig("images/trend/zd/trend_zd_mean.png")

    graph.trend(
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        [zd_spec_00, zd_spec_12],
        levels,
        "Trend, Zadar, 1940. - 2022. JJA",
        season="JJA",
    )
    savefig("images/trend/zd/trend_zd_mean_JJA.png")

    graph.trend(
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        [zd_spec_00, zd_spec_12],
        levels,
        "Trend, Zadar, 1940. - 2022. DJF",
        season="DJF",
    )
    savefig("images/trend/zd/trend_zd_mean_DJF.png")

    graph.trend(
        zd_temp_00, zd_rel_00, zd_spec_00, levels, "Trend, Zadar 00 UTC, 1940. - 2022."
    )
    savefig("images/trend/zd/trend_zd_00.png")

    graph.trend(
        zd_temp_00,
        zd_rel_00,
        zd_spec_00,
        levels,
        "Trend, Zadar 00 UTC, 1940. - 2022. JJA",
        season="JJA",
    )
    savefig("images/trend/zd/trend_zd_00_JJA.png")

    graph.trend(
        zd_temp_00,
        zd_rel_00,
        zd_spec_00,
        levels,
        "Trend, Zadar 00 UTC, 1940. - 2022. DJF",
        season="DJF",
    )
    savefig("images/trend/zd/trend_zd_00_DJF.png")

    graph.trend(
        zd_temp_12, zd_rel_12, zd_spec_12, levels, "Trend, Zadar 12 UTC, 1940. - 2022."
    )
    savefig("images/trend/zd/trend_zd_12.png")

    graph.trend(
        zd_temp_12,
        zd_rel_12,
        zd_spec_12,
        levels,
        "Trend, Zadar 12 UTC, 1940. - 2022. JJA",
        season="JJA",
    )
    savefig("images/trend/zd/trend_zd_12_JJA.png")

    graph.trend(
        zd_temp_12,
        zd_rel_12,
        zd_spec_12,
        levels,
        "Trend, Zadar 12 UTC, 1940. - 2022. DJF",
        season="DJF",
    )
    savefig("images/trend/zd/trend_zd_12_DJF.png")

    plt.close("all")


def trend_ttest():
    graph.ttest(
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        [zg_spec_00, zg_spec_12],
        levels,
        "Trend t-test, Zagreb, 1940. - 2022.",
    )
    savefig("images/trend/zg/ttest/trend_zg_mean_ttest.png")

    graph.ttest(
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        [zg_spec_00, zg_spec_12],
        levels,
        "Trend t-test, Zagreb, 1940. - 2022. JJA",
        season="JJA",
    )
    savefig("images/trend/zg/ttest/trend_zg_mean_JJA_ttest.png")

    graph.ttest(
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        [zg_spec_00, zg_spec_12],
        levels,
        "Trend t-test, Zagreb, 1940. - 2022. DJF",
        season="DJF",
    )
    savefig("images/trend/zg/ttest/trend_zg_mean_DJF_ttest.png")

    graph.ttest(
        zg_temp_00,
        zg_rel_00,
        zg_spec_00,
        levels,
        "Trend t-test, Zagreb 00 UTC, 1940. - 2022.",
    )
    savefig("images/trend/zg/ttest/trend_zg_00_ttest.png")

    graph.ttest(
        zg_temp_00,
        zg_rel_00,
        zg_spec_00,
        levels,
        "Trend t-test, Zagreb 00 UTC, 1940. - 2022. JJA",
        season="JJA",
    )
    savefig("images/trend/zg/ttest/trend_zg_00_JJA_ttest.png")

    graph.ttest(
        zg_temp_00,
        zg_rel_00,
        zg_spec_00,
        levels,
        "Trend t-test, Zagreb 00 UTC, 1940. - 2022. DJF",
        season="DJF",
    )
    savefig("images/trend/zg/ttest/trend_zg_00_DJF_ttest.png")

    graph.ttest(
        zg_temp_12,
        zg_rel_12,
        zg_spec_12,
        levels,
        "Trend t-test, Zagreb 12 UTC, 1940. - 2022.",
    )
    savefig("images/trend/zg/ttest/trend_zg_12_ttest.png")

    graph.ttest(
        zg_temp_12,
        zg_rel_12,
        zg_spec_12,
        levels,
        "Trend t-test, Zagreb 12 UTC, 1940. - 2022. JJA",
        season="JJA",
    )
    savefig("images/trend/zg/ttest/trend_zg_12_JJA_ttest.png")

    graph.ttest(
        zg_temp_12,
        zg_rel_12,
        zg_spec_12,
        levels,
        "Trend t-test, Zagreb 12 UTC, 1940. - 2022. DJF",
        season="DJF",
    )
    savefig("images/trend/zg/ttest/trend_zg_12_DJF_ttest.png")

    graph.ttest(
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        [zd_spec_00, zd_spec_12],
        levels,
        "Trend t-test, Zadar, 1940. - 2022.",
    )
    savefig("images/trend/zd/ttest/trend_zd_mean_ttest.png")

    graph.ttest(
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        [zd_spec_00, zd_spec_12],
        levels,
        "Trend t-test, Zadar, 1940. - 2022. JJA",
        season="JJA",
    )
    savefig("images/trend/zd/ttest/trend_zd_mean_JJA_ttest.png")

    graph.ttest(
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        [zd_spec_00, zd_spec_12],
        levels,
        "Trend t-test, Zadar, 1940. - 2022. DJF",
        season="DJF",
    )
    savefig("images/trend/zd/ttest/trend_zd_mean_DJF_ttest.png")

    graph.ttest(
        zd_temp_00,
        zd_rel_00,
        zd_spec_00,
        levels,
        "Trend t-test, Zadar 00 UTC, 1940. - 2022.",
    )
    savefig("images/trend/zd/ttest/trend_zd_00_ttest.png")

    graph.ttest(
        zd_temp_00,
        zd_rel_00,
        zd_spec_00,
        levels,
        "Trend t-test, Zadar 00 UTC, 1940. - 2022. JJA",
        season="JJA",
    )
    savefig("images/trend/zd/ttest/trend_zd_00_JJA_ttest.png")

    graph.ttest(
        zd_temp_00,
        zd_rel_00,
        zd_spec_00,
        levels,
        "Trend t-test, Zadar 00 UTC, 1940. - 2022. DJF",
        season="DJF",
    )
    savefig("images/trend/zd/ttest/trend_zd_00_DJF_ttest.png")

    graph.ttest(
        zd_temp_12,
        zd_rel_12,
        zd_spec_12,
        levels,
        "Trend t-test, Zadar 12 UTC, 1940. - 2022.",
    )
    savefig("images/trend/zd/ttest/trend_zd_12_ttest.png")

    graph.ttest(
        zd_temp_12,
        zd_rel_12,
        zd_spec_12,
        levels,
        "Trend t-test, Zadar 12 UTC, 1940. - 2022. JJA",
        season="JJA",
    )
    savefig("images/trend/zd/ttest/trend_zd_12_JJA_ttest.png")

    graph.ttest(
        zd_temp_12,
        zd_rel_12,
        zd_spec_12,
        levels,
        "Trend t-test, Zadar 12 UTC, 1940. - 2022. DJF",
        season="DJF",
    )
    savefig("images/trend/zd/ttest/trend_zd_12_DJF_ttest.png")

    plt.close("all")


def hovmoeller():
    graph.hovmoeller(
        [zg_temp_00, zg_temp_12],
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zagreb",
    )
    savefig("images/hovmoeller/temp/zg/hov_temp_zg_mean.png")

    graph.hovmoeller(
        [zg_temp_00, zg_temp_12],
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zagreb, JJA",
        season="JJA",
    )
    savefig("images/hovmoeller/temp/zg/hov_temp_zg_mean_JJA.png")

    graph.hovmoeller(
        [zg_temp_00, zg_temp_12],
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zagreb, DJF",
        season="DJF",
    )
    savefig("images/hovmoeller/temp/zg/hov_temp_zg_mean_DJF.png")

    graph.hovmoeller(
        [zg_rel_00, zg_rel_12],
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zagreb",
    )
    savefig("images/hovmoeller/rel/zg/hov_rel_zg_mean.png")

    graph.hovmoeller(
        [zg_rel_00, zg_rel_12],
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zagreb, JJA",
        season="JJA",
    )
    savefig("images/hovmoeller/rel/zg/hov_rel_zg_mean_JJA.png")

    graph.hovmoeller(
        [zg_rel_00, zg_rel_12],
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zagreb, DJF",
        season="DJF",
    )
    savefig("images/hovmoeller/rel/zg/hov_rel_zg_mean_DJF.png")

    graph.hovmoeller(
        [zg_spec_00, zg_spec_12],
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zagreb",
    )
    savefig("images/hovmoeller/spec/zg/hov_spec_zg_mean.png")

    graph.hovmoeller(
        [zg_spec_00, zg_spec_12],
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zagreb, JJA",
        season="JJA",
    )
    savefig("images/hovmoeller/spec/zg/hov_spec_zg_mean_JJA.png")

    graph.hovmoeller(
        [zg_spec_00, zg_spec_12],
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zagreb, DJF",
        season="DJF",
    )
    savefig("images/hovmoeller/spec/zg/hov_spec_zg_mean_DJF.png")

    graph.hovmoeller(
        zg_temp_00,
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zagreb 00 UTC",
    )
    savefig("images/hovmoeller/temp/zg/hov_temp_zg_00.png")

    graph.hovmoeller(
        zg_temp_00,
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zagreb 00 UTC, JJA",
        season="JJA",
    )
    savefig("images/hovmoeller/temp/zg/hov_temp_zg_00_JJA.png")

    graph.hovmoeller(
        zg_temp_00,
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zagreb 00 UTC, DJF",
        season="DJF",
    )
    savefig("images/hovmoeller/temp/zg/hov_temp_zg_00_DJF.png")

    graph.hovmoeller(
        zg_rel_00,
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zagreb 00 UTC",
    )
    savefig("images/hovmoeller/rel/zg/hov_rel_zg_00.png")

    graph.hovmoeller(
        zg_rel_00,
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zagreb 00 UTC, JJA",
        season="JJA",
    )
    savefig("images/hovmoeller/rel/zg/hov_rel_zg_00_JJA.png")

    graph.hovmoeller(
        zg_rel_00,
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zagreb 00 UTC, DJF",
        season="DJF",
    )
    savefig("images/hovmoeller/rel/zg/hov_rel_zg_00_DJF.png")

    graph.hovmoeller(
        zg_spec_00,
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zagreb 00 UTC",
    )
    savefig("images/hovmoeller/spec/zg/hov_spec_zg_00.png")

    graph.hovmoeller(
        zg_spec_00,
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zagreb 00 UTC, JJA",
        season="JJA",
    )
    savefig("images/hovmoeller/spec/zg/hov_spec_zg_00_JJA.png")

    graph.hovmoeller(
        zg_spec_00,
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zagreb 00 UTC, DJF",
        season="DJF",
    )
    savefig("images/hovmoeller/spec/zg/hov_spec_zg_00_DJF.png")

    graph.hovmoeller(
        zg_temp_12,
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zagreb 12 UTC",
    )
    savefig("images/hovmoeller/temp/zg/hov_temp_zg_12.png")

    graph.hovmoeller(
        zg_temp_12,
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zagreb 12 UTC, JJA",
        season="JJA",
    )
    savefig("images/hovmoeller/temp/zg/hov_temp_zg_12_JJA.png")

    graph.hovmoeller(
        zg_temp_12,
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zagreb 12 UTC, DJF",
        season="DJF",
    )
    savefig("images/hovmoeller/temp/zg/hov_temp_zg_12_DJF.png")

    graph.hovmoeller(
        zg_rel_12,
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zagreb 12 UTC",
    )
    savefig("images/hovmoeller/rel/zg/hov_rel_zg_12.png")

    graph.hovmoeller(
        zg_rel_12,
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zagreb 12 UTC, JJA",
        season="JJA",
    )
    savefig("images/hovmoeller/rel/zg/hov_rel_zg_12_JJA.png")

    graph.hovmoeller(
        zg_rel_12,
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zagreb 12 UTC, DJF",
        season="DJF",
    )
    savefig("images/hovmoeller/rel/zg/hov_rel_zg_12_DJF.png")

    graph.hovmoeller(
        zg_spec_12,
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zagreb 12 UTC",
    )
    savefig("images/hovmoeller/spec/zg/hov_spec_zg_12.png")

    graph.hovmoeller(
        zg_spec_12,
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zagreb 12 UTC, JJA",
        season="JJA",
    )
    savefig("images/hovmoeller/spec/zg/hov_spec_zg_12_JJA.png")

    graph.hovmoeller(
        zg_spec_12,
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zagreb 12 UTC, DJF",
        season="DJF",
    )
    savefig("images/hovmoeller/spec/zg/hov_spec_zg_12_DJF.png")

    graph.hovmoeller(
        [zd_temp_00, zd_temp_12],
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zadar",
    )
    savefig("images/hovmoeller/temp/zd/hov_temp_zd_mean.png")

    graph.hovmoeller(
        [zd_temp_00, zd_temp_12],
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zadar, JJA",
        season="JJA",
    )
    savefig("images/hovmoeller/temp/zd/hov_temp_zd_mean_JJA.png")

    graph.hovmoeller(
        [zd_temp_00, zd_temp_12],
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zadar, DJF",
        season="DJF",
    )
    plt.savefig(
        "images/hovmoeller/temp/zd/hov_temp_zd_mean_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        [zd_rel_00, zd_rel_12],
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zadar",
    )
    plt.savefig(
        "images/hovmoeller/rel/zd/hov_rel_zd_mean.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        [zd_rel_00, zd_rel_12],
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zadar, JJA",
        season="JJA",
    )
    plt.savefig(
        "images/hovmoeller/rel/zd/hov_rel_zd_mean_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        [zd_rel_00, zd_rel_12],
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zadar, DJF",
        season="DJF",
    )
    plt.savefig(
        "images/hovmoeller/rel/zd/hov_rel_zd_mean_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        [zd_spec_00, zd_spec_12],
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zadar",
    )
    plt.savefig(
        "images/hovmoeller/spec/zd/hov_spec_zd_mean.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        [zd_spec_00, zd_spec_12],
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zadar, JJA",
        season="JJA",
    )
    plt.savefig(
        "images/hovmoeller/spec/zd/hov_spec_zd_mean_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        [zd_spec_00, zd_spec_12],
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zadar, DJF",
        season="DJF",
    )
    plt.savefig(
        "images/hovmoeller/spec/zd/hov_spec_zd_mean_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_temp_00,
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zadar 00 UTC",
    )
    plt.savefig(
        "images/hovmoeller/temp/zd/hov_temp_zd_00.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_temp_00,
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zadar 00 UTC, JJA",
        season="JJA",
    )
    plt.savefig(
        "images/hovmoeller/temp/zd/hov_temp_zd_00_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_temp_00,
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zadar 00 UTC, DJF",
        season="DJF",
    )
    plt.savefig(
        "images/hovmoeller/temp/zd/hov_temp_zd_00_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_rel_00,
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zadar 00 UTC",
    )
    plt.savefig(
        "images/hovmoeller/rel/zd/hov_rel_zd_00.png",
        facecolor="white",
        transparent=False,
    )
    graph.hovmoeller(
        zd_rel_00,
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zadar 00 UTC, JJA",
        season="JJA",
    )
    plt.savefig(
        "images/hovmoeller/rel/zd/hov_rel_zd_00_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_rel_00,
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zadar 00 UTC, DJF",
        season="DJF",
    )
    plt.savefig(
        "images/hovmoeller/rel/zd/hov_rel_zd_00_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_spec_00,
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zadar 00 UTC",
    )
    plt.savefig(
        "images/hovmoeller/spec/zd/hov_spec_zd_00.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_spec_00,
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zadar 00 UTC, JJA",
        season="JJA",
    )
    plt.savefig(
        "images/hovmoeller/spec/zd/hov_spec_zd_00_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_spec_00,
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zadar 00 UTC, DJF",
        season="DJF",
    )
    plt.savefig(
        "images/hovmoeller/spec/zd/hov_spec_zd_00_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_temp_12,
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zadar 12 UTC",
    )
    plt.savefig(
        "images/hovmoeller/temp/zd/hov_temp_zd_12.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_temp_12,
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zadar 12 UTC, JJA",
        season="JJA",
    )
    plt.savefig(
        "images/hovmoeller/temp/zd/hov_temp_zd_12_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_temp_12,
        levels,
        cmap_levels=hovmoeller_temp_levels,
        cmap_label=r"[$^{\circ}$ C]",
        title="Temperatura, Zadar 12 UTC, DJF",
        season="DJF",
    )
    plt.savefig(
        "images/hovmoeller/temp/zd/hov_temp_zd_12_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_rel_12,
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zadar 12 UTC",
    )
    plt.savefig(
        "images/hovmoeller/rel/zd/hov_rel_zd_12.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_rel_12,
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zadar 12 UTC, JJA",
        season="JJA",
    )
    plt.savefig(
        "images/hovmoeller/rel/zd/hov_rel_zd_12_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_rel_12,
        levels,
        cmap_levels=hovmoeller_rel_levels,
        cmap_label="[%]",
        title="Relativna vlažnost, Zadar 12 UTC, DJF",
        season="DJF",
    )
    plt.savefig(
        "images/hovmoeller/rel/zd/hov_rel_zd_12_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_spec_12,
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zadar 12 UTC",
    )
    plt.savefig(
        "images/hovmoeller/spec/zd/hov_spec_zd_12.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_spec_12,
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zadar 12 UTC, JJA",
        season="JJA",
    )
    plt.savefig(
        "images/hovmoeller/spec/zd/hov_spec_zd_12_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.hovmoeller(
        zd_spec_12,
        levels,
        cmap_levels=hovmoeller_spec_levels,
        cmap_label="[g/kg]",
        title="Specifična vlažnost, Zadar 12 UTC, DJF",
        season="DJF",
    )
    plt.savefig(
        "images/hovmoeller/spec/zd/hov_spec_zd_12_DJF.png",
        facecolor="white",
        transparent=False,
    )

    plt.close("all")


def profile_comparison():
    graph.profile_comparison(
        "data/soundings/zg.txt",
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zagreb, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison/zg/profile_comparison_zg_mean.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zg_JJA.txt",
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zagreb, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison/zg/profile_comparison_zg_mean_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zg_DJF.txt",
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zagreb, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison/zg/profile_comparison_zg_mean_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zg_00.txt",
        zg_temp_00,
        zg_rel_00,
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zagreb 00 UTC, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison/zg/profile_comparison_zg_00.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zg_00_JJA.txt",
        zg_temp_00,
        zg_rel_00,
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zagreb 00 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison/zg/profile_comparison_zg_00_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zg_00_DJF.txt",
        zg_temp_00,
        zg_rel_00,
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zagreb 00 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison/zg/profile_comparison_zg_00_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zg_12.txt",
        zg_temp_12,
        zg_rel_12,
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zagreb 12 UTC, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison/zg/profile_comparison_zg_12.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zg_12_JJA.txt",
        zg_temp_12,
        zg_rel_12,
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zagreb 12 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison/zg/profile_comparison_zg_12_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zg_12_DJF.txt",
        zg_temp_12,
        zg_rel_12,
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zagreb 12 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison/zg/profile_comparison_zg_12_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zd.txt",
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zadar, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison/zd/profile_comparison_zd_mean.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zd_JJA.txt",
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zadar, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison/zd/profile_comparison_zd_mean_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zd_DJF.txt",
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zadar, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison/zd/profile_comparison_zd_mean_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zd_00.txt",
        zd_temp_00,
        zd_rel_00,
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zadar 00 UTC, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison/zd/profile_comparison_zd_00.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zd_00_JJA.txt",
        zd_temp_00,
        zd_rel_00,
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zadar 00 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison/zd/profile_comparison_zd_00_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zd_00_DJF.txt",
        zd_temp_00,
        zd_rel_00,
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zadar 00 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison/zd/profile_comparison_zd_00_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zd_12.txt",
        zd_temp_12,
        zd_rel_12,
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zadar 12 UTC, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison/zd/profile_comparison_zd_12.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zd_12_JJA.txt",
        zd_temp_12,
        zd_rel_12,
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zadar 12 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison/zd/profile_comparison_zd_12_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison(
        "data/soundings/zd_12_DJF.txt",
        zd_temp_12,
        zd_rel_12,
        levels,
        title="Usporedba profila stvarnih vrijednosti i ERA5, Zadar 12 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison/zd/profile_comparison_zd_12_DJF.png",
        facecolor="white",
        transparent=False,
    )

    plt.close("all")


def profile_comparison_ttest():
    graph.profile_comparison_ttest(
        "data/soundings/zg.txt",
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zagreb, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison/zg/ttest/profile_comparison_zg_mean_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zg_JJA.txt",
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zagreb, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison/zg/ttest/profile_comparison_zg_mean_JJA_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zg_DJF.txt",
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zagreb, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison/zg/ttest/profile_comparison_zg_mean_DJF_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zg_00.txt",
        zg_temp_00,
        zg_rel_00,
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zagreb 00 UTC, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison/zg/ttest/profile_comparison_zg_00_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zg_00_JJA.txt",
        zg_temp_00,
        zg_rel_00,
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zagreb 00 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison/zg/ttest/profile_comparison_zg_00_JJA_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zg_00_DJF.txt",
        zg_temp_00,
        zg_rel_00,
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zagreb 00 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison/zg/ttest/profile_comparison_zg_00_DJF_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zg_12.txt",
        zg_temp_12,
        zg_rel_12,
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zagreb 12 UTC, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison/zg/ttest/profile_comparison_zg_12_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zg_12_JJA.txt",
        zg_temp_12,
        zg_rel_12,
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zagreb 12 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison/zg/ttest/profile_comparison_zg_12_JJA_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zg_12_DJF.txt",
        zg_temp_12,
        zg_rel_12,
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zagreb 12 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison/zg/ttest/profile_comparison_zg_12_DJF_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zd.txt",
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zadar, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison/zd/ttest/profile_comparison_zd_mean_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zd_JJA.txt",
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zadar, 2011. - 2020. JJA",
    )
    plt.savefig(
        "images/profile_comparison/zd/ttest/profile_comparison_zd_mean_JJA_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zd_DJF.txt",
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zadar, 2011. - 2020. DJF",
    )
    plt.savefig(
        "images/profile_comparison/zd/ttest/profile_comparison_zd_mean_DJF_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zd_00.txt",
        zd_temp_00,
        zd_rel_00,
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zadar 00 UTC, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison/zd/ttest/profile_comparison_zd_00_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zd_00_JJA.txt",
        zd_temp_00,
        zd_rel_00,
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zadar 00 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison/zd/ttest/profile_comparison_zd_00_JJA_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zd_00_DJF.txt",
        zd_temp_00,
        zd_rel_00,
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zadar 00 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison/zd/ttest/profile_comparison_zd_00_DJF_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zd_12.txt",
        zd_temp_12,
        zd_rel_12,
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zadar 12 UTC, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison/zd/ttest/profile_comparison_zd_12_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zd_12_JJA.txt",
        zd_temp_12,
        zd_rel_12,
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zadar 12 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison/zd/ttest/profile_comparison_zd_12_JJA_ttest.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_ttest(
        "data/soundings/zd_12_DJF.txt",
        zd_temp_12,
        zd_rel_12,
        levels,
        title="T-test profila stvarnih vrijednosti i ERA5, Zadar 12 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison/zd/ttest/profile_comparison_zd_12_DJF_ttest.png",
        facecolor="white",
        transparent=False,
    )

    plt.close("all")


def profile_comparison_stddev():
    graph.profile_comparison_stddev(
        "data/soundings/zg.txt",
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zagreb, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zg/profile_comparison_stddev_zg_mean.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zg_JJA.txt",
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zagreb, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zg/profile_comparison_stddev_zg_mean_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zg_DJF.txt",
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zagreb, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zg/profile_comparison_stddev_zg_mean_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zg_00.txt",
        zg_temp_00,
        zg_rel_00,
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zagreb 00 UTC, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zg/profile_comparison_stddev_zg_00.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zg_00_JJA.txt",
        zg_temp_00,
        zg_rel_00,
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zagreb 00 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zg/profile_comparison_stddev_zg_00_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zg_00_DJF.txt",
        zg_temp_00,
        zg_rel_00,
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zagreb 00 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zg/profile_comparison_stddev_zg_00_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zg_12.txt",
        zg_temp_12,
        zg_rel_12,
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zagreb 12 UTC, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zg/profile_comparison_stddev_zg_12.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zg_12_JJA.txt",
        zg_temp_12,
        zg_rel_12,
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zagreb 12 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zg/profile_comparison_stddev_zg_12_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zg_12_DJF.txt",
        zg_temp_12,
        zg_rel_12,
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zagreb 12 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zg/profile_comparison_stddev_zg_12_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zd.txt",
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zadar, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zd/profile_comparison_stddev_zd_mean.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zd_JJA.txt",
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zadar, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zd/profile_comparison_stddev_zd_mean_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zd_DJF.txt",
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zadar, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zd/profile_comparison_stddev_zd_mean_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zd_00.txt",
        zd_temp_00,
        zd_rel_00,
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zadar 00 UTC, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zd/profile_comparison_stddev_zd_00.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zd_00_JJA.txt",
        zd_temp_00,
        zd_rel_00,
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zadar 00 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zd/profile_comparison_stddev_zd_00_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zd_00_DJF.txt",
        zd_temp_00,
        zd_rel_00,
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zadar 00 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zd/profile_comparison_stddev_zd_00_DJF.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zd_12.txt",
        zd_temp_12,
        zd_rel_12,
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zadar 12 UTC, 2011. - 2020.",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zd/profile_comparison_stddev_zd_12.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zd_12_JJA.txt",
        zd_temp_12,
        zd_rel_12,
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zadar 12 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zd/profile_comparison_stddev_zd_12_JJA.png",
        facecolor="white",
        transparent=False,
    )

    graph.profile_comparison_stddev(
        "data/soundings/zd_12_DJF.txt",
        zd_temp_12,
        zd_rel_12,
        levels,
        title="Usporedba standardnih devijacija profila stvarnih vrijednosti i ERA5, Zadar 12 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    plt.savefig(
        "images/profile_comparison_stddev/zd/profile_comparison_stddev_zd_12_DJF.png",
        facecolor="white",
        transparent=False,
    )

    plt.close("all")


def profile_comparison_ftest():
    graph.profile_comparison_ftest(
        "data/soundings/zg.txt",
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zagreb, 2011. - 2020.",
    )
    savefig("images/profile_comparison_stddev/zg/ftest/profile_comparison_zg_mean_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zg_JJA.txt",
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zagreb, 2011. - 2020. JJA",
        season="JJA",
    )
    savefig("images/profile_comparison_stddev/zg/ftest/profile_comparison_zg_mean_JJA_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zg_DJF.txt",
        [zg_temp_00, zg_temp_12],
        [zg_rel_00, zg_rel_12],
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zagreb, 2011. - 2020. DJF",
        season="DJF",
    )
    savefig("images/profile_comparison_stddev/zg/ftest/profile_comparison_zg_mean_DJF_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zg_00.txt",
        zg_temp_00,
        zg_rel_00,
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zagreb 00 UTC, 2011. - 2020.",
    )
    savefig("images/profile_comparison_stddev/zg/ftest/profile_comparison_zg_00_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zg_00_JJA.txt",
        zg_temp_00,
        zg_rel_00,
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zagreb 00 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    savefig("images/profile_comparison_stddev/zg/ftest/profile_comparison_zg_00_JJA_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zg_00_DJF.txt",
        zg_temp_00,
        zg_rel_00,
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zagreb 00 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    savefig("images/profile_comparison_stddev/zg/ftest/profile_comparison_zg_00_DJF_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zg_12.txt",
        zg_temp_12,
        zg_rel_12,
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zagreb 12 UTC, 2011. - 2020.",
    )
    savefig("images/profile_comparison_stddev/zg/ftest/profile_comparison_zg_12_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zg_12_JJA.txt",
        zg_temp_12,
        zg_rel_12,
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zagreb 12 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    savefig("images/profile_comparison_stddev/zg/ftest/profile_comparison_zg_12_JJA_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zg_12_DJF.txt",
        zg_temp_12,
        zg_rel_12,
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zagreb 12 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    savefig("images/profile_comparison_stddev/zg/ftest/profile_comparison_zg_12_DJF_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zd.txt",
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zadar, 2011. - 2020.",
    )
    savefig("images/profile_comparison_stddev/zd/ftest/profile_comparison_zd_mean_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zd_JJA.txt",
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zadar, 2011. - 2020. JJA",
        season="JJA",
    )
    savefig("images/profile_comparison_stddev/zd/ftest/profile_comparison_zd_mean_JJA_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zd_DJF.txt",
        [zd_temp_00, zd_temp_12],
        [zd_rel_00, zd_rel_12],
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zadar, 2011. - 2020. DJF",
        season="DJF",
    )
    savefig("images/profile_comparison_stddev/zd/ftest/profile_comparison_zd_mean_DJF_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zd_00.txt",
        zd_temp_00,
        zd_rel_00,
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zadar 00 UTC, 2011. - 2020.",
    )
    savefig("images/profile_comparison_stddev/zd/ftest/profile_comparison_zd_00_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zd_00_JJA.txt",
        zd_temp_00,
        zd_rel_00,
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zadar 00 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    savefig("images/profile_comparison_stddev/zd/ftest/profile_comparison_zd_00_JJA_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zd_00_DJF.txt",
        zd_temp_00,
        zd_rel_00,
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zadar 00 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    savefig("images/profile_comparison_stddev/zd/ftest/profile_comparison_zd_00_DJF_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zd_12.txt",
        zd_temp_12,
        zd_rel_12,
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zadar 12 UTC, 2011. - 2020.",
    )
    savefig("images/profile_comparison_stddev/zd/ftest/profile_comparison_zd_12_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zd_12_JJA.txt",
        zd_temp_12,
        zd_rel_12,
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zadar 12 UTC, 2011. - 2020. JJA",
        season="JJA",
    )
    savefig("images/profile_comparison_stddev/zd/ftest/profile_comparison_zd_12_JJA_ftest.png")

    graph.profile_comparison_ftest(
        "data/soundings/zd_12_DJF.txt",
        zd_temp_12,
        zd_rel_12,
        levels,
        title="F-test profila stvarnih vrijednosti i ERA5, Zadar 12 UTC, 2011. - 2020. DJF",
        season="DJF",
    )
    savefig("images/profile_comparison_stddev/zd/ftest/profile_comparison_zd_12_DJF_ftest.png")

    plt.close("all")


def sounding_data_availability():
    graph.sounding_data_availability("./data/soundings/zg.txt", title="Postotak sondažih podataka, Zagreb", city="zg")
    savefig("images/sounding_data_availability/zg.png")

    graph.sounding_data_availability("./data/soundings/zd.txt", title="Postotak sondažih podataka, Zadar", city="zd")
    savefig("images/sounding_data_availability/zd.png")

    plt.close("all")