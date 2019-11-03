import numpy as np 
import pandas as pd
from pathlib import Path

num_regions = 11
num_simulations = 1000
num_bins = 131

#get dataset_week and 53_week_year from lookup table
dataset_week = 160
year=2013
week=43
is_53_week_year = False

#set up bins
bins = [-0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.0, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 11.0, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12.0, 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8, 12.9, 13.0, 100]
group_names=['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '4.0', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.8', '4.9', '5.0', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '5.8', '5.9', '6.0', '6.1', '6.2', '6.3', '6.4', '6.5', '6.6', '6.7', '6.8', '6.9', '7.0', '7.1', '7.2', '7.3', '7.4', '7.5', '7.6', '7.7', '7.8', '7.9', '8.0', '8.1', '8.2', '8.3', '8.4', '8.5', '8.6', '8.7', '8.8', '8.9', '9.0', '9.1', '9.2', '9.3', '9.4', '9.5', '9.6', '9.7', '9.8', '9.9', '10.0', '10.1', '10.2', '10.3', '10.4', '10.5', '10.6', '10.7', '10.8', '10.9', '11.0', '11.1', '11.2', '11.3', '11.4', '11.5', '11.6', '11.7', '11.8', '11.9', '12.0', '12.1', '12.2', '12.3', '12.4', '12.5', '12.6', '12.7', '12.8', '12.9', '13.0']


print ("Current season is 2013. This season has 52 weeks.")

filename_subs_template = "Long_Flu_Submission_Template_1718.csv"
filepath_subs_template = "C:/Users/SalMustaquim/Dropbox/Influenza Forecasting 2018-19/for applying model to past seasons/Model/" + filename_subs_template

df_sub = pd.read_csv(filepath_subs_template)

df_sub['Value']=8888

filename_sims_plus = "sims_plus_160.csv"
filepath_sims_plus = "C:/Users/SalMustaquim/Desktop/dissertation/" + filename_sims_plus

df_sims_plus = pd.read_csv(filepath_sims_plus)

week_index = df_sims_plus.columns.get_loc(str(week))

for cur_region in range(num_regions):
    print ("processing points for region " + str(cur_region))
    #populate onset_week
    pos=cur_region*729
    df_sub.loc[pos, 'Value'] = df_sims_plus.loc[1000, 'onset_week']
    
    pos=cur_region*729+35
    df_sub.loc[pos, 'Value'] = df_sims_plus.loc[1000, 'peak_week']
    
    pos=cur_region*729+69
    df_sub.loc[pos, 'Value'] = df_sims_plus.loc[1000, 'peak_week_intensity']    

    pos=cur_region*729+201
    #df_sub.loc[pos, 'Value'] = df_sims_plus.loc[1000, '1_wk_ahead']    
    #df_sub.loc[pos, 'Value'] = df_sims_plus.loc[1000, str(week+1)]
    df_sub.loc[pos, 'Value'] = df_sims_plus.iat[1000, week_index+1]

    pos=cur_region*729+333
    #df_sub.loc[pos, 'Value'] = df_sims_plus.loc[1000, '2_wk_ahead']    
    df_sub.loc[pos, 'Value'] = df_sims_plus.iat[1000, week_index+2]
        
    pos=cur_region*729+465
    #df_sub.loc[pos, 'Value'] = df_sims_plus.loc[1000, '3_wk_ahead']    
    df_sub.loc[pos, 'Value'] = df_sims_plus.iat[1000, week_index+3]
        
    pos=cur_region*729+597
    #df_sub.loc[pos, 'Value'] = df_sims_plus.loc[1000, '4_wk_ahead']    
    df_sub.loc[pos, 'Value'] = df_sims_plus.iat[1000, week_index+4]
        
#drop the means row so we can calculate probabilities / counts easier
df_sims_plus=df_sims_plus[0:-1]

# Populate onset_week bins    
for cur_region in range(num_regions):  
    print ("processing bins for region " + str(cur_region))
    pos=cur_region*729+1
    for i in range(40, 53):
         df_sub.loc[pos, 'Value'] = (df_sims_plus.onset_week == i).sum()/1000
         pos=pos+1
    if (is_53_week_year == True):
         df_sub.loc[pos, 'Value'] = (df_sims_plus.onset_week == i).sum()/1000
         pos=pos+1
    for i in range(1, 21):
         df_sub.loc[pos, 'Value'] = (df_sims_plus.onset_week == i).sum()/1000
         pos=pos+1        
    df_sub.loc[pos, 'Value'] = (df_sims_plus.onset_week == 0).sum()/1000
    
# Populate peak_week bins    
for cur_region in range(num_regions):    
    pos=cur_region*729+36
    for i in range(40, 53):
         df_sub.loc[pos, 'Value'] = (df_sims_plus.peak_week == i).sum()/1000
         pos=pos+1
    for i in range(1, 21):
         df_sub.loc[pos, 'Value'] = (df_sims_plus.peak_week == i).sum()/1000
         pos=pos+1     
         
#*********************************************
# Populate peak_intensity bins    
#*********************************************
#create new df with counts for each bin
         
         # begin hack - for some reason, need to read in csv again and update pwi_label again - this keeps zero occurrences
df_for_bins = pd.read_csv("C:/Users/SalMustaquim/Desktop/dissertation/sims_plus_160.csv")
df_for_bins=df_for_bins[0:-1]

df_for_bins['pwi_label']=pd.cut(df_for_bins['peak_week_intensity'], bins, labels=group_names)
#create new df with counts for each bin
bins_hack=pd.value_counts(df_for_bins['pwi_label'])/1000
         # end hack

#first create a list (series) of bins
# bins=pd.value_counts(df_sims_plus['pwi_label'])/1000

df_binstemp = bins_hack.to_frame().reset_index()
df_binstemp.columns = ["Label", "Count"]
df_binstemp=df_binstemp.sort_values('Label')
df_binstemp.reset_index(inplace=True)
del df_binstemp['index']
for cur_region in range(num_regions): 
    
    df_sub.loc[(cur_region*729+70):(cur_region*729+200), 'Value']=df_binstemp['Count'].values

#index_values = dfn.index.values
    
#for cur_region in range(num_regions):    
#    pos=cur_region*729+70
#    for i in range(num_bins):
#         df_sub.loc[pos, 'Value'] = df_binstemp.loc[i, 'Count']
#         pos=pos+1
#    print("pos is: " + str(pos))
    
    
#*********************************************
# Populate Next 4 weeks bins    
#*********************************************
for cur_region in range(num_regions):    
    df_for_bins['1_wk_ahead']=pd.cut(df_for_bins.iloc[:, week_index+1], bins, labels=group_names)
    df_for_bins['2_wk_ahead']=pd.cut(df_for_bins.iloc[:, week_index+2], bins, labels=group_names)
    df_for_bins['3_wk_ahead']=pd.cut(df_for_bins.iloc[:, week_index+3], bins, labels=group_names)
    df_for_bins['4_wk_ahead']=pd.cut(df_for_bins.iloc[:, week_index+4], bins, labels=group_names)
    
    bins_1_week_ahead=pd.value_counts(df_for_bins['1_wk_ahead'])/num_simulations
    bins_2_week_ahead=pd.value_counts(df_for_bins['2_wk_ahead'])/num_simulations
    bins_3_week_ahead=pd.value_counts(df_for_bins['3_wk_ahead'])/num_simulations
    bins_4_week_ahead=pd.value_counts(df_for_bins['4_wk_ahead'])/num_simulations
    
    df_binstemp_wk1 = bins_1_week_ahead.to_frame().reset_index()
    df_binstemp_wk1.columns = ["Label", "Count"]
    df_binstemp_wk1=df_binstemp_wk1.sort_values('Label')
    df_binstemp_wk1.reset_index(inplace=True)
    del df_binstemp_wk1['index']
    df_sub.loc[(cur_region*729+202):(cur_region*729+332), 'Value']=df_binstemp_wk1['Count'].values
    
    df_binstemp_wk2 = bins_2_week_ahead.to_frame().reset_index()
    df_binstemp_wk2.columns = ["Label", "Count"]
    df_binstemp_wk2=df_binstemp_wk2.sort_values('Label')
    df_binstemp_wk2.reset_index(inplace=True)
    del df_binstemp_wk2['index']
    df_sub.loc[(cur_region*729+334):(cur_region*729+464), 'Value']=df_binstemp_wk2['Count'].values
    
    df_binstemp_wk3 = bins_3_week_ahead.to_frame().reset_index()
    df_binstemp_wk3.columns = ["Label", "Count"]
    df_binstemp_wk3=df_binstemp_wk3.sort_values('Label')
    df_binstemp_wk3.reset_index(inplace=True)
    del df_binstemp_wk3['index']
    df_sub.loc[(cur_region*729+466):(cur_region*729+596), 'Value']=df_binstemp_wk3['Count'].values
    
    df_binstemp_wk4 = bins_4_week_ahead.to_frame().reset_index()
    df_binstemp_wk4.columns = ["Label", "Count"]
    df_binstemp_wk4=df_binstemp_wk4.sort_values('Label')
    df_binstemp_wk4.reset_index(inplace=True)
    del df_binstemp_wk4['index']
    df_sub.loc[(cur_region*729+598):(cur_region*729+728), 'Value']=df_binstemp_wk4['Count'].values









# *************************************************************************
# ************************** CREATE SUB FILE (START) **********************
# *************************************************************************

#df_sub = pd.DataFrame(columns=['Location','Target','Type','Unit','Bin_start_incl','Bin_end_notincl','Value'])




filename_sub = "EW" + str(dataset_week) + ".csv"
filepath_sub = "C:/Users/SalMustaquim/Desktop/dissertation/" + filename_sub

df_sub.to_csv(filepath_sub, index=False) 
