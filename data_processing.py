from sklearn.model_selection import train_test_split as tts
def find_constant_columns(dataframe):
    # This function takes the column and return the single fuinction
    constant_columns=[]
    for column in dataframe.columns:
        unique_values = dataframe[column].unique()
        if(len(unique_values)==1):
            constant_columns.append(column)
    return constant_columns

def find_columns_with_few_values(dataframe,threshold):
    few_values_columns = []
    for column in dataframe.columns:
        few_values_columns = []
        for column in dataframe.columns:
            unique_values_count = len(dataframe[column].unique())
            if(unique_values_count < threshold):
                few_values_columns.append(column)
    return few_values_columns

def drop_and_fill(dataframe):
    cols_to_drop = dataframe.columns[dataframe.isnull().sum()]
    dataframe = dataframe.drop(cols_to_drop,axis = 1)
    dataframe = dataframe.fillna(dataframe.mean())
    return dataframe
