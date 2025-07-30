import pandas as pd

def f02__Path2Label(path):
    suploc_tag = path.split("/")[-3]
    year_month = path.split("/")[-2]
    filename = path.split("/")[-1]

    year, month = year_month.split(".")
    subloc_tag = filename.split("_")[0]

    suploc_dict = {
            "Hamaguri Hama_2024.07-2025.05": "H",
            "Onagawa Bay_2024.01-2025.06": "O",
    }

    subloc_tags = ["hg", "mm", "og", "Onagawa_1", "Onagawa_4", "Onagawa_8"]
    subloc_dict = {
        "hg": "hm",
        "mm": "mm",
        "og": "og",
        "Onagawa_1": "s1",
        "Onagawa_4": "s4",
        "Onagawa_8": "s8"
    }

    subloc_tag = ""
    for subloc_tag_tmp in subloc_tags:
        if subloc_tag_tmp in filename:
            subloc_tag = subloc_tag_tmp
            
    suploc = suploc_dict[suploc_tag]
    subloc = subloc_dict[subloc_tag]

    label = f"{year}-{month}-{suploc}-{subloc}"
    return label

def f01__CrtMergedTable(pathes):
    location_flags = [
        "hg", "mm", "og", "Onagawa_1", "Onagawa_4", "Onagawa_8"
    ]

    converted_flags = {
        "hg": "H-hm",
        "mm": "H-mm",
        "og": "H-og",
        "Onagawa_1": "O-s1",
        "Onagawa_4": "O-s4",
        "Onagawa_8": "O-s8"
    }

    df = pd.DataFrame()
    for path in pathes:
        month = path.split("/")[-2]
        location = ""
        for location_flag in location_flags:
            if location_flag in path:
                location = location_flag
        label = f"{month.replace('.', '-')}-{converted_flags[location]}"
        df_tmp = pd.read_csv(path, index_col=0)
        df_tmp["label"] = label
        df = pd.concat(
            [df, df_tmp], axis="index"
        )
    df = df.dropna(axis="columns")
    return df
