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

def encode_yes_or_no(train, val, test):
    df_list = [train, val, test]
    
    for df in df_list:
        for col in df.columns.tolist():
            if len(df[col].unique()) == 2:
                if 'Male' in df[col].unique():
                    df[f'{col}_encoded'] = df[col].replace('Male', 1).replace('Female', 0)
                else:
                    df[f'{col}_encoded'] = df[col].replace('Yes', 1).replace('No', 0)
                
    return train, val, test

def prep_telco_data(df):
    df['tenure_years'] = df.tenure // 12
    train, val, test = split_data(df)
    train, val, test = remove_blank_total_charges(train, val, test)
    train, val, test = encode_yes_or_no(train, val, test)
    
    return train, val, test

def remove_blank_total_charges_all_data(df):
    '''Takes in a train, validate, and test DataFrame, removes blank rows, and returns the train, validate, and test DataFrames'''
    df.total_charges = (df.total_charges
                           .str
                           .strip()
                           .replace('', np.nan)
                           .astype('float')
                          )
    
    return df

def encode_yes_or_no_all_data(df):
    for col in df.columns.tolist():
        if len(df[col].unique()) == 2:
            if 'Male' in df[col].unique():
                df[f'{col}_encoded'] = df[col].replace('Male', 1).replace('Female', 0)
            else:
                df[f'{col}_encoded'] = df[col].replace('Yes', 1).replace('No', 0)
                
    return df

def prep_all_data(df):
    df['tenure_years'] = df.tenure // 12
    df = remove_blank_total_charges_all_data(df)
    df = encode_yes_or_no_all_data(df)
    
    return df