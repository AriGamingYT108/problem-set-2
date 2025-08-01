'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

def seaborn_settings():
    '''
    Applies the default seaborn theme and sets the default figure size for part 5 plots
    '''
    sns.set_theme()
    sns.set(rc={'figure.figsize': (6, 4)})

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 

def scatterplot_felony_nonfelony_by_charge(pred_merged):
    '''
    1. Using lmplot, create a scatter plot where:
       - x-axis is prediction for felony rearrest
       - y-axis is prediction for non-felony rearrest
       - hue by whether the current charge is a felony (has_felony_charge)

    Parameters:
    - pred_merged: DataFrame with 'prediction_felony', 'prediction_nonfelony', 'has_felony_charge'

    Returns:
    - Saves plot to './data/part5_plots/scatter_felony_nonfelony_by_charge.png'
    '''
    sns.lmplot(
        data=pred_merged,
        x='prediction_felony',
        y='prediction_nonfelony',
        hue='has_felony_charge',
        fit_reg=False
    )
    plt.savefig('./data/part5_plots/scatter_felony_nonfelony_by_charge.png', bbox_inches='tight')
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
    print("Most points on the right are cases with a current felony charge, so the model also assigns them higher non-felony risk.")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
def scatterplot_felony_vs_actual(pred_merged):
    '''
    2. Create a scatterplot where:
       - x-axis is prediction for felony rearrest
       - y-axis is actual felony rearrest outcome (y_felony)

    Parameters:
    - pred_merged: DataFrame with 'prediction_felony' and 'y_felony'

    Returns:
    - Saves plot to './data/part5_plots/scatter_felony_vs_actual.png'
    '''
    sns.scatterplot(
        data=pred_merged,
        x='prediction_felony',
        y='y_felony'
    )
    plt.savefig('./data/part5_plots/scatter_felony_vs_actual.png', bbox_inches='tight')
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
    print("Higher predicted felony risk aligns with more actual felony rearrests, so the model appears reasonably calibrated.")
