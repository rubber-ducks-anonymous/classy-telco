from sklearn.model_selection import train_test_split
import numpy as np

def split_data(df):
    '''
    df: pd.DataFrame
    Returns three pd.DataFrames; train, validate, test
    '''
    train, test = train_test_split(df, train_size=.7, random_state=13)
    train, val = train_test_split(train, train_size=.7, random_state=13)
    return train, val, test

def remove_blank_total_charges(train_df, val_df, test_df):
    '''Takes in a train, validate, and test DataFrame, removes blank rows, and returns the train, validate, and test DataFrames'''
    train_df.total_charges = (train_df.total_charges
                           .str
                           .strip()
                           .replace('', np.nan)
                           .astype('float')
                          )
    val_df.total_charges = (val_df.total_charges
                           .str
                           .strip()
                           .replace('', np.nan)
                           .astype('float')
                          )
    test_df.total_charges = (test_df.total_charges
                           .str
                           .strip()
                           .replace('', np.nan)
                           .astype('float')
                          )
    
    return train_df.dropna(), val_df.dropna(), test_df.dropna()

def prep_telco_data(df):
    df['tenure_years'] = df.tenure // 12
    train, val, test = split_data(df)
    train, val, test = remove_blank_total_charges(train, val, test)
    
    
    return train, val, test