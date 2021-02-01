import ms1.matching as matching

csv_filepath = "data/test_masses.csv"
ftrs_filepath = "data/test_ms_data.ftrs"

raw_data = matching.ftrs_reader(ftrs_filepath)
theo_masses = matching.theo_masses_reader(csv_filepath)
mod_test = ['Sodium','Nude', 'DeAc']
results = matching.data_analysis(raw_data, theo_masses, 0.5, mod_test)

results.to_csv("data/baseline_output.csv")