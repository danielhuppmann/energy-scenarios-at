import pandas as pd

import pyam


def read_uba_file(
    file,
    sheet_name,
    skiprows,
    usecols,
    df_args,
    variable_col,
    variable_mapping,
    scenario,
    unit,
    col_suffix=None,
    nrows=None,
):
    data = pd.read_excel(
        file, sheet_name=sheet_name, skiprows=skiprows, usecols=usecols, nrows=nrows,
    )

    if col_suffix is not None:
        col_rename_mapping = dict(
            [
                (col, int(col.replace(col_suffix, "")))
                for col in data.columns
                if pyam.utils.is_str(col) and col.endswith(col_suffix)
            ]
        )
        data.rename(columns=col_rename_mapping, inplace=True)

    return (
        pyam.IamDataFrame(
            data, scenario=scenario, variable=variable_col, unit=unit, **df_args
        )
        .filter(
            variable=[
                key for key, value in variable_mapping.items() if value is not None
            ]
        )
        .rename(variable=variable_mapping)
    )
