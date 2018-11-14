# -*- coding: utf-8 -*-

###############################################################################
# This script applies empath on movie reviews
###############################################################################

# Load libraries
import os
import logging
from empath import Empath
import pandas as pd

# Set up folder locations
source_folder_path_list = []
source_folder_path = "C:/Users/Marriane/Documents/GitHub/empath-on-movie-reviews/data/input/scale_whole_review.tar (with text)/scale_whole_review/scale_whole_review/"
folder_list = ["Dennis+Schwartz/txt.parag"] #, "James+Berardinelli/txt.parag", "Scott+Renshaw/txt.parag", "Steve+Rhodes/txt.parag"]
for folder in folder_list:
    folder_loc = source_folder_path + folder
    source_folder_path_list.append(folder_loc)    
print(source_folder_path_list)
    
###############################################################################
## Program Logic
###############################################################################    

if __name__ == "__main__":
    lexicon = Empath()
    result = lexicon.analyze("the quick brown fox jumps over the lazy dog", normalize=True)
    df0 = pd.Series(result, name = 'KeyValue')
    
    col_names = df0.keys()  
    df = pd.DataFrame(columns=col_names)
    
    for folder in source_folder_path_list:
        txt_list = []
        for file in os.listdir(folder):
            if file.endswith(".txt"):
                txt_list.append(file)
                
        for txt_i in txt_list:
            txt_file_name = txt_i
            
            logging.getLogger().setLevel(logging.INFO)
        
            logging.info("Converting " + txt_i)
        
            txt_full_path = os.path.join(folder, txt_file_name)
            try:
                txt_file = open(txt_full_path, 'r')
                lines = txt_file.readlines()
        
                lexicon = Empath()
                result = lexicon.analyze(lines, normalize=True)
        
                new_result = pd.Series(result, name = txt_full_path)
                new_result.index.name = 'Key'
                new_result.reset_index()
        
                df = df.append(new_result)
                        
                logging.info(txt_i, " successfully analyzed")
            except:
                logging.info(txt_i + " open failed")
                   
    df = df.dropna()
    
    # Clean the data frame
    df['Details'] = df.index
    df['Reviewer'] = df['Details'].str.split("/").str[11]
    df['Text file'] = df['Details'].str.split("/").str[12]
    df = df.set_index(['Reviewer', 'Text file'])
    df = df.drop(['Details'], axis = 1)
    
    
    df.to_csv('./data/output/Empath-on-movie-reviews_results.csv', sep=',', encoding='utf-8')
