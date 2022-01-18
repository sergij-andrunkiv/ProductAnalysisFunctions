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


# Test the function on a corrupted NPS file
if __name__ == '__main__':
    print(check_csv('datasets/corrupted.csv'))
