import pandas as pd

def process(path, file, verbose):
    print(f'HL050: {file}')
    print('Processing sheet: 1. Kjønn Antall')
    df = pd.read_excel(f'{path}/{file}', sheet_name="1. Kjønn Antall")
    trimmed_df = df.drop('Unnamed: 0', axis=1).dropna().rename_columns()

    if verbose:
        print(trimmed_df)

    print('Processing sheet: 2. Kjønn Prosent av arbeidsstyr')
    df = pd.read_excel(f'{path}/{file}', sheet_name="2. Kjønn Prosent av arbeidsstyr")
    trimmed_df = df.drop('Unnamed: 0', axis=1).dropna().rename_columns()

    if verbose:
        print(trimmed_df)

    print('Processing sheet: 3a. Alder Antall')
    df = pd.read_excel(f'{path}/{file}', sheet_name="3a. Alder Antall")
    trimmed_df = df.drop('Unnamed: 0', axis=1).dropna().rename_columns()

    if verbose:
        print(trimmed_df)

    print('Processing sheet: 3b. Alder Kjønn Antall')
    # TODO: Splitte per kjønn
    df = pd.read_excel(f'{path}/{file}', sheet_name="3b. Alder Kjønn Antall")
    trimmed_df = df.drop('Unnamed: 0', axis=1).dropna().rename_columns()

    if verbose:
        print(trimmed_df)

    print('Processing sheet: 4. Alder Prosent av arbeidsstyr')
    df = pd.read_excel(f'{path}/{file}', sheet_name="4. Alder Prosent av arbeidsstyr")
    trimmed_df = df.drop('Unnamed: 0', axis=1).dropna().rename_columns()

    if verbose:
        print(trimmed_df)
