import pandas as pd
import matplotlib.pyplot as plt

class TimelineBabyNames:

    header_names = ('name', 'sex', 'number',)

    def __init__(self, data) -> None:
        self.data = data

    def read_data(self, header=None):
        '''
            This method reads a csv file, takes the header as input,
            and returns a dataframe. If the file is invalid, 
            None is returned
        '''
        try:
            df = pd.read_csv(self.data, header=header)
            df.columns = self.header_names
            return df
        except FileNotFoundError:
            print('file not found')

    def calculate_perc_total_births_by_name(self, df):
        '''
            This method takes the data as input, calculates
            the percentage births by name, and returns a dataframe
            with the percentage births
        '''
        try:
            total_births = float(df[self.header_names[2]].sum())
            df['percentage_births'] = df[self.header_names[2]].map(lambda each_num: (each_num * 100.0) / total_births)
            return df
        except AttributeError:
            pass
        except IndexError:
            pass
        except FileNotFoundError:
            pass
        except ZeroDivisionError:
            pass

    def read_and_concatenate_files(self, files):
        '''
            This method takes the files as input,
            and returns a row-wise combination of
            all the files with the year column attached
            to the dataframe
        '''
        df_files = []

        for file in files:
            try:
                data = pd.read_csv(f'{file[0]}', names=self.header_names)
                data['year'] = file[1]
                df_files.append(data)
            except IndexError:
                pass
        df_combined = pd.concat(df_files, axis=0, ignore_index=True)
        return df_combined
    
    def total_births_per_year(self, df):
        '''
            This methods gets the data as input and returns the
            sum of the total births per year
        '''
        try:
            total_births = df.groupby('year')[self.header_names[-1]].sum()
            return total_births
        except IndexError:
            pass

    def name_timeline(self, df, my_name):
        '''
            This method takes the combined data and my name to search for as input,
            then returns a Dataframe of the searched name
        '''
        try:
            df_check_name = df[df[self.header_names[-1]].where((df[self.header_names[0]].str.lower() == my_name.lower()) \
                                                        & (df[self.header_names[1]] == 'M')) \
                .notnull()]
            return df_check_name
        except IndexError:
            pass
    

    def investigate_celebrity_names(self, df, names):
        '''
            This method takes the data and names as input,
            and returns a DataFrame of the celebrity names
        '''
        max_year = df['year'].max()
        last_130_years = max_year - 130
        df_celeb_names = df[(df[self.header_names[0]].str.lower().isin(names)) & (df['year'] >= last_130_years)]
        return df_celeb_names
    
    def timeline_plot(self, x, y, title, x_label, y_label):
        '''
            This method takes the x axis column, y axis column, title,
            xlabel and ylabel as input and plots a line graph
        '''
        plt.figure(figsize=(12, 8))
        plt.plot(x, y)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()