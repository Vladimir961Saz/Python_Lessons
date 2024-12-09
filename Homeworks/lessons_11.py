import pandas as pd


def chickenpox_by_sex():

    df = pd.read_csv(r"C:\Users\Владимир\Downloads\NISPUF17.csv")

    had_chickenpox_and_vaccine = df[
        (df["HAD_CPOX"] == 1) & (df["P_NUMVRC"] >= 1)
    ]

    grouped_by_sex = had_chickenpox_and_vaccine.groupby(
        "SEX").agg(count=("SEX", "count"))

    ratios = {}
    for sex, count in grouped_by_sex["count"].items():
        not_contracted = df[
            (df["SEX"] == sex) & (df["HAD_CPOX"] == 2) & (df["P_NUMVRC"] >= 1)
        ].shape[0]
        ratio = count / not_contracted

        if sex == 1:
            ratios["male"] = ratio
        else:
            ratios["female"] = ratio

    return ratios


if __name__ == "__main__":
    print(chickenpox_by_sex())
