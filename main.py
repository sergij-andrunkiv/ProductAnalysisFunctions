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


# Test the function on the mobile data
if __name__ == '__main__':
    print(convert_csv_to_df("datasets/2020Q4_nps_mobile.csv", "mobile"))
