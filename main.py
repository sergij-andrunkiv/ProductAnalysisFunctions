import pandas as pd


def convert_csv_to_df(csv_name, source_type):
    """ Converts an NPS CSV into a DataFrame with a column for the source.
    Args:
        csv_name (str): The name of the NPS CSV file.
        source_type (str): The source of the NPS responses.
    Returns:
        A DataFrame with the CSV data and a column, source. """

    df = pd.read_csv(csv_name)
    df['source'] = source_type
    # Define a new column nps_group which applies categorize_nps to nps_rating
    df['nps_group'] = df['nps_rating'].apply(categorize_nps)
    return df


def check_csv(csv_name):
    """ Checks if a CSV has three columns: response_date, user_id, nps_rating
    Args:
        csv_name (str): The name of the CSV file.
    Returns:
        Boolean: True if the CSV is valid, False otherwise. """

    with open(csv_name) as f:
        first_line = f.readline()
        if first_line == "response_date,user_id,nps_rating\n":
            return True
        else:
            return False


def combine_nps_csvs(csvs_dict):
    """ Converts all csv_files to DataFrames by adding the source and group columns,
        and combines them into one DataFrame
        Args:
            csvs_dict (dict): The dictionary of pair (csv_file: source_column)
        Returns:
            DataFrame: the combined DataFrame """

    combined = pd.DataFrame()
    for name, source in csvs_dict.items():
        if check_csv(name) is True:
            temp = convert_csv_to_df(name, source)
            combined = pd.concat([combined, temp])
        else:
            print(name + " is not a valid file and will not be added.")
    return combined


def categorize_nps(x):
    """ Takes a NPS rating and outputs whether it is a "promoter",
    "passive", "detractor", or "invalid" rating. "invalid" is
    returned when the rating is not between 0-10.
    Args:
        x: The NPS rating
    Returns:
        String: the NPS category or "invalid". """

    if x >= 0 and x <= 6:
        return 'detractor'
    elif x == 7 or x == 8:
        return 'passive'
    elif x == 9 or x == 10:
        return 'promoter'
    else:
        return 'invalid'


if __name__ == '__main__':
    print(convert_csv_to_df("datasets/2020Q4_nps_mobile.csv", "mobile"))
