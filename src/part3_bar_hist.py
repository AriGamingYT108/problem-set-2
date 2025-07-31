'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

def seaborn_settings():
    '''
    Applies the default seaborn theme and sets the default figure size for part 3 plots
    '''
    sns.set_theme()
    sns.set(rc={'figure.figsize': (6, 4)})

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def fta_barplot(fta_counts):
    '''
    1. Bar plot for the fta column.

    Parameters:
    - fta_counts dataframe (from ETL)

    Returns:
    - Bar plot of FTA counts saved as PNG
    '''
    sns.barplot(data=fta_counts, x='fta', y='count')
    plt.savefig('./data/part3_plots/fta_barplot.png', bbox_inches='tight')



# 2. Hue the previous barplot by sex
def fta_barplot_by_sex(fta_counts_by_sex):
    '''
    2. Bar plot for fta by sex.

    Parameters:
    - fta_counts_by_sex dataframe (from ETL)

    Returns:
    - Bar plot of FTA counts by sex saved as PNG
    '''
    sns.barplot(data=fta_counts_by_sex, x='fta', y='count', hue='sex')
    plt.savefig('./data/part3_plots/fta_barplot_by_sex.png', bbox_inches='tight')
# 3. Plot a histogram of age_at_arrest
def age_histogram(pred_universe):
    '''
    3. Histogram of age_at_arrest.

    Parameters:
    - pred_universe dataframe

    Returns:
    - Histogram saved as 'age_histogram.png'
    '''
    sns.histplot(data=pred_universe, x='age_at_arrest')
    plt.savefig('./data/part3_plots/age_histogram.png', bbox_inches='tight')

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def age_group_histogram(pred_universe):
    '''
    Parameters:
    - pred_universe dataframe

    Returns:
    - Histogram saved as 'age_group_histogram.png'
    '''
    bins = [18, 21, 30, 40, 100]
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=bins)
    plt.savefig('./data/part3_plots/age_group_histogram.png', bbox_inches='tight')
