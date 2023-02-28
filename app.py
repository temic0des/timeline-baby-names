import matplotlib.pyplot as plt
import numpy as np
from timeline_baby_names import TimelineBabyNames


def main():
    data = 'data/yob2000.txt'
    tbm = TimelineBabyNames(data=data)

    # Read Data
    df = tbm.read_data()

    # Print the first five rows of the data
    print("---------- Print the first five rows of the data ----------")
    print(df.head())
    print()

    # Calculate for each name in yob2000.txt its percentage of total births. 
    # Store this percentage as an additional column.

    print("---------- Calculate for each name in yob2000.txt its percentage of total births. ----------")
    df_new = None
    try:
        df_new = tbm.calculate_perc_total_births_by_name(df)
        print(df_new.head())
    except AttributeError:
        pass
    print()

    # Read all the files and add an extra column for year. 
    # Concatenate them into a single data structure
    print("---------- Read all the files and add an extra column for year. ----------")
    filenames = [('data/yob'+str(name)+'.txt', name) for name in list(range(1880, 2022))]
    df_all = tbm.read_and_concatenate_files(filenames)
    print(df_all.head())
    print(df_all.tail())
    print()

    # Calculate the total number of births for each year. Visualize the timeline as a line plot
    print('---------- Calculate the total number of births for each year. ----------')
    total_births_year = tbm.total_births_per_year(df_all).reset_index()
    print(total_births_year)
    print()

    tbm.timeline_plot(x=np.asarray(total_births_year['year'], int), y=total_births_year['number'], 
                      title='Visualization of the year vs total number of births',
                      x_label='Year', y_label='Total number of births')

    # Now, create a timeline for your own name. First check if your name occurs at all. If yes, create a table with the columns year and number.
    # You may want to sum up the binary genders or choose one. With few exceptions, the influence on the result is tiny.
    # If your name is not very frequent, there might be missing data for some years. Insert missing data with a 0.  
    # Draw a line plot and label the axes.

    print("---------- create a timeline for your own name ----------")
    name = 'Temitope'
    df_my_name = tbm.name_timeline(df=df_all, my_name=name).reset_index()
    print(df_my_name)
    print()


    tbm.timeline_plot(x=np.asarray(df_my_name['year'], int), y=df_my_name['number'], 
                      title='Timeline of my name by year', x_label='Year', y_label='Name count')
 

    # Investigate the popularity of the names of some US celebrities over the last 130 years. Plot a time line with 2-4 names.
    print("---------- Investigate the popularity of the names of some US celebrities over the last 130 years. ----------")
    celebrity_names = ['jackson', 'barak', 'madonna', 'denzel']
    df_celebrity = tbm.investigate_celebrity_names(df_all, celebrity_names)
    print(df_celebrity.head())
    print(df_celebrity.tail())

    print("---------- Names Timeline ----------")
    names_timeline = df_celebrity.groupby(['year', 'name'])['number'].sum().unstack().fillna(value=0)
    print(names_timeline)
    names_timeline.plot(kind='line')
    plt.show()

    # print(df_my_name[(df_my_name['year'].map(lambda x: total_births_year['year'] == x).notnull()) & (df_my_name['number'].map(lambda x: x / total_births_year['number']))])
    # print(x[x.where(x['name'] == 'Temitope').notnull()])
    

if __name__ == '__main__':
    main()