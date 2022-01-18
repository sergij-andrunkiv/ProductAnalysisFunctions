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


my_files = {
  "datasets/2020Q4_nps_email.csv": "email",
  "datasets/2020Q4_nps_mobile.csv": "mobile",
  "datasets/2020Q4_nps_web.csv": "web",
  "datasets/corrupted.csv": "social_media"
}
# Test the function on the my_files dictionary
if __name__ == '__main__':
    print(combine_nps_csvs(my_files))
