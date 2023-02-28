from timeline_baby_names import TimelineBabyNames

data = 'data/yob2000.txt'
tbm = TimelineBabyNames(data=data)

def test_valid_read_file():
    df = tbm.read_data()
    assert df.shape == (29776, 3,)

def test_invalid_read_file():
    bad_data = 'dyob2000.txt'
    tbm = TimelineBabyNames(data=bad_data)
    assert tbm.read_data() == None

def test_calculate_total_births_by_name():
    df = tbm.read_data()
    new_df = tbm.calculate_perc_total_births_by_name(df)
    assert new_df.shape == (29776, 4,)
    assert round(new_df['percentage_births'].sum(), 2) == 100.0

def test_combined_files():
    all_files = [('data/yob'+str(name)+'.txt', name) for name in list(range(1880, 2022))]
    assert tbm.read_and_concatenate_files(all_files).shape == (2052781, 4,)
    