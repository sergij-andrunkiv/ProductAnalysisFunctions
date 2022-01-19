import functions as paf

my_files = {
  "datasets/2020Q4_nps_email.csv": "email",
  "datasets/2020Q4_nps_web.csv": "web",
  "datasets/2020Q4_nps_mobile.csv": "mobile",
}
# Test the function on the my_files dictionary
if __name__ == '__main__':
    print(paf.convert_csv_to_df(next(key for key, value in my_files.items() if value == 'email'), my_files.get('email')))

    print(paf.check_csv(next(key for key, value in my_files.items() if value == 'email')))

    print(paf.combine_nps_csvs(my_files))

    print(paf.categorize_nps(3))
    print(paf.categorize_nps(7))
    print(paf.categorize_nps(10))

    q4_nps = paf.combine_nps_csvs(my_files)
    print(paf.calculate_nps(q4_nps))
    print(paf.calculate_nps_by_source(q4_nps))
