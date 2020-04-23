from sklearn.model_selection import train_test_split

def split_data(df):
    train, test = train_test_split(df, train_size=.7, random_state=13)
    train, val = train_test_split(train, train_size=.7, random_state=13)
    return train, val, test