import os
import pandas as pd
import warnings

# Define the destination directory
FILE_DEST = "./scraped/"

months = [
    "Januar",
    "Februar",
    "Mars",
    "April",
    "Mai",
    "Juni",
    "Juli",
    "August",
    "September",
    "Oktober",
    "November",
    "Desember",
]

tables = [
    "HL050",
    "HL060",
    "HL070",
    "HL075",
    "HL080",
    "HL085",
    "HL090",
]

# Define your custom function
def rename_columns(self):
    self.columns = ['Kategori'] + months[:len(self.columns)-1]
    return self

# Monkey patch the function to the DataFrame class
pd.DataFrame.rename_columns = rename_columns

def guardXls(filename) -> bool:
    return (filename.endswith(".xls") or filename.endswith(".xlsx"))

def extractTable(filename):
    
    for table in tables:
        if table in filename:
            return table

    raise TypeError

def filesInPath(path, verbose=False):
    # Iterate files
    for filename in os.listdir(FILE_DEST):
        if not guardXls(filename):
            continue
        
        try:
            table = extractTable(filename)
        except TypeError:
            continue

        # Temporarily suppress the warning
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            match table:
                case "HL050":
                    print(f'HL050: {filename}')
                    print('Processing sheet: 1. Kjønn Antall')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="1. Kjønn Antall")
                    trimmed_df = df.drop('Unnamed: 0', axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: 2. Kjønn Prosent av arbeidsstyr')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="2. Kjønn Prosent av arbeidsstyr")
                    trimmed_df = df.drop('Unnamed: 0', axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: 3a. Alder Antall')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="3a. Alder Antall")
                    trimmed_df = df.drop('Unnamed: 0', axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: 3b. Alder Kjønn Antall')
                    # TODO: Splitte per kjønn
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="3b. Alder Kjønn Antall")
                    trimmed_df = df.drop('Unnamed: 0', axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: 4. Alder Prosent av arbeidsstyr')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="4. Alder Prosent av arbeidsstyr")
                    trimmed_df = df.drop('Unnamed: 0', axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                case "HL060":
                    print(f'HL060: {filename}')
                    print('Processing sheet: 1. Fylke Antall')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="1. Fylke Antall")
                    trimmed_df = df.drop(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 4'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: 2. Fylke Prosent av arbeidsstyr')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="2. Fylke Prosent av arbeidsstyr")
                    trimmed_df = df.drop(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 4'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: 3. Kommune Antall')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="3. Kommune Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: 4. Kommune Prosent av arbeidsst')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="4. Kommune Prosent av arbeidsst")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)
                case "HL070":
                    print(f'HL070: {filename}')
                    print('Processing sheet: Utdanningsnivå. Antall')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Utdanningsnivå. Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Utdanningsnivå. Andel')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Utdanningsnivå. Andel")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Kjønn. Antall')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Kjønn. Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Kjønn. Andel')
                    # TODO: Splitte per kjønn
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Kjønn. Andel")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Alder. Antall')
                    # TODO: Splitte per kjønn
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Alder. Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Alder. Andel')
                    # TODO: Splitte per kjønn
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Alder. Andel")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Fylke. Antall')
                    # TODO: Splitte per fylke 
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Fylke. Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Fylke. Andel')
                    # TODO: Splitte per fylke 
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Fylke. Andel")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Varighet arbeidssøker. Antall')
                    # TODO: Splitte df på varighet
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Varighet arbeidssøker. Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                case "HL075":
                    print(f'HL075: {filename}')
                    print('Processing sheet: Yrkesgruppe. Antall')
                    # TODO: Splitte df på varighet
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Yrkesgruppe. Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Yrkesgruppe. Andel')
                    # TODO: Splitte df på varighet
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Yrkesgruppe. Andel")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Yrkesgruppe grov og fin. Antall')
                    # TODO: Splitte df på varighet
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Yrkesgruppe grov og fin. Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Fylke. Antall')
                    # TODO: Splitte per fylke 
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Fylke. Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Kjønn. Antall')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Kjønn. Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()
                    
                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Alder. Antall')
                    # TODO: Splitte per kjønn
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Alder. Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Antall. Topp 30 i perioden')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Antall. Topp 30 i perioden")
                    trimmed_df = df.drop(['Unnamed: 0','Unnamed: 1', 'Unnamed: 3'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                case "HL080":
                    print(f'HL080: {filename}')
                    print('Processing sheet: Antall')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Varighet Antall')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Varighet Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Kjønn Antall')
                    # TODO: Splitte per kjønn
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Kjønn Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Varighet Kjønn Antall')
                    # TODO: Splitte per kjønn
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Varighet Kjønn Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Alder Antall')
                    # TODO: Splitte på lengde ledig 
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Alder Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Innvandrerstatus Antall')
                    # TODO: Splitte innvandrerstatus
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Innvandrerstatus Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Utdanningsnivå Antall')
                    # TODO: Splitte på utdanningsnivå 
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Utdanningsnivå Antall")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Langtidsledige Alder Kjønn Anta')
                    # TODO: Splitte på kjønn
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Langtidsledige Alder Kjønn Anta")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: Langtidsledige Fylke Prosent')
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="Langtidsledige Fylke Prosent")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                case "HL085":
                    print(f'HL085: {filename}')

                    print('Processing sheet: 1. Innvandr')
                    # TODO: Splitte
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="1. Innvandr")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: 2. Innvandr Kjønn')
                    # TODO: Splitte
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="2. Innvandr Kjønn")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: 3. Innvandr Alder')
                    # TODO: Splitte
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="3. Innvandr Alder")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: 4. Innvandr verdensdel')
                    # TODO: Splitte
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="4. Innvandr verdensdel")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: 5. Innvandr land')
                    # TODO: Splitte
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="5. Innvandr land")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)

                    print('Processing sheet: 6. Innvandr fylke')
                    # TODO: Splitte
                    df = pd.read_excel(f'{FILE_DEST}/{filename}', sheet_name="6. Innvandr fylke")
                    trimmed_df = df.drop(['Unnamed: 0'], axis=1).dropna().rename_columns()

                    if verbose:
                        print(trimmed_df)
                case "HL090":
                    print(filename)
                case _: 
                    raise TypeError
