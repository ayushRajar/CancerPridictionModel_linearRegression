import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def bin_to_num(data):
    binnedInc = []
    for i in data["binnedInc"]:
        i=i.strip("()[]")
        i=i.split(",")
        i=tuple(i)
        i=tuple(map(float,i))
        i=list(i)
        binnedInc.append(i)
    data["binnedInc"] = binnedInc

    data["lower_bound"] = [i[0] for i in data["binnedInc"]]
    data["upper_bound"] = [i[1] for i in data["binnedInc"]]
    data["median"] = (data["lower_bound"]+data["upper_bound"])/2
    data.drop("binnedInc",axis = 1 , inplace = True)
    return data

def cat_to_col(data):
    data["county"] = [i.split(",")[0] for i in data["Geography"]]
    data["state"] = [i.split(",")[0] for i in data["Geography"]]
    data.drop("Geography",axis = 1 , inplace = True)
    return data

def one_hot_encoding(X):
    categorial_columns = X.select_dtypes(include=["object"]).columns
    one_hot_encoder = OneHotEncoder(sparse_output = False , handle_unknown="ignore")
    one_hot_encoded = one_hot_encoder.fit_transform(X[categorial_columns])

    one_hot_encoded = pd.DataFrame(
        one_hot_encoded,columns=one_hot_encoder.get_feature_names_out(categorial_columns)

    )
    X=X.drop(categorial_columns,axis=1)
    X=pd.concat([X, one_hot_encoded],axis=1)
    return X
