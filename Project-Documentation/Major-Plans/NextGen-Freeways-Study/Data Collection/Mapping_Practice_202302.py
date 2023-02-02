import os
import csv
import numpy as np
import pandas as pd
from pandas import DataFrame
import xlrd
import pyreadr

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Compare results for the following runs (i.e. show metric values and percent change for 5 maps)
# Location: L:\Application\Model_One\NextGenFwys\Scenarios:
# 2035 mock 13 segments (2035_TM152_NGF_NP02_BPALT13segments_01)
# 2035 mock 100+ segments (2035_TM152_NGF_NP02_BPALTsegmented_03)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# names of folders for runs listed above
list_dir = ['2035_TM152_NGF_NP02_BPALTsegmented_03','2035_TM152_NGF_NP02_BPALT13segments_01']

# define path location for folders above
file_loc = "L:\\Application\\Model_One\\NextGenFwys\\Scenarios"

#list of full file directories
loadednetworkvehclass_to_VMT_file_list = [os.path.join(file_loc, i, 'OUTPUT', 'avgload5period_vehclasses.csv') for i in list_dir]

# load major and minor groupings of tollclasses for visualization purposes
minor_link_lookup = "C:\\Users\\jalatorre\\Box\\NextGen Freeways Study\\05 Modeling\\3_Coding\\Tollclasses\\TollclassGrouping.csv"
minor_links_df = pd.read_csv(minor_link_lookup)
minor_groups = minor_links_df['Grouping minor'].unique()

def tally_vmt(roadvols_df): #borrowed code from PBA2050 ... sum vmt across links, will be used for toll class groupings
    """
    Tallies the oVMT autos, small trucks and large trucks, as well as the total VMT.
    Adds the following keys to the metrics_dict:
    * road_vmt_auto                  : VMT by autos
    * road_vmt_smtr                  : VMT by small trucks
    * road_vmt_lrtr                  : VMT by large trucks
    """
#     print("Tallying roads cost and vmt")
#     roadvols_df = pandas.read_csv(os.path.join("hwy","iter%d" % iteration, "avgload5period_vehclasses.csv"), sep=",")

    

    # keep sums

    auto_vmt = 0
    smtr_vmt = 0
    lrtr_vmt = 0

    for timeperiod in ['EA','AM','MD','PM','EV']:
        # total auto volume for the timeperiod
        roadvols_df['vol%s_auto' % timeperiod] = roadvols_df['vol%s_da'  % timeperiod] + roadvols_df['vol%s_s2'  % timeperiod] + roadvols_df['vol%s_s3'  % timeperiod] + \
                                                 roadvols_df['vol%s_dat' % timeperiod] + roadvols_df['vol%s_s2t' % timeperiod] + roadvols_df['vol%s_s3t' % timeperiod]
        # vmt
        roadvols_df['vmt%s_auto' % timeperiod] = roadvols_df['vol%s_auto' % timeperiod]*roadvols_df['distance']
        roadvols_df['vmt%s_smtr' % timeperiod] = roadvols_df['distance']*(roadvols_df['vol%s_sm' % timeperiod]+roadvols_df['vol%s_smt' % timeperiod])
        roadvols_df['vmt%s_lrtr' % timeperiod] = roadvols_df['distance']*(roadvols_df['vol%s_hv' % timeperiod]+roadvols_df['vol%s_hvt' % timeperiod])
       
        auto_vmt += roadvols_df['vmt%s_auto' % timeperiod].sum()
        smtr_vmt += roadvols_df['vmt%s_smtr' % timeperiod].sum()
        lrtr_vmt += roadvols_df['vmt%s_lrtr' % timeperiod].sum()

    # return it

#     metrics_dict['road_vmt_auto']                 = auto_vmt
#     metrics_dict['road_vmt_smtr']                 = smtr_vmt
#     metrics_dict['road_vmt_lrtr']                 = lrtr_vmt
    return auto_vmt

def sum_grouping(network_df): #sum congested time across selected toll class groupings
    return network_df['ctimAM'].sum()


def file_list_to_csv(file_list, file_name): # read through a list of directories for files of the same type (different blueprints), combine the files in one csv and add identifying columns
    n = 0 #use to designate runs
    ab100seg = pd.read_csv('C:\\Users\\jalatorre\\Documents\\GitHub\\Spatial-Analysis-Mapping-Projects\\Project-Documentation\\Major-Plans\\NextGen-Freeways-Study\\Data Collection')
    df_output = ab100seg.copy()
    for file in file_list:
        print("Opening and saving %s"%file)
        df_temp = pd.read_csv(file)
        df_temp['a_b'] = df_temp['a'].astype(str) + '_' + df_temp['b'].astype(str)
        df_temp = df_temp.merge(ab100seg, on='a_b', how='left')
        df_temp = df_temp.merge(minor_links_df,how='left',left_on=['TOLLCLASS'],right_on=['TOLLCLASS (network links 100plusSeg.shp)'])
        try:
            for i in minor_groups:
            #     filter each minor link_AMPM, get average value for VMT (for minor link), reassign to each a_b link
                avgvmt = np.mean([tally_vmt(df_temp.loc[df_temp['Grouping minor_AMPM'] == i+'_AM'].copy()), tally_vmt(df_temp.loc[df_temp['Grouping minor_AMPM'] == i+'_PM'].copy())])
                avgtime = np.mean([sum_grouping(df_temp.loc[df_temp['Grouping minor_AMPM'] == i+'_AM'].copy()),sum_grouping(df_temp.loc[df_temp['Grouping minor_AMPM'] == i+'_PM'].copy())])
                df_temp.loc[df_temp['Grouping minor'] == i,'VMT_' + str(n)] = avgvmt
                df_temp.loc[df_temp['Grouping minor'] == i,'Grouping minor ctimAM_' + str(n)] = avgtime    

            df_output = df_output.merge(df_temp[['a_b','VMT_' + str(n), 'Grouping minor ctimAM_' + str(n)]], on='a_b', how='left')
            print("Appended %s"%file)   

        except:
            print("Folder does not exist: " + file) 
        n = n + 1

    df_output.to_csv(os.path.join(os.getcwd(),file_name), header=True, index=False)
    print('here:' + os.path.join(os.getcwd(),file_name))
    print ("Successfully wrote " + file_name)


file_list_to_csv(loadednetworkvehclass_to_VMT_file_list, "Practice_Mapping_Outputs.csv")

