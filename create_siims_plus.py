import numpy as np 
import pandas as pd
from pathlib import Path

dir_sims_corr = "C:/Users/SalMustaquim/Dropbox/Influenza Forecasting 2018-19/for applying model to past seasons/Model/Tree_Regression/outfiles/sims_corr/"

cur_region = 0

#get dataset_week and 53_week_year from lookup table - *NOT DONE YET*
#hardcoding following variables to complete one test run
cur_week = 160
year=2013
week=43
is_53_week_year = False

bins = [-0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.0, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 11.0, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12.0, 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8, 12.9, 13.0, 100]
group_names=['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '4.0', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.8', '4.9', '5.0', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '5.8', '5.9', '6.0', '6.1', '6.2', '6.3', '6.4', '6.5', '6.6', '6.7', '6.8', '6.9', '7.0', '7.1', '7.2', '7.3', '7.4', '7.5', '7.6', '7.7', '7.8', '7.9', '8.0', '8.1', '8.2', '8.3', '8.4', '8.5', '8.6', '8.7', '8.8', '8.9', '9.0', '9.1', '9.2', '9.3', '9.4', '9.5', '9.6', '9.7', '9.8', '9.9', '10.0', '10.1', '10.2', '10.3', '10.4', '10.5', '10.6', '10.7', '10.8', '10.9', '11.0', '11.1', '11.2', '11.3', '11.4', '11.5', '11.6', '11.7', '11.8', '11.9', '12.0', '12.1', '12.2', '12.3', '12.4', '12.5', '12.6', '12.7', '12.8', '12.9', '13.0']

def get_onset_week(fname):
    a=1
    
print ("We are in 2013-14, week 43. This season has 52 weeks.")
 
# *** START LOOP TO LOOP THROUGH REGIONS HERE - NOT DONE YET ***

#Construct filename from cur_week and cur_region
filename_sims_corr = str(cur_week) + "_region0" + str(cur_region) + ".csv"
filepath_sims_corr = dir_sims_corr + filename_sims_corr

#create sims_plus dataframe from sims_corr data
print ("Creating Sims Plus ...")
df_sims_plus_data = pd.read_csv(filepath_sims_corr)
print ("Completed reading data from " + filepath_sims_corr)


# *** Rename column headers to reflect weeks 40-26 ***
df_sims_plus_data.columns = ['40','41','42', '43', '44', '45','46','47', '48', '49', '50','51','52', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26' ]


# *** Add the row of means at the bottom ***
print ("- Adding means row ...")
df_sims_plus_data.loc['mean'] = df_sims_plus_data.mean()



# *** Find columns that contain simulation data. ***
col_of_weeks = df_sims_plus_data.loc[: , "40":"26"]


# *************************************************************************
# **************************** PEAK WEEK (START) **************************
# *************************************************************************
# Add peak_week column: Finds peak_week for each simulation and for mean
print ("- Adding peak_week column ...")
df_sims_plus_data['peak_week'] = df_sims_plus_data.idxmax(axis=1)
# *************************************************************************
# **************************** PEAK WEEK (END) ****************************
# *************************************************************************


# *************************************************************************
# ************************ PEAK WEEK INTENSITY (START) ********************
# *************************************************************************
# Add peak_week_intensity column: Finds peak_week_intensity for each simulation and for mean
print ("- Adding peak_week_intensity column ...")
df_sims_plus_data['peak_week_intensity'] = col_of_weeks.max(axis=1)
# *************************************************************************
# ************************ PEAK WEEK INTENSITY (END) **********************
# *************************************************************************


# *************************************************************************
# **************************** ONSET WEEK (START) *************************
# *************************************************************************
print ("- Adding onset column ...")

# Load in baseline value
#print ("  - First load in baselines for 2013-14 ...")
get_onset_week(cur_region)
filepath_baselines = "C:/Users/SalMustaquim/Dropbox/Influenza Forecasting 2018-19/for applying model to past seasons/Model/baseline2013.csv"
df_baselines_data = pd.read_csv(filepath_baselines,header=None)
baseline=df_baselines_data.iat[cur_region,0]
#print ("  - Completed reading baseline data from " + filepath_baselines)
# Run algorithm
#print ("- onset_week found, column added [fake] ...")
#Get list of all column names
#columns = list(df_sims_plus_data)
# Add onset_week column and set to 0; values will be populated in loop below
df_sims_plus_data.loc[:,'onset_week'] = 0
for i in range(1000): # for each simulation (i)
    #print("\nsim #:", i)
    for j in range(39-2): # for each week (j)
           if ((df_sims_plus_data.iat[i,j] > baseline) & (df_sims_plus_data.iat[i,j+1] > baseline) & (df_sims_plus_data.iat[i,j+2] > baseline)):
                #print ("onset found! onset is week", df_sims_plus_data.columns.values[j])
                #print ("- Adding onset to onset column ...")
                #Found onset for this simulation, populate the onset cell
            df_sims_plus_data.loc[i, 'onset_week'] = df_sims_plus_data.columns.values[j]
            break
    else:
        print ("   - ALERT! No onset found in simulation #", i)
               
    # finally, find onset for mean (index 1000)               
    for j in range(39-2): # for each week (j)
           if ((df_sims_plus_data.iat[1000,j] > baseline) & (df_sims_plus_data.iat[1000,j+1] > baseline) & (df_sims_plus_data.iat[1000,j+2] > baseline)):
                #print ("onset found! onset is week", df_sims_plus_data.columns.values[j])
                #print ("- Adding onset to onset column ...")
                #Found onset for this simulation, populate the onset cell
            df_sims_plus_data.loc['mean', 'onset_week'] = df_sims_plus_data.columns.values[j]
            break
    else:
        print ("   - ALERT! No onset found in mean row")                            
# *************************************************************************
# **************************** ONSET WEEK (END) ***************************
# *************************************************************************


# *************************************************************************
# ********************* PEAK WEEK INTENSITY LABELS (START) *****************
# *************************************************************************
# Add pwi_labels column: Puts the peak_week_intensity items into binsb
print ("- Adding peak_week_intensity labels column ...")
df_sims_plus_data['pwi_label']=pd.cut(df_sims_plus_data['peak_week_intensity'], bins, labels=group_names)

# *************************************************************************
# ********************* PEAK WEEK INTENSITY LABELS (END) *******************
# *************************************************************************


# *************************************************************************
# **************************** NEXT 4 WEEKS (START) **************************
# *************************************************************************
# Add peak_week column: Finds peak_week for each simulation and for mean
week_index = df_sims_plus_data.columns.get_loc(str(week))
print ("- Adding next 4 weeks labels columns ...")
df_sims_plus_data['next_1_wk_label']=pd.cut(df_sims_plus_data['peak_week_intensity'], bins, labels=group_names)
# *************************************************************************
# **************************** PEAK WEEK (END) ****************************
# *************************************************************************



# ********************** Sims Plus creation successful ********************

print ("Completed creation of Sims Plus ...")

filepath_sims_plus = "C:/Users/SalMustaquim/Desktop/dissertation/sims_plus_160.csv"
print ("Writing updated Sims Plus data to  " + filepath_sims_plus)
df_sims_plus_data.to_csv(filepath_sims_plus) 
print ("Completed writing Sims Plus data.")



# *************************************************************************
# ************************** CREATE SUB FILE (START) **********************
# *************************************************************************


