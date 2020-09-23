import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt  
#import seaborn as sns
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.model_selection import cross_val_score
#from sklearn.metrics import classification_report, confusion_matrix
#from sklearn.metrics import make_scorer
#from sklearn.metrics import accuracy_score
#import ast

pd.set_option("display.max_columns", 100)

def str_to_list(x):
    return eval(x) if x and x != '#N/A' else []

list_cols = ['genres', 'belongs_to_collection', 'production_companies', 'production_countries', 'spoken_languages', 'Keywords', 'cast', 'crew']


io_params = {'index_col': 'id', 'converters': {col: str_to_list for col in list_cols}}

# We can read the train and the test in one go using the concat function
data = pd.concat(
    objs=(
        pd.read_csv('/Users/SirishaBojjireddy/Documents/courses/R programming/kraggle project/tmdb-box-office-prediction/train_copy.csv', **io_params).assign(is_train=True),
        pd.read_csv('/Users/SirishaBojjireddy/Documents/courses/R programming/kraggle project/tmdb-box-office-prediction/test_copy.csv', **io_params).assign(is_train=False)
        ),
    sort=False
)

list_cols = ['genres', 'belongs_to_collection', 'production_companies', 'production_countries', 'spoken_languages', 'Keywords', 'cast', 'crew']

# Here for each column in list above, we make an empty list s, and then for each line in the column, we extract the id info and append it to s
# Then, we put the list back into the dataframe, replacing the original unclean values of the column
for col in list_cols:
    s=[]
    for l in data[col]:
        m=[d['id'] for d in l if 'id' in d]
        s.append(m)        
    data[col]=s
        
print(data.head())
