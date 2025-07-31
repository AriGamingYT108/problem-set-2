'''
- You will run Problem Set 2 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5

def main():
    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    directories = ['data/part2_plots', 'data/part3_plots', 'data/part4_plots', 'data/part5_plots']
    part1.create_directories(directories)
    
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense, fta_counts, fta_counts_by_sex, felony_charge, pred_merged  = part1.extract_transform()
    
    ##  PART 2: PLOT EXAMPLES  ##
    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)

    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##
    part3.seaborn_settings()

    # 1
    part3.fta_barplot(fta_counts)

    # 2
    part3.fta_barplot_by_sex(fta_counts_by_sex)

    # 3
    part3.age_histogram(pred_universe)
    # 4
    part3.age_group_histogram(pred_universe)

    ##  PART 4: CATEGORICAL PLOTS  ##
    part4.seaborn_settings()

    print(felony_charge['has_felony_charge'].value_counts())

    # 1
    part4.catplot_felony_prediction(pred_merged)
    # 2
    part4.catplot_nonfelony_prediction(pred_merged)
    # 3
    part4.catplot_felony_hue_actual(pred_merged)

    ##  PART 5: SCATTERPLOTS  ##
    # 1
    
    # 2


if __name__ == "__main__":
    main()
