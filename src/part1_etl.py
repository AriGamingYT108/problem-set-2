'''
PART 1: ETL
- This code sets up the datasets for Problem Set 2
- NOTE: You will update this code for PART 4: CATEGORICAL PLOTS
'''

import os
import pandas as pd

def create_directories(directories):
    """
    Creates the necessary directories for storing plots and data.

    Args:
        directories (list of str): A list of directory paths to create.
    """
    
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def extract_transform():
    """
    Extracts and transforms data from arrest records for analysis

    Returns:
        - `pred_universe`: The dataframe containing prediction-related data for individuals
        - `arrest_events`: The dataframe containing arrest event data
        - `charge_counts`: A dataframe with counts of charges aggregated by charge degree
        - `charge_counts_by_offense`: A dataframe with counts of charges aggregated by both charge degree and offense category
    """
    # Extracts arrest data CSVs into dataframes
    pred_universe = pd.read_csv('https://www.dropbox.com/scl/fi/a2tpqpvkdc8n6advvkpt7/universe_lab9.csv?rlkey=839vsc25njgfftzakr34w2070&dl=1')
    arrest_events = pd.read_csv('https://www.dropbox.com/scl/fi/n47jt4va049gh2o4bysjm/arrest_events_lab9.csv?rlkey=u66usya2xjgf8gk2acq7afk7m&dl=1')

    # Creates two additional dataframes using groupbys
    charge_counts = arrest_events.groupby(['charge_degree']).size().reset_index(name='count')
    charge_counts_by_offense = arrest_events.groupby(['charge_degree', 'offense_category']).size().reset_index(name='count')

    fta_counts = pred_universe.groupby('fta').size().reset_index(name='count')
    fta_counts_by_sex = pred_universe.groupby(['fta', 'sex']).size().reset_index(name='count')

    # 1. Build a table of whether each arrest had any felony charge
    felony_charge = arrest_events.groupby('arrest_id')['charge_degree'].apply(lambda degs: degs.str.contains('felony', case=False, na=False).any()).reset_index(name='has_felony_charge')

    # 2. Merge that flag onto your pred_universe
    pred_merged = pred_universe.merge(felony_charge,on='arrest_id',how='left')
    



    return (pred_universe, arrest_events, charge_counts, charge_counts_by_offense, fta_counts, fta_counts_by_sex, felony_charge, pred_merged)
