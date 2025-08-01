'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

def seaborn_settings():
    '''
    Applies the default seaborn theme and sets the default figure size for part 4 plots
    '''
    sns.set_theme()
    sns.set(rc={'figure.figsize': (6, 4)})

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def catplot_felony_prediction(pred_merged):
    '''
    1. Catplot of predicted felony rearrest by charge type

    Parameters:
    - pred_merged: DataFrame containing 'has_felony_charge' and 'prediction_felony'

    Returns:
    - Saves bar plot to './data/part4_plots/catplot_felony_prediction.png'
    '''
    sns.catplot(data=pred_merged,x='has_felony_charge',y='prediction_felony',kind='bar')
    plt.savefig('./data/part4_plots/catplot_felony_prediction.png', bbox_inches='tight')


# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
def catplot_nonfelony_prediction(pred_merged):
    '''
    2. Catplot of predicted non-felony rearrest by charge type

    Parameters:
    - pred_merged: DataFrame containing 'has_felony_charge' and 'prediction_nonfelony'

    Returns:
    - Saves bar plot to './data/part4_plots/catplot_nonfelony_prediction.png'
    '''
    sns.catplot(
        data=pred_merged,
        x='has_felony_charge',
        y='prediction_nonfelony',
        kind='bar'
    )
    plt.savefig('./data/part4_plots/catplot_nonfelony_prediction.png', bbox_inches='tight')
# In a print statement, answer the following question: What might explain the difference between the plots?
    print("Non-felony rearrests occur at a different rate than felony rearrests, which is reflected in the different predicted probabilities.")

# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
def catplot_felony_hue_actual(pred_merged):
    '''
    3. Catplot of predicted felony rearrest by charge type, hued by actual felony rearrest

    Parameters:
    - pred_merged: DataFrame containing 'has_felony_charge', 'prediction_felony', and 'rearrest_felony'

    Returns:
    - Saves bar plot to './data/part4_plots/catplot_felony_actual_hue.png'
    '''
    sns.catplot(
        data=pred_merged,
        x='has_felony_charge',
        y='prediction_felony',
        hue='y_felony',
        kind='bar'
    )
    plt.savefig('./data/part4_plots/catplot_felony_actual_hue.png', bbox_inches='tight')
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime? 
    print("The model places heavy weight on the current felony charge, even if the individual does not get rearrested for a felony crime.")